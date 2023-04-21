def r_set_dns(cluster, credentials, dns_config_info):
    """ Rest API for set DNS config for given cluster

    Args:
        cluster (object): Cluster object has detailed information about a cluster, used in the REST API URL.
        credentials (dict): Cluster credentials
            ex. {‘user’: ‘admin’, ‘pw’: ‘mypass’}
        dns_config_info (dict): dns config info dict
            ex. {'domains':['domain.com'], 'name-servers':['1.2.3.4']}

    Returns:
        bool: True/False

    Raises:
        SDOTAdminError: Raises when any error occurs during API request.

    Exceptions:
        exception: exception will be logged in case of error
    """
    set_dns_success = False
    url = None
    try:
        with HostConnection(cluster.cluster_mgmt_ip, credentials['user'], credentials['pw'], verify=False) as conn:
            url = "{0}{1}".format(conn.origin, Constants.REST_API_URL['name-services-dns'])
            dns_config_info["servers"] = dns_config_info.pop("name-servers") if "name-servers" in dns_config_info else []
            dns_config_info["svm"] = {"name": cluster.name}
            response = conn.session.post(url, json=dns_config_info)
        Logger().log_error('Cluster [{0}]: "POST {1}" response: {2}'.format(cluster.name, url, response.text))
        if response.status_code == 201:
            set_dns_success = True
    except Exception as exc:
        Logger().log_error('Cluster [{0}]: "POST {1}" error: {2}'.format(cluster.name, url, exc))
        raise SDOTAdminError('DnsSetupFailed', params=str(exc))
    return set_dns_success
