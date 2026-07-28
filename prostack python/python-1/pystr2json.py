import json

emp_list = [{'esal': 101, 'avail': True}, {'esal': 102, 'avail': False}]

print(type(emp_list))

emp_json_str = json.dumps(emp_list)
print(type(emp_json_str))
print(emp_json_str)