extract()     # Read data
transform()   # Clean or modify data
load()        # Save data





def extract():
    fp = open("employee.txt", "r")
    data = fp.read()
    fp.close()
    return data
result = extract()
print(result)