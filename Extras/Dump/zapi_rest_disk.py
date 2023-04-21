data = {
    "records": [
        {
            "name": "NET-2.1",
            "uid": "34363435:36316534:00000000:00000000:00000000:00000000:00000000:00000000:00000000:00000000",
            "serial_number": "3436343536316534",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "type": "vmdisk",
            "class": "virtual",
            "container_type": "mediator",
            "pool": "pool0",
            "node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0f",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "53059d50444f5476",
                    "wwpn": "53059d50444f5476",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "outage": {
                "persistently_failed": False,
                "reason": {
                    "message": "Failed disk. Reason: \"\".",
                    "code": "721081"
                }
            },
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 47104,
            "right_size_sector_count": 34304,
            "physical_size": 24117248,
            "stats": {
                "average_latency": 16,
                "throughput": 2048,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-2.1?fields=**"
                }
            }
        },
        {
            "name": "NET-2.2",
            "uid": "35356537:66393933:00000000:00000000:00000000:00000000:00000000:00000000:00000000:00000000",
            "serial_number": "3535653766393933",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "type": "vmdisk",
            "class": "virtual",
            "container_type": "mediator",
            "pool": "pool0",
            "node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0f",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "53059d50444f5476",
                    "wwpn": "53059d50444f5476",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "outage": {
                "persistently_failed": False,
                "reason": {
                    "message": "Failed disk. Reason: \"\".",
                    "code": "721081"
                }
            },
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 47104,
            "right_size_sector_count": 34304,
            "physical_size": 24117248,
            "stats": {
                "average_latency": 16,
                "throughput": 3072,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-2.2?fields=**"
                }
            }
        },
        {
            "name": "NET-1.4",
            "uid": "4E455441:50502020:30303030:30303030:36307147:39767636:65334A34:00000000:00000000:00000000",
            "serial_number": "0000000060qG9vv6e3J4",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 53680537600,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "spare",
            "pool": "pool0",
            "state": "spare",
            "node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530291aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                },
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530891aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 104857592,
            "right_size_sector_count": 104844800,
            "physical_size": 53687087104,
            "stats": {
                "average_latency": 16,
                "throughput": 1024,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-1.4?fields=**"
                }
            }
        },
        {
            "name": "NET-1.3",
            "uid": "4E455441:50502020:30303030:30303030:46333532:4E376747:51333032:00000000:00000000:00000000",
            "serial_number": "00000000F352N7gGQ302",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 71866187776,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "aggregate",
            "pool": "pool1",
            "state": "present",
            "node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "aggregates": [
                {
                    "uuid": "42f9b1a2-96f6-4572-b98a-f06d229c882d",
                    "name": "aggr0_ArunS_2node_02",
                    "_links": {
                        "self": {
                            "href": "/api/storage/aggregates/42f9b1a2-96f6-4572-b98a-f06d229c882d"
                        }
                    }
                }
            ],
            "local": True,
            "paths": [
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530291aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                },
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530891aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 142606328,
            "right_size_sector_count": 142593536,
            "physical_size": 73014439936,
            "stats": {
                "average_latency": 16,
                "throughput": 3993600,
                "iops_total": 27,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-1.3?fields=**"
                }
            }
        },
        {
            "name": "NET-3.3",
            "uid": "4E455441:50502020:30303030:30303030:4A332D69:65524747:304A3032:00000000:00000000:00000000",
            "serial_number": "00000000J3-ieRGG0J02",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 71866187776,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "aggregate",
            "pool": "pool1",
            "state": "present",
            "node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "aggregates": [
                {
                    "uuid": "f8b8efd2-f7dc-48a7-93d8-a93bc283d2bf",
                    "name": "aggr0_ArunS_2node_01",
                    "_links": {
                        "self": {
                            "href": "/api/storage/aggregates/f8b8efd2-f7dc-48a7-93d8-a93bc283d2bf"
                        }
                    }
                }
            ],
            "local": True,
            "paths": [
                {
                    "initiator": "0b",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb0e000000",
                    "wwpn": "530191aabb0e0000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 142606328,
            "right_size_sector_count": 142593536,
            "physical_size": 73014439936,
            "stats": {
                "average_latency": 16,
                "throughput": 418816,
                "iops_total": 12,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-3.3?fields=**"
                }
            }
        },
        {
            "name": "NET-1.2",
            "uid": "4E455441:50502020:30303030:30303030:58356533:304F5447:6D594233:00000000:00000000:00000000",
            "serial_number": "00000000X5e30OTGmYB3",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 53680537600,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "spare",
            "pool": "pool1",
            "state": "spare",
            "node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530291aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                },
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530891aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 104857592,
            "right_size_sector_count": 104844800,
            "physical_size": 53687087104,
            "stats": {
                "average_latency": 16,
                "throughput": 1024,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-1.2?fields=**"
                }
            }
        },
        {
            "name": "NET-3.1",
            "uid": "4E455441:50502020:30303030:30303030:58377075:434A5142:705A4634:00000000:00000000:00000000",
            "serial_number": "00000000X7puCJQBpZF4",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 53680537600,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "spare",
            "pool": "pool1",
            "state": "spare",
            "node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0b",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb0e000000",
                    "wwpn": "530191aabb0e0000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 104857592,
            "right_size_sector_count": 104844800,
            "physical_size": 53687087104,
            "stats": {
                "average_latency": 16,
                "throughput": 1024,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-3.1?fields=**"
                }
            }
        },
        {
            "name": "NET-3.4",
            "uid": "4E455441:50502020:30303030:30303030:61355352:7437787A:534A3833:00000000:00000000:00000000",
            "serial_number": "00000000a5SRt7xzSJ83",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 53680537600,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "spare",
            "pool": "pool0",
            "state": "spare",
            "node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "local": True,
            "paths": [
                {
                    "initiator": "0b",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb0e000000",
                    "wwpn": "530191aabb0e0000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 104857592,
            "right_size_sector_count": 104844800,
            "physical_size": 53687087104,
            "stats": {
                "average_latency": 16,
                "throughput": 1024,
                "iops_total": 0,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-3.4?fields=**"
                }
            }
        },
        {
            "name": "NET-1.1",
            "uid": "4E455441:50502020:30303030:30303030:652D3646:67786855:4D6E5A35:00000000:00000000:00000000",
            "serial_number": "00000000e-6FgxhUMnZ5",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 71866187776,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "aggregate",
            "pool": "pool0",
            "state": "present",
            "node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c64bbe-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-01",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c64bbe-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "aggregates": [
                {
                    "uuid": "f8b8efd2-f7dc-48a7-93d8-a93bc283d2bf",
                    "name": "aggr0_ArunS_2node_01",
                    "_links": {
                        "self": {
                            "href": "/api/storage/aggregates/f8b8efd2-f7dc-48a7-93d8-a93bc283d2bf"
                        }
                    }
                }
            ],
            "local": True,
            "paths": [
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530291aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                },
                {
                    "initiator": "0d",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb56000000",
                    "wwpn": "530891aabb560000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 142606328,
            "right_size_sector_count": 142593536,
            "physical_size": 73014439936,
            "stats": {
                "average_latency": 16,
                "throughput": 396288,
                "iops_total": 11,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-1.1?fields=**"
                }
            }
        },
        {
            "name": "NET-3.2",
            "uid": "4E455441:50502020:30303030:30303030:6D457252:38465663:2D5A5635:00000000:00000000:00000000",
            "serial_number": "00000000mErR8FVc-ZV5",
            "model": "PHA-DISK",
            "vendor": "NETAPP",
            "firmware_version": "0001",
            "usable_size": 71866187776,
            "type": "ssd",
            "effective_type": "ssd",
            "class": "solid_state",
            "container_type": "aggregate",
            "pool": "pool0",
            "state": "present",
            "node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "home_node": {
                "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                "name": "ArunS_2node-02",
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                    }
                }
            },
            "aggregates": [
                {
                    "uuid": "42f9b1a2-96f6-4572-b98a-f06d229c882d",
                    "name": "aggr0_ArunS_2node_02",
                    "_links": {
                        "self": {
                            "href": "/api/storage/aggregates/42f9b1a2-96f6-4572-b98a-f06d229c882d"
                        }
                    }
                }
            ],
            "local": True,
            "paths": [
                {
                    "initiator": "0b",
                    "port_name": "A",
                    "port_type": "sas",
                    "wwnn": "5391aabb0e000000",
                    "wwpn": "530191aabb0e0000",
                    "node": {
                        "name": "ArunS_2node-02",
                        "uuid": "b2c71008-63cf-11ed-bfb4-000c297a9d59",
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/b2c71008-63cf-11ed-bfb4-000c297a9d59"
                            }
                        }
                    }
                }
            ],
            "self_encrypting": False,
            "fips_certified": False,
            "bytes_per_sector": 512,
            "sector_count": 142606328,
            "right_size_sector_count": 142593536,
            "physical_size": 73014439936,
            "stats": {
                "average_latency": 16,
                "throughput": 5302272,
                "iops_total": 190,
                "path_error_count": 0,
                "power_on_hours": 0
            },
            "_links": {
                "self": {
                    "href": "/api/storage/disks/NET-3.2?fields=**"
                }
            }
        }
    ],
    "num_records": 10,
    "_links": {
        "self": {
            "href": "/api/storage/disks/?fields=**"
        }
    }
}

def collect_info():
    storage_disk = []
    for disk in data.get('records', []):
        storage_disk_dict = {
                'disk-inventory-info': {},
                'disk-metrocluster-info': {},
                'disk-name': '',
                'disk-ownership-info': {},
                'disk-paths': {},
                'disk-raid-info': {},
                'disk-stats-info': {},
                'disk-uid': '',
                'max-records': 0
                }

        # disk-inventory-info
        storage_disk_dict['disk-inventory-info']['capacity-sectors'] = disk.get('sector_count')
        storage_disk_dict['disk-inventory-info']['physical-size'] = disk.get('physical_size')
        storage_disk_dict['disk-inventory-info']['disk-class'] = disk.get('class')
        storage_disk_dict['disk-inventory-info']['disk-cluster-name'] = disk.get('name')
        storage_disk_dict['disk-inventory-info']['disk-type'] = disk.get('type')
        storage_disk_dict['disk-inventory-info']['disk-uid'] = disk.get('uid')
        storage_disk_dict['disk-inventory-info']['firmware-revision'] = disk.get('firmware_version')
        storage_disk_dict['disk-inventory-info']['is-shared'] = disk.get('container_type')
        storage_disk_dict['disk-inventory-info']['model'] = disk.get('model')
        storage_disk_dict['disk-inventory-info']['serial-number'] = disk.get('serial_number')
        storage_disk_dict['disk-inventory-info']['storage-sed-info'] = {
                'is-fips-sed': disk.get('fips_certified'), 
                'is-sed': disk.get('self_encrypting')
                } 
        storage_disk_dict['disk-inventory-info']['vendor'] = disk.get('vendor')

        storage_disk_dict['disk-inventory-info']['bytes-per-sector'] = disk.get('bytes_per_sector')
        storage_disk_dict['disk-inventory-info']['disk-effective-type'] = disk.get('effective-type')
        storage_disk_dict['disk-inventory-info']['drawer'] = disk.get('drawer', {}).get('id')
        storage_disk_dict['disk-inventory-info']['drawer-slot'] = disk.get('drawer', {}).get('slot')
        storage_disk_dict['disk-inventory-info']['rpm'] = disk.get('rpm')
        storage_disk_dict['disk-inventory-info']['shelf-bay'] = disk.get('bay')
        storage_disk_dict['disk-inventory-info']['shelf-uid'] = disk.get('shelf', {}).get('uid')
        storage_disk_dict['disk-inventory-info']['storage-sed-info'] = {
                'data-key-id': disk.get('key_id', {}).get('id'),
                'fips-key-id': disk.get('key_id', {}).get('fips'),
                'is-fips-sed': str(disk.get('fips_certified')).lower(),
                'is-sed': str(disk.get('self_encrypting')).lower(),
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
        storage_disk_dict['disk-raid-info']['used-blocks'] = disk.get('usable_size')
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
        storage_disk_dict['disk-stats-info']['path-error-count'] = disk.get('stats', {}).get('path_error_count')
        storage_disk_dict['disk-stats-info']['power-on-time-interval'] = disk.get('stats', {}).get('power_on_hours')

        # disk-uid
        storage_disk_dict['disk-uid'] = disk.get('uid')

        storage_disk.append(storage_disk_dict)
    print(storage_disk)

collect_info()
