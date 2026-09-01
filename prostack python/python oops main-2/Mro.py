class parent1:
    def m1(self):
        print("parent1-m1()method")
    def m2(self):
        print("parent1-m2()method")

class parent2:
    def m1(self):
            print("parent2-m1()method")
    def m2(self):
        print("parent2-m2()method")

class child(parent2, parent1):
    def m3(self):
        print("child class -m3() method")

c1=child()
c1.m1()
c1.m2()
c1.m3()