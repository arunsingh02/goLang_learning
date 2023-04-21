
def prepare_storage_disk_details(storage_disk_data, node_name):
    """ Prepare the storage disks information

    Args:
        storage_disk_data (dict): Detailed information of storage disks
        node_name (object): Node name

    Returns:
        list: Storage disks data
    """
    storage_disk = []
    for disk in storage_disk_data.get('records', []):
        # In order to collect unassigned disk information, only the container_type filter is added,
        # since disk-inventory-info.location does not exist.
        if disk.get('container_type') != 'unassigned':
            continue
        storage_disk_dict = {
                'disk-inventory-info': {},
                'disk-metrocluster-info': {},
                'disk-name': '',
                'disk-ownership-info': {},
                'disk-paths': {},
                'disk-raid-info': {},
                'disk-stats-info': {},
                'disk-uid': '',
                }

        # disk-inventory-info
        storage_disk_dict['disk-inventory-info']['capacity-sectors'] = disk.get('sector_count', 0)
        storage_disk_dict['disk-inventory-info']['physical-size'] = disk.get('physical_size', 0)
        storage_disk_dict['disk-inventory-info']['disk-class'] = disk.get('class')
        storage_disk_dict['disk-inventory-info']['disk-cluster-name'] = disk.get('name')
        storage_disk_dict['disk-inventory-info']['disk-type'] = disk.get('type')
        storage_disk_dict['disk-inventory-info']['disk-uid'] = disk.get('uid')
        storage_disk_dict['disk-inventory-info']['firmware-revision'] = disk.get('firmware_version')
        storage_disk_dict['disk-inventory-info']['is-shared'] = disk.get('container_type')
        storage_disk_dict['disk-inventory-info']['model'] = disk.get('model')
        storage_disk_dict['disk-inventory-info']['serial-number'] = disk.get('serial_number')
        storage_disk_dict['disk-inventory-info']['storage-sed-info'] = {
                'is-fips-sed': str(disk.get('fips_certified')).lower(),
                'is-sed': str(disk.get('self_encrypting')).lower()
                }
        storage_disk_dict['disk-inventory-info']['vendor'] = disk.get('vendor')

        storage_disk_dict['disk-inventory-info']['bytes-per-sector'] = disk.get('bytes_per_sector', 0)
        storage_disk_dict['disk-inventory-info']['disk-effective-type'] = disk.get('effective-type')
        storage_disk_dict['disk-inventory-info']['drawer'] = disk.get('drawer', {}).get('id')
        storage_disk_dict['disk-inventory-info']['drawer-slot'] = disk.get('drawer', {}).get('slot')
        storage_disk_dict['disk-inventory-info']['rpm'] = disk.get('rpm')
        storage_disk_dict['disk-inventory-info']['shelf-bay'] = disk.get('bay')
        storage_disk_dict['disk-inventory-info']['shelf-uid'] = disk.get('shelf', {}).get('uid')
        storage_disk_dict['disk-inventory-info']['storage-sed-info'] = {
                'data-key-id': disk.get('key_id', {}).get('id'),
                'fips-key-id': disk.get('key_id', {}).get('fips'),
                'is-fips-sed': disk.get('fips_certified'),
                'is-sed': disk.get('self_encrypting'),
                'protection-mode': disk.get('protection_mode'),
                'percent-rated-life-used': disk.get('rated_life_used_percent')
                }
        storage_disk_dict['disk-inventory-info']['virtual-machine-disk-info'] = {
                'vmdisk-container-name': disk.get('virtual', {}).get('container_name'),
                'vmdisk-object-name': disk.get('virtual', {}).get('object_name'),
                'vmdisk-storage-account': disk.get('virtual', {}).get('storage_account')
                }

        # disk-metrocluster-info
        storage_disk_dict['disk-metrocluster-info']['is-local-attach'] = str(disk.get('local')).lower()

        # disk-name
        storage_disk_dict['disk-name'] = disk.get('name')

        # disk-ownership-info
        storage_disk_dict['disk-ownership-info']['disk-uid'] = disk.get('uid')
        storage_disk_dict['disk-ownership-info']['home-node-name'] = disk.get('home_node', {}).get('name')
        storage_disk_dict['disk-ownership-info']['owner-node-name'] = disk.get('node', {}).get('name')
        storage_disk_dict['disk-ownership-info']['pool'] = disk.get('pool')
        storage_disk_dict['disk-ownership-info']['dr-home-node-name'] = disk.get('dr_node', {}).get('name')
        storage_disk_dict['disk-ownership-info']['owner-node-id'] = disk.get('system', {}).get('uuid')

        # disk-paths
        disk_path_info = []
        for path_dict in disk.get('paths', []):
            disk_path_info.append(
                    {
                        'initiator': path_dict.get('initiator'),
                        'disk-port': path_dict.get('port_name'),
                        'node': path_dict.get('node', {}).get('name'),
                        'disk-port-name': path_dict.get('port_type'),
                        'disk-target-wwnn': path_dict.get('wwnn'),
                        'disk-target-wwpn': path_dict.get('wwpn'),
                        'vmdisk-hypervisor-file-name': path_dict.get('vmdisk_hypervisor_file_name')
                        }
                    )
        if len(disk_path_info) > 1:
            storage_disk_dict['disk-paths']['disk-path-info'] = disk_path_info
        else:
            storage_disk_dict['disk-paths']['disk-path-info'] = disk_path_info[0]

        # disk-raid-info
        storage_disk_dict['disk-raid-info']['active-node-name'] = disk.get('node', {}).get('name')
        storage_disk_dict['disk-raid-info']['container-type'] = disk.get('container_type')
        storage_disk_dict['disk-raid-info']['disk-outage-info'] = {
                'is-in-fdr': str(disk.get('outage', {}).get('persistently_failed')).lower(),
                'reason': disk.get('outage', {}).get('reason')
                }
        storage_disk_dict['disk-raid-info']['disk-uid'] = disk.get('uid')
        storage_disk_dict['disk-raid-info']['spare-pool'] = disk.get('pool')
        storage_disk_dict['disk-raid-info']['effective-disk-type'] = disk.get('effective_type')
        storage_disk_dict['disk-raid-info']['used-blocks'] = disk.get('usable_size', 0)
        storage_disk_dict['disk-raid-info']['disk-shared-info'] = {'storage-pool': disk.get('storage_pool', {}).get('name')}
        storage_disk_dict['disk-raid-info']['error-text-list'] = disk.get('errors', {}).get('reason')
        storage_disk_dict['disk-raid-info']['error-type'] = disk.get('errors', {}).get('type')

        storage_disk_dict['disk-raid-info']['disk-aggregate-info'] = {'aggregate-name': []}
        storage_disk_dict['disk-raid-info']['disk-shared-info'] = {'aggregate-list': []}
        for aggregate_dict in disk.get('aggregates', []):
            storage_disk_dict['disk-raid-info']['disk-aggregate-info']['aggregate-name'].append(aggregate_dict.get('name'))
            storage_disk_dict['disk-raid-info']['disk-shared-info']['aggregate-list'].append(aggregate_dict.get('name'))

        # disk-stats-info
        storage_disk_dict['disk-stats-info']['average-latency'] = disk.get('stats', {}).get('average_latency')
        storage_disk_dict['disk-stats-info']['bytes-per-sector'] = disk.get('bytes_per_sector')
        storage_disk_dict['disk-stats-info']['disk-io-kbps'] = disk.get('stats', {}).get('throughput')
        storage_disk_dict['disk-stats-info']['disk-iops'] = disk.get('stats', {}).get('iops_total')
        storage_disk_dict['disk-stats-info']['disk-uid'] = disk.get('uid')
        storage_disk_dict['disk-stats-info']['path-error-count'] = disk.get('stats', {}).get('path_error_count', 0)
        storage_disk_dict['disk-stats-info']['power-on-time-interval'] = disk.get('stats', {}).get('power_on_hours')

        # disk-uid
        storage_disk_dict['disk-uid'] = disk.get('uid')

        storage_disk.append(storage_disk_dict)
    return storage_disk
