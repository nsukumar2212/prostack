class Grandparent:

    def m1(self):
        print("Grandparent m1")


class Parent(Grandparent):

    def m2(self):
        print("Parent m2")


class Child(Parent):

    def m3(self):
        print("Child m3")


c1 = Child()

c1.m1()
c1.m2()
c1.m3()