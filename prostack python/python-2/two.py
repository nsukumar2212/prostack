import json
fp = open("emp.json", "r")
employees = json.load(fp)
mcount = 0
fcount = 0
i = 0
while i < len(employees):
    if employees[i]["gender"] == "Male":
        mcount = mcount + 1
    elif employees[i]["gender"] == "Female":
        fcount = fcount + 1
    i = i + 1
print("No of Male:", mcount)
print("No of Female:", fcount)
fp.close()