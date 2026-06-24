import json
emp={
    'eid':101,
    'ename':'RG',
    'esal':45000,
    'avail':True,
    'discount':None
}
emp_json=json.dumps(emp)
print(emp_json)