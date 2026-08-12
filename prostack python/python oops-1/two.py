class Account:

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

a1.open_account()
a1.deposit(5000)
a1.withdraw(2000)
a1.get_balance()
a1.close_account()