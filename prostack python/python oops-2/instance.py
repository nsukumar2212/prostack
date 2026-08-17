class Account:
    min_bal=500
    bank_name="SBI"

    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount

    def deposit(self):
        print("Amount deposited successfully")

a1=Account(1,"rg",1000)
a2=Account(2,"sg",2000)
a3=Account(3,"pg",3000)
a1.deposit()
a2.deposit()
a3.deposit()

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(Account.__dict__)
