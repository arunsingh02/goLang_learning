# Simply comparing the string with padding '0' on the major version

def test(node_version, min_required_version):
    node_version = convert_to_number(node_version)
    print('node : ', node_version)
    min_required_version = convert_to_number(min_required_version)
    print('MIN : ', min_required_version)
    if node_version < min_required_version:
        print("Smaller than min version")
        return
    print('Greater or equal than min version')
    return

def convert_to_number(version_str):
    version_li = []
    for i, ver in enumerate(version_str.split('.')):
         if not i and len(ver) == 1:
            version_li.append("0%s"%ver)
         else:
             version_li.append(ver)
    return '.'.join(version_li)

test('10.1.1', '9.12.1')    # 10.1.1 and 9.12.1
test('10.1.1', '9.123.198')
test('9.07.1', '9.12.1')
test('10.1.1', '9.0.0')
test('10.0', '9.12.1')
test('9.13.1', '9.12.1')
test('9.111.99999', '9.12.1')
test('09.11.123', '9.12.1')
test('9.12.1', '9.12.1')
test('9.0', '9.12.1')
test('9.12.0', '9.12.1')


def sort_package_version_info(data_list: list) -> list:
    """
    Sorting package version list.

    Args:
        data_list (list): containing package data

    Example:
        input = [
            ('a', '0.a'),
            ('b', '10.1.01'),
            ('c', 'a.a.1'),
            ('d', '.1.b.'),
            ('e', '0.1.212.3231.121.ab')
        ]
        Padding 0 according to largest master version in all given version to sort by string
        intermediate result = [
            ('d', '00.1.0b.'),
            ('e', '00.1.212.3231.121.ab'),
            ('a', '00.a'),
            ('c', '0a.a.01'),
            ('b', '10.1.01')
        ]
        output = [
            ('d', '.1.b.'),
            ('e', '0.1.212.3231.121.ab'),
            ('a', '0.a'),
            ('c', 'a.a.1'),
            ('b', '10.1.01')
        ]

    Returns:
        list: sorted version list
    """
    try:
        master_version_list = []
        for _package_name, version in data_list:
            master_version_list.append(
                ([len(version_list) for version_list in version.split(".")], version)
            )
        print(master_version_list)
        if not master_version_list:
            return data_list
        max_master_version = sorted(master_version_list)[-1][1]
        master_version_details = [len(x) for x in max_master_version.split(".")]
        print(master_version_details, '>>>>>', max_master_version)
        final_version_list = []
        for package_name, version in data_list:
            final_version = ".".join(
                [
                    "0" * (master_version_details[index] - len(version_list)) + version_list
                    if (
                        version_list != max_master_version
                        and len(master_version_details) - 1 >= index
                        and len(version_list) < master_version_details[index]
                    )
                    else version_list
                    for index, version_list in enumerate(version.split("."))
                ]
            )
            final_version_list.append((package_name, final_version, version))
        print(final_version_list)
        sorted_version_list = sorted(final_version_list, key=lambda version_tup: version_tup[1])
        return [(version_tup[0], version_tup[2]) for version_tup in sorted_version_list]
    except TypeError:
        logger.exception("Cannot supported sorting between instances of 'int' and 'str'")
    except IndexError:
        logger.exception("Tuple index out of range while sort the versions")
    except Exception as err:
        logger.exception(f"Not able to sort the versions\n {err}")
    return data_list

#print(sort_package_version_info([
#            ('a', '0.a'),
#            ('b', '10.11.01'),
#            ('c', 'a.a.1'),
#            ('d', '.1.b.'),
#            ('e', '0.1.212.3231.121.ab')
#        ]))
