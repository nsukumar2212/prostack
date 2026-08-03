import pandas as pd
data = pd.read_json("employee.json")
data.to_csv("employee.csv", index=False)
print("JSON converted to CSV successfully.")