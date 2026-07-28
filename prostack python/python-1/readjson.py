import json

fp1=open('emp.json', 'r')
emp_list = json.load(fp1)
print(len(emp_list))

for emp in emp_list:
    if emp['gender'] == 'Female':
        print(emp['ename'])  