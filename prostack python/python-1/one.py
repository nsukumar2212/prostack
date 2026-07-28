f1 = open("user.txt", "r")
f2 = open("emp.txt", "w")

data = f1.read()
f2.write(data)
