male_users = []
for user in users:
    if user[2] == "male":
        male_users.append((user[0], user[1]))
print(len(male_users))



