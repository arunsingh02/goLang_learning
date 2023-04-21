# Test

data={
		1:{"a":[1,2,3,5,6,7]},
		2:{"b":[11,21,23,5,6,7]},
		3:{"c":[111,12,13,514,6,7]}
     }

def testing(disk_id, pool_name=""):
	disk=None
	if pool_name.strip():
		disk = data.get(disk_id, {}).get(pool_name, [])
	elif not disk:
		disk = data.get(disk_id, {})

	print(disk)

testing(1)                   # {'a': [1, 2, 3, 5, 6, 7]}
testing(1, " ")              # {'a': [1, 2, 3, 5, 6, 7]}
testing(1, "None")           # []
testing(1, "a")              # [1, 2, 3, 5, 6, 7]
testing(1, 'None')           # []
testing(3, "wrong")          # []
testing(2)                   # {'b': [11, 21, 23, 5, 6, 7]}
#testing(2, None) 
"""
Traceback (most recent call last):
  File "test.py", line 25, in <module>
    testing(2, None)                   # {'b': [11, 21, 23, 5, 6, 7]}
  File "test.py", line 11, in testing
    if pool_name.strip():
AttributeError: 'NoneType' object has no attribute 'strip'
"""


a = '9.12.1'

def convert_to_number(version_string):
    """Converting version from string to integer"""
    #version_list = version_string.split('.')
    #version = ''
    #for ver_str in version_list:
    #    version += ver_str


    l = [int(x, 10) for x in version_string.split('.')]
    l.reverse()
    print(l)
    version = sum(x * (100 ** i) for i, x in enumerate(l))
    return version


print(convert_to_number(a))
