import csv

fp = open("users.csv", "r")
csv_reader = csv.reader(fp)
users = list(csv_reader)
fp.close()

for user in users[1:]:
    print(user[1])