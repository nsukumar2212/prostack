import json

# Extract Function
def extract():
    fp1= open("users.json", "r")
    users = json.load(fp1)
    fp1.close()
    return users


# Transform Function
def transform(users):
    male_users = []
    female_users = []

    for user in users:
        if user["gender"] == "Male":
            male_users.append(user)
        elif user["gender"] == "Female":
            female_users.append(user)

    return male_users, female_users


# Load Function
def load(male_users, female_users):
    fp2 = open("male.json", "w")
    json.dump(male_users, fp2)
    fp2.close()

    fp3 = open("female.json", "w")
    json.dump(female_users, fp3)
    fp3.close()

