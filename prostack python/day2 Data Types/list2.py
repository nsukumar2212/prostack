'''
--group of elemnet/values/objects/items as one entity
--allowed duplicats
--allowed heterogenous elements
'''
a=[]   #empty list
print(a)
print(type(a))


#create 

a=[]
eids=[101,102,103,104]
numbers=[10,10,20,20,30,40]
b=[10,20.2,"y","RG","true",[],{}]

#read

print(a)
print(eids)

#index  -4        -3      -2       -1
enames=["Rahul","sonia","Priya","Modi"]
#index   0         1         2      3
#read
print(enames)
#how to read list elements- using index
print(enames[0])
print(enames[1])
print(enames[2])
print(enames[3])
print(enames[-1])
print(enames[-2])
print(enames[-3])
print(enames[-4])

#update

enames[0]="Rahul Ji"
print(enames)
