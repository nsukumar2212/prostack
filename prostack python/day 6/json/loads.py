import json
emp_json_str='''
{"eid": 101, "ename": "RG", "esal": 45000, "avail": true, "discount": null}
'''

json_loads=json.loads(emp_json_str)
print(json_loads)