# An example of a class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


# Creating instances of BankAccount class
harriet_account = BankAccount("Harriet Smith", 10)
emma_account = BankAccount("Emma Woodhouse", 100000)

# Depositing money into accounts
harriet_account.deposit(25)
emma_account.deposit(100)

print("Harriet's balance:", harriet_account.balance)  # 35
print("Emma's balance:", emma_account.balance)  # 100100
