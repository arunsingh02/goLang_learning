from re import findall

def test():
    resp = { "records": [ { "node": "ArunS_2node-01", "version": "NetApp Release Lighthouse__9.13.0: Tue Nov 08 07:42:19 UTC 2022" }, { "node": "ArunS_2node-02", "version": "NetApp Release Lighthouse__9.13.0: Tue Nov 08 07:42:19 UTC 2022" } ], "num_records": 2 }
    resp = { "records": []}# { "node": "test-cluster-dns-01", "version": "NetApp Release Lighthouse__9.13.0: Tue Nov 08 07:42:19 UTC 2022" } ], "num_records": 1 }
    node_info_dict = resp['records']
    #output = '{0} entry was acted on.'.format(len(node_info_dict))
    output = '{0} entry {1} acted on.'.format(len(node_info_dict), 'were' if len(node_info_dict) > 1 else 'was')
    for node_dict in node_info_dict:
        output += '\n\nNode: {0}\n{1}'.format(node_dict.get('node'), node_dict.get('version'))
    #return output.rstrip('\n')
    version = '2 entry was acted on.\n\nNode: Test_node-01\nNetApp Release devN_9.1.0: Tue Nov 08 07:42:19 UTC 2022\n\n \
            Node: Test_node-02\nNetApp Release devN_9.2.0:: Tue Nov 08 07:42:19 UTC 2022'
    print(version)
    node_versions = list(findall('NetApp Release (.+?):', version))
    assert len(node_versions) == 2
    assert node_versions[0] == 'devN_9.1.0'
    assert node_versions[1] == 'devN_9.2.0'
    print(node_versions)

    a = {'ONTAPSelectSysCLIVersionFailed': {'category': 'cluster', 'message': 'Failed to get ONTAP Select version. Reason: %s.'}}
    print(a['ONTAPSelectSysCLIVersionFailed']['message'] % ('Hi Arun singh',))
    return output


def aa():
    a ='{\n  "output": "2 entries were acted on.\\n\\nNode: add_disk2-01\\nNetApp Release devN_230304_0200: Sat Mar  4 02:54:02 EST 2023<1>\\n\\nNode: add_disk2-02\\nNetApp Release devN_230304_0200: Sat Mar  4 02:54:02 EST 2023   <1>\\n\\n"\n}'
    b = '2 entries were acted on.\n\nNode: add_disk2-01\nNetApp Release devN_230304_0200: Sat Mar  4 02:54:02 EST 2023   <1>\n\nNode: add_disk2-02\nNetApp Release devN_230304_0200: Sat Mar  4 02:54:02 EST 2023   <1>\n\n' 
    import re
    x = list(re.findall('NetApp Release (.+?):', b))
    print(x)


aa()
#print({'a':test()})
#print(test())
