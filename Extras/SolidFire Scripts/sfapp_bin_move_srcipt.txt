# Author: Arun Singh
# Email: Arun.Singh2@netapp.com

import argparse
from random import randint
from requests import request
import sys
import subprocess

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def collect_active_nodes_info(mvip):
    """API call function"""
    print("Hitting ListActiveNodes API to collect storage nodes IPs")
    url = f"https://{mvip}/json-rpc/8.2?method=ListActiveNodes"

    print(
        "To get the authorization, make an API call with postman and use the basic auth, <username>/<password>, "
        "and then when you click the code button underneath send, generate the python requests code and "
        "you will get the header object. Currently we generated basic auth for admin/admin."
    )
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46YWRtaW4='
    }
    try:
        response = request("GET", url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            return data["result"]["nodes"] if data else []
        return {}
    except:
        print(
            "Failing while collecting Nodes IPs info. Please check MVIP "
            "and basic authorization value (username and password) (generated via postman) and try again."
        )


def run(mvip, storage_ips, username, src, dest, binBackup, revertCluster):
    """Main Function"""
    if not storage_ips:
        nodes = collect_active_nodes_info(mvip)
        storage_ips = []
        for node in nodes:
            storage_ips.append(node["cip"])

    print(f"Total number of Nodes : {len(storage_ips)}")
    print(f"Storage IPs : {', '.join(storage_ips)}")
    print("Start copying sfapp to the nodes")

    for storage_ip in storage_ips:
        print(f"\n============================{storage_ip}===================================\n")

        # Running `stop solidfire` command to inactivate the solidfire service.
        print(" ".join(["ssh", f"{username}@{storage_ip}", "stop solidfire"]))
        subprocess.run(["ssh", f"{username}@{storage_ip}", "stop solidfire"])

        # Take by default backup at the very first time of destination sfapp (Internal)
        status = subprocess.run(["ssh", f"{username}@{storage_ip}", f"test -e {dest}/sfapp.org"])
        if status.returncode:
            # print(" ".join(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp {dest}/sfapp.org"]))
            subprocess.run(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp {dest}/sfapp.org"])

        if binBackup:
            # Running `cp sfapp sfapp_<bkp_no>` command to take backup of sfapp on node.
            ran = randint(1, 1000)
            print(" ".join(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp {dest}/sfapp_{ran}"]))
            subprocess.run(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp {dest}/sfapp_{ran}"])

        # Running `rm -f sfapp` command to delete existing sfapp on node.
        print(" ".join(["ssh", f"{username}@{storage_ip}", f"rm -f {dest}/sfapp"]))
        subprocess.run(["ssh", f"{username}@{storage_ip}", f"rm -f {dest}/sfapp"])

        if revertCluster:
            # Copy orginal sfapp back to make cluster up and running
            print(" ".join(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp.org {dest}/sfapp"]))
            subprocess.run(["ssh", f"{username}@{storage_ip}", f"cp {dest}/sfapp.org {dest}/sfapp"])
        else:
            # Running `scp` command to copy the new sfapp to the node.
            print(f"scp {src} {username}@{storage_ip}:{dest}")
            subprocess.run(["scp", src, f"{username}@{storage_ip}:{dest}"])

        # Running `start solidfire` command to activate the solidfire service.
        print(" ".join(["ssh", f"{username}@{storage_ip}", "start solidfire"]))
        subprocess.run(["ssh", f"{username}@{storage_ip}", "start solidfire"])

    print("Done")
    print(
        "We can refresh the cluster UI page, if loaded successfully means services are up and running. "
        "Otherwise please ssh to nodes and check `status solidfire` to confirm solidfire services are active."
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        fromfile_prefix_chars="@",
        description="This script will copy the sfapp (BIN) to all nodes to get new changes in element code snippet."
    )

    nodeOptionsGroup = parser.add_mutually_exclusive_group(required=True)
    nodeOptionsGroup.add_argument('-m', '--mvip', type=str, help='Cluster MVIP')
    nodeOptionsGroup.add_argument('-n', '--nodes', nargs="+", help='List of node IP addresses')
    parser.add_argument('-u', '--user', type=str, required=False, default="root",
                        help='(Optional) Node administrator username (Default value : root)')
    parser.add_argument('-s', '--src', type=str, required=False,
                        help='sfapp source path (Optional only while running revert command)')
    parser.add_argument('-d', '--dest', type=str, required=False, default="/sf/bin",
                        help='(Optional) sfapp destination path (Default value : /sf/bin)')
    parser.add_argument('-b', '--backup', action='store_true', dest='binBackup',
                        help='Backup of existing bin of cluster (Second way to copy sfapp at destination)')
    parser.add_argument('-r', '--revert', action='store_true', dest='revertCluster',
                        help='Revert Cluster with old bin (In case of any failure with new sfapp)')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    userArgs = parser.parse_args()
    run(userArgs.mvip, userArgs.nodes, userArgs.user, userArgs.src, userArgs.dest, userArgs.binBackup,
        userArgs.revertCluster)
