class Account:

    min_bal = 500

    def __init__(self, acc_id, name, amount):
        self.acc_id = acc_id
        self.name = name
        self.amount = amount

    def deposit_amount(self, amount):
        self.amount = self.amount + amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if self.amount - amount >= Account.min_bal:
            self.amount = self.amount - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def get_bal(self):
        return self.amount

    @classmethod
    def update_minbal(cls, amount):
        cls.min_bal = amount

    @staticmethod
    def cal_interest(p, ri):
        return p * ri / 100


# Create objects

a1 = Account(101, "Sunny", 5000)
a2 = Account(102, "RG", 5000)


print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)


# Deposit

a1.deposit_amount(2000)

print(a1.__dict__)


# Withdraw

a1.withdraw(1000)

print(a1.__dict__)


# Update static/class method

Account.update_minbal(1000)

print(Account.min_bal)


# Calculate interest

interest = Account.cal_interest(5000, 5)

print("Interest:", interest)

Account.update_minbal(600)
print(a1.get_bal())
print(a2.get_bal())