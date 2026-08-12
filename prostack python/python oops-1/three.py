class Account:

    def open_account(self):
        print("Account opened successfully.")

    def deposit(self):
        print("Deposited sucessfully.")

    def withdraw(self):
        print("Withdrawn successfully.")

    def get_balance(self):
        print("Balance retrieved successfully.")

    def close_account(self):
        print("Account closed successfully.")


a1 = Account()

a1.open_account()
a1.deposit()
a1.withdraw()
a1.get_balance()
a1.close_account()