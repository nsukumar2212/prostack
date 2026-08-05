import csv
fp = open('data.csv', 'r')
csv_reader = csv.reader(fp)
employees = list(csv_reader)
fp.close()
print(employees)