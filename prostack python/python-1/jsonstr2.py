import json
emp_json_str = '''
[
    {"esal":101,"avail":true},
    {"esal":102,"avail":false}
]
'''
emp_list = json.loads(emp_json_str)

print(emp_list)