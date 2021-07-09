class BankAccount:
    def __init__(self, account_type, balance):
        self.type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ${amount}. Your new balance is ${self.balance} ({self.type} account)")
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"You withdrawed ${amount}, Your new balance is ${self.balance} ({self.type} account)")
        return self.balance

BBVAsavings = BankAccount("savings", 500)
BBVAcheckings = BankAccount("checking", 0)

BBVAsavings.withdraw(300)
BBVAcheckings.deposit(300)
