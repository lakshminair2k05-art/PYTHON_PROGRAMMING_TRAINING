
class BankAccount:
    # constructor
    def __init__(self, balance, name):
        self.name = name
        self.__balance = balance

    # getter
    def get_balance(self):
        return self.__balance

    # setter
    def set_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Balance Amount")


# Main
account = BankAccount(500, "LAKSHMI")

print(account.get_balance())   # current balance
account.set_balance(500)       # add amount
print("Total after adding:", account.get_balance())