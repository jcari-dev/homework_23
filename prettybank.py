class BankAccount:
    def __init__(self, account_type, balance):
        self.type = account_type
        self.balance = balance
        self.overdraft_fees = 0

    def deposit(self, amount):
        self.balance += amount
        print(
            f"You deposited ${amount}. Your new balance is ${self.balance} ({self.type} account)")
        return self.balance

    def withdraw(self, amount):
        if(self.balance - amount <= -100):
            print(f"Transaction Declined")
        elif(self.balance - amount < 0):
            amount += 20
            self.balance -= amount
            print(
                f"This transaction was allowed (${amount-20}), but an overdraft fee of $20 was charged (${amount} total). Your current balance {self.balance}")
        else:
            self.balance -= amount
            print(
                f"You withdrawed ${amount}, Your new balance is ${self.balance} ({self.type} account)")
            return self.balance


BBVAsavings = BankAccount("savings", 500)
# BBVAcheckings = BankAccount("checking", 0)

BBVAsavings.withdraw(500)  # Balance 0
BBVAsavings.withdraw(20)  # 520+20 Balance -40
BBVAsavings.withdraw(40)  # 40+40+20 Balance -100
BBVAsavings.withdraw(20)  # Transaction Declined
# BBVAcheckings.deposit(300)
