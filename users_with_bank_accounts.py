class User:

    def __init__(self, account_type, name = "Unassigned", balance = 0, interest_rate = 1.04):
        self.name = name
        self.account = BankAccount(balance, interest_rate)
        self.account_type = account_type

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"You have deposited ${amount}")
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"You have withdrawn ${amount}")
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def yield_user_interest(self):
        self.account.yield_of_interest()
        print("You have accrued interest")
        return self

class BankAccount:

    # CLS METHOD
    accounts = []
    # CLS METHOD

    def __init__(self, balance = 0, interest_rate = 1.04):
        self.balance = balance
        self.interest_rate = interest_rate
        # CLS METHOD
        BankAccount.accounts.append(self)
        # CLS METHOD

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Your balance is up to ${self.balance}!')
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
            print(f'Your balance is down to ${self.balance}.')
        else:
            self.balance = self.balance - 5
            print('Insufficient Funds')
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.interest_rate}%")
        return self

    def yield_of_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (self.interest_rate)
        else:
            print("Your negative account is ineligible to accrue interest")
        return self

# CLS METHOD
    @classmethod
    def display_all(cls):
        sum = 0
        for account in cls.accounts:
            sum = sum + account.balance
        return sum
# CLS METHOD
# CLS METHOD
    @classmethod
    def all_balances(cls):
        for account in cls.accounts:
            account.display_account_info()
        return cls
# CLS METHOD

brendan = User("Brendan Cordova")
tori = User("Tori Cordova")

brendan.make_deposit(50).make_withdrawal(25).yield_user_interest().display_user_balance()
tori.display_user_balance()

# BankAccount.all_balances()
# BankAccount.display_all()





# --------PART 1---------
# checking = BankAccount(5200, 1.045)
# savings = BankAccount(105000, 1.02)

# print(checking.balance, checking.interest_rate)
# print(savings.balance, savings.interest_rate)


# checking.deposit(675).deposit(1450).deposit(375).withdraw(1690).yield_of_interest().display_account_info()
# savings.deposit(5770).deposit(1525).withdraw(70000).withdraw(10000).withdraw(2500).withdraw(2250).yield_of_interest().display_account_info()

# CLS METHOD -- this will print all values. 
# BankAccount.display_all()