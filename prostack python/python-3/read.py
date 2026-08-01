import json
# Extract 
fp1 = open("users.json", "r")
users = json.load(fp1)
print(type(users))
print(len(users))
fp1.close()

# Transform
male_users = []
female_users = []

for user in users:
    if user["gender"] == "Male":
        male_users.append(user)
    elif user["gender"] == "Female":
        female_users.append(user)
len(male_users)
len(female_users)

# Load
fp2 = open("male.json", "w")
json.dump(male_users, fp2)
fp2.close()

fp3 = open("female.json", "w")
json.dump(female_users, fp3)
fp3.close()

print("ETL Process Completed Successfully")
