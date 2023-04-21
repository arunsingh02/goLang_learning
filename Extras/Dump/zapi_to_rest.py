def r_system_cli_inline_dedupe_on(cluster, credentials, node_name):
    """ Rest API to get system CLI inline dedupe on info for given node

    Args:
        cluster (object): Cluster object has detailed information about a cluster, used in the REST API URL.
        credentials (dict): Cluster credentials
            ex. {‘user’: ‘admin’, ‘pw’: ‘mypass’}
        node_name (str): Node name 

    Returns:
        bool: True/False

    Raises:
        SDOTAdminError: Raises when any error occurs during API request.

    Exceptions:
        exception: exception will be logged in case of error
    """
    output = None
    url = None
    try:
        with HostConnection(cluster.cluster_mgmt_ip, credentials['user'], credentials['pw'], verify=False) as conn:
            url = "{0}{1}{2}".format(conn.origin, Constants.REST_API_URL['system-cli'], 'version')
            response = conn.session.get(url, params={'node': '*', 'fields': ['version']})

        url = utils.decode_url(response.url)
        Logger().log_debug('Cluster [{0}]: "GET {1}" response: {2}'.format(cluster.name, url, response.text))
        if response.status_code == 200:
            node_info_dict = response.json()['records']
            output = '{0} entry {1} acted on.'.format(len(node_info_dict), 'were' if len(node_info_dict) > 1 else 'was')
            for node_dict in node_info_dict:
                output += '\n\nNode: {0}\n{1}'.format(node_dict.get('node'), node_dict.get('version'))
            Logger().log_debug('Cluster [{0}]: "GET {1}" system CLI node version: {2}'.format(cluster.name, url, output))
        else:
            Logger().log_error('Cluster [{0}]: System CLI, failed to get version.'.format(cluster.name))
            error_detail = response.json().get('error', {}).get('message')
            err_msg = 'REST returned bad status {0}: {1}'.format(response.status_code, error_detail)
            raise SDOTAdminError('ONTAPSelectSysCLIVersionFailed', params=(err_msg,))
    except Exception as exc:
        Logger().log_error('Cluster [{0}]: "GET {1}" System CLI version REST exception: {2}'.format(cluster.name, url, exc))
        raise SDOTAdminError('ONTAPSelectSysCLIVersionFailed', params=str(exc))
    return output
