class BankAccount:
    def __init__(self, account_type, balance):
        self.type = account_type
        self.balance = balance
        self.overdraft_fees = 0
        self.default_interest = 0.02

    def deposit(self, amount):
        if (amount <= 0):
            print('Invalid Transaction') # this could be also return false!
        else:

            self.balance += amount
            print(
                f"You deposited ${amount}. Your new balance is ${self.balance} ({self.type} account)")
            return self.balance

    def withdraw(self, amount):
        if (amount <= 0):
            print('Invalid Transaction') # this could be also return false!
        elif(self.balance - amount <= -100):
            print(f"Transaction Declined")
        elif(self.balance - amount < 0):
            amount += 20
            self.balance -= amount
            print(
                f"This transaction was allowed (${amount-20}), but an overdraft fee of $20 was charged (${amount} total). Your current balance {self.balance}")
        else:
            self.balance -= amount
            print(
                f"You withdrew ${amount}, Your new balance is ${self.balance} ({self.type} account)")
            return self.balance
    def accumulate_interest(self):
        self.balance = (self.balance * self.default_interest) + self.balance
        print(f'{self.balance}')
        
    def full_balance(self):
        return self.balance
    
    def __add__(self, other_acc1):
        return self.balance + other_acc1.balance
    
    def __sub__(self, other_acc1):
        return self.balance - other_acc1.balance
    
    def __mul__(self, other_acc1):
        return self.balance * other_acc1.balance
    
    def __truediv__(self, other_acc1):
        return self.balance / other_acc1.balance
    

BBVAsavings = BankAccount("savings", 500)
# BBVAcheckings = BankAccount("checking", 0)
BBVAsavings.accumulate_interest()

# BBVAsavings.withdraw(500)  # Balance 0
# BBVAsavings.withdraw(20)  # 520+20 Balance -40
# BBVAsavings.withdraw(40)  # 40+40+20 Balance -100
# BBVAsavings.withdraw(20)  # Transaction Declined
# BBVAcheckings.deposit(300)

class ChildrensAccount(BankAccount):
    
    def __init__(self, account_type, balance):
        super().__init__(account_type, balance)
        self.default_interest = 0
    def accumulate_interest(self):
        self.balance += 10
        print(f"An extra $10 have been added to your account! Now your total is ${self.balance}")


# fidelity = ChildrensAccount("savings", 34)

# fidelity.withdraw(17)
# fidelity.accumulate_interest()


class OverdraftAccount(BankAccount):
    
    def __init__(self, account_type, balance):
        super().__init__(account_type, balance)
        self.overdraft_penalty = 40
    
    def withdraw(self, amount):
        if (amount > self.balance):
            self.balance -= self.overdraft_penalty
            print(f"You have been penalized because the withdraw amount exceeded the account balance. A total of ${self.overdraft_penalty} has been charged, your new total is ${self.balance}. Lol we love this.")
    def accumulate_interest(self):
        if (self.balance < 0):
            self.default_interest == 0
            print(f"Unfortunately, because your account balance is negative your interested rate has been reduced to zero")

        

noBuenoBank = OverdraftAccount("checking", 12)
# noBuenoBank = OverdraftAccount("saving", 12)
# noBuenoBank.withdraw(17)
# noBuenoBank.accumulate_interest()


print(noBuenoBank + BBVAsavings)
print(noBuenoBank / BBVAsavings)
print(noBuenoBank - BBVAsavings)
print(noBuenoBank * BBVAsavings)
