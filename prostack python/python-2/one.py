import json

fp=open('emp.json', 'r')
employees=json.load(fp)

mcount = 0
fcount = 0
for emp in employees:
    if emp['gender']=='Male':
        mcount = mcount + 1
    elif emp['gender']=='Female':
        fcount = fcount + 1

print("No of Male:", mcount)
print("No of Female:", fcount)