def smart_div(func):
    def inner(a,b):
        if b==0:
            print("can't divided by 0")
        else:
            return func(a,b)

    return inner

@smart_div
def cal_div(a,b):
    print(a/b)

cal_div(10,0)
print("GM")