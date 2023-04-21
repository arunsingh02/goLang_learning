#!/usr/bin/python3

# This script provides a convenient way to call the SignSshKeys API method and automate the building of the local
# ssl keychain in order to allow for key based authentication access to the remote shell of an Element node.
#
# The most basic usage of this script is to execute it with only providing the ip parameter:
#
# ./SignSshKeys.py --ip 1.2.3.4
#
# However, this will only succeed when the ip is of a node that is not a member of a cluster.
#
# In the case that the ip is of a node that is a member of a cluster, then the user parameter will need to be specified
# with a value of a cluster user name (this will prompt for the associated password):
#
# ./SignSshKeys.py --ip 1.2.3.4 --user admin
#
# In either example above, if the script executes successfully then it will create the necessary keychain files in
# the working directory in order to enable key based authentication. In order to log into the target node, simply use
# the ssh command with the -i flag to specify the private key:
#
# ssh -i user 1.2.3.4
#
# Note that 'user' maps to the file names used in the keychain files (user, user.pub, and user-cert.pub).
#
# Additionally, it is important to note that the keychain will allow equivalent key based authentication access to all
# nodes in a cluster, not just the node for which the command was targetted at.
#
# Lastly, refer the the commands --help flag for usage information.

import argparse
import base64
import getpass
import json
import os
import re
import stat
import sys

try:
    import requests
except ModuleNotFoundError:
    print("Error: the requests module cannot be imported and is required to run this script.\n"
          "Please check your Python path or install and run again.\n"
          "More information can be found at https://docs.python-requests.org/")
    exit(1)

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_VERSION = "12.5"

def is_cluster_api_supported(ip, headers):
    response = call_api(ip, method="GetAPI", headers=headers, api_version="0.0")
    return API_VERSION in response["result"]["supportedVersions"]

def build_headers(user=None, passwd=None):
    headers={"Content-Type": "application/json"}

    if user is not None and passwd is not None:
        auth_string = user + ":" + passwd
        b64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        headers["Authorization"] = "Basic " + b64

    return headers

def build_params(args):
    params=dict()
    if args.duration is not None:
        params["duration"] = args.duration
    if args.publickey is not None:
        with open(args.publickey, "r") as key:
            params["publicKey"] = [line.rstrip('\n') for line in key][0]
    if args.sfadmin:
        params["sfadmin"] = "true"

    return params

def call_api(ip, method, headers, params=None, api_version=API_VERSION):
    if params is None:
        params = {}

    base_url = f"https://{ip}:442"
    url_path = f"/json-rpc/{api_version}"
    url = f"{base_url}{url_path}"
    payload = json.dumps({"method":method,"params":params})

    try:
        response = requests.request(method="POST", url=url, headers=headers, data=payload, verify=False, timeout=10)

        if response.status_code != 200:
            raise Exception(response)

        response = response.json()
    except ValueError as ex:
        print(f"API response is not valid JSON: {response}, exception={ex}")
        exit(1)
    except Exception as ex:
        print(f"API call failed at {base_url} due to {ex}")
        exit(1)

    return response

def is_response_successful(response):
    if "error" in response.keys():
        error = response["error"]
        print("API call could not complete successfully. See error below. \n"
             f"\t status code: \t{error['code']} \n"
             f"\t reason: \t{error['message']} \n"
             f"\t exception: \t{error['name']}")
        return False
    elif "result" not in response.keys():
        print("An unknown or unexpected error occurred. See error below and contact Netapp support. \n"
             f"\t {response}")
        return False
    return True

def populate_keychain(response, publickey=None):
    try:
        signed_key = response["result"]["signedKeys"]
        status = signed_key["keygen_status"]
    except KeyError as ex:
        print(f"An unknown or unexpected error occurred due to {ex}. See response below and contact Netapp support. \n"
              f"\t {response}")
        exit(1)

    if 'public_key' in signed_key.keys():
        with open("user.pub", "w") as public_key:
            public_key.write(signed_key["public_key"])

    if 'private_key' in signed_key.keys():
        private_key = base64.b64decode(signed_key["private_key"]).decode("utf-8")

        with open("user", "w") as private:
            private.write(private_key)

        os.chmod("user", stat.S_IREAD | stat.S_IWRITE)

    if publickey is not None:
        user_cert = re.split(r'\.pub$', publickey)[0] + "-cert.pub"
    else:
        user_cert = "user-cert.pub"

    with open(user_cert, "w") as signed:
        signed.write(signed_key["signed_public_key"])

    print(f"{status} \n"
    f"\t Specify the private key with '-i' option when executing ssh to the node.")

def parse_args(args):

    def check_ip(value):
        if not re.match('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', value):
            raise argparse.ArgumentTypeError(f"is not a valid IP address: '{value}'")

        return value

    def check_duration(value):
        try:
            if int(value) <= 0:
                raise argparse.ArgumentTypeError(f"must be a positive integer greater than 0: '{value}'")
        except ValueError:
            raise argparse.ArgumentTypeError(f"invalid integer value: '{value}'")

        return value

    def check_path(value):
        if not os.path.isfile(value):
            raise argparse.ArgumentTypeError("must be a valid filesystem path that contains a file")

        return value

    parser = argparse.ArgumentParser(description="Communicates with the Solidfire Element SignSshKeys API for ease of use. Initiates api call to Solidfire node, then takes the response and writes ssh key(s) to files for remote access.")
    parser.add_argument(
        "--ip", "-i", required=True, type=check_ip, help="IP address of the target node for the api to run against."
    )
    parser.add_argument(
        "--user", "-u", help="Cluster user used in api call."
    )
    parser.add_argument(
        "--duration", "-d", type=check_duration, help="How long a signed key should remain valid. Integer in hours."
    )
    parser.add_argument(
        "--publickey", "-k", type=check_path, help="Path to a user provided public key."
    )
    parser.add_argument(
        "--sfadmin", "-s", action="store_true", help="Request access to sfadmin user."
    )

    return parser.parse_args()

def main(args):
    parsed_args = parse_args(args)
    passwd = None

    if parsed_args.user is None:
        empty_user = input("User was not provided. Proceed without credentials? (y/n):")
        if empty_user != "y":
            print("Exiting. Please specify a user with --user and run again.")
            exit(1)
    else:
        passwd = getpass.getpass(prompt=f"Enter password for cluster user '{parsed_args.user}':")

    headers = build_headers(parsed_args.user, passwd)

    if is_cluster_api_supported(parsed_args.ip, headers):
        params = build_params(parsed_args)
        response = call_api(parsed_args.ip, method="SignSshKeys", headers=headers, params=params)
        if is_response_successful(response):
            populate_keychain(response, parsed_args.publickey)
    else:
        print(f"SignSshKeys API call is not supported on the node with ip {parsed_args.ip}. "
              f"Check that the IP address is correct and that the Element version is {API_VERSION} or greater.")

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nExiting on keyboard interrupt...")
