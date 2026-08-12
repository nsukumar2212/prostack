class Account:
    ''' Class Created By Sunny '''
    def open_account(self):
        print("Account opened successfully.")

    def deposit(self, amount):
        print("Deposited:", amount)

    def withdraw(self, amount):
        print("Withdrawn:", amount)

    def get_balance(self):
        print("Balance retrieved successfully.")

    def close_account(self):
        print("Account closed successfully.")


a1 = Account()

print(a1.__dict__)
print(Account.__dict__)