
class parent:
    def m1(self):
        print("parent class m1 - Instance method")

class child:
    def m2(self):
        print("parent class m2 - Instance method")

    def m3(self):
            print("Child Class m3 - instance method") 


c1=Child()

c1.m1()
c1.m2()
c1.m3()