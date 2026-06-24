
def add(a,*b):
    print(a)
    print(b)

add(10,20)     #10 (20,)
add(10,20,30,40)   #10 (20, 30, 40)
add(10)       #10 ()