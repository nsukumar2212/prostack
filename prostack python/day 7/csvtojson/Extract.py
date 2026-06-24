import csv
fp1=open('user.csv','r')
csv_reader_obj=csv.reader(fp1)
users=list(csv_reader_obj)
print(len(users))

#transform

employee_data=[]
for user in users:
    employee_data.append({"id":user[0],
                          "name":user[1],
                          "gender":user[2]
                          
                            })