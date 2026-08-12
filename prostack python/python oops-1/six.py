class Account:
    '''Account Created By sunny'''
    min_bal=500         # static variable

    def deposit(self, amount):      #instance method
        print("Amount deposited")

a1 = Account()

a2 = Account()

print(a1.__dict__)  # prints the instance variables of a1
print(a2.__dict__)  # prints the instance variables of a2
print(Account.__dict__)  # prints the class variables of Account

    