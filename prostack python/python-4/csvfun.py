import pandas as pd
def extract_json(file_name):
    data = pd.read_json(file_name)
    return data
employees = extract_json("employee.json")
print(employees)