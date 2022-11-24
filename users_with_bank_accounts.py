class User:

    def __init__(self, name = "Unassigned"):
        self.name = name
        self.account = {} #BankAccount(balance, interest_rate) goes here originally, moves into create_new_account function

    def create_New_Account(self, balance = 0, interest_rate = 1.04, account_type = "checking"):
        print('we are creating an account here')
        self.account[account_type] = BankAccount(balance, interest_rate, account_type)
        return self

    def make_deposit(self, amount, account_type = "checking"):
        self.account[account_type].deposit(amount)
        print(f"You have deposited ${amount}")
        return self

    def make_withdrawal(self, amount, account_type = "checking"):
        self.account[account_type].withdraw(amount)
        print(f"You have withdrawn ${amount}")
        return self

    def display_user_balance(self):
        print(self.name)
        for user_account in self.account:
            self.account[user_account].display_account_info()
        return self

    def yield_user_interest(self):
        self.account.yield_of_interest()
        print("You have accrued interest")
        return self

    def transfer_money(self, other_user, other_user_acc_type, amount, from_account_type):
        if self.account[from_account_type].balance < amount:
            print("Insufficient funds")
            return self
        print("Transferring $" + str(amount) + " into " + other_user.name + "'s " + other_user_acc_type + " account.")
        self.account[from_account_type].balance -= amount
        other_user.account[other_user_acc_type].balance += amount

        self.display_user_balance()
        other_user.display_user_balance()

        return self

class BankAccount:

    # CLS METHOD
    accounts = []
    # CLS METHOD

    def __init__(self, balance = 0, interest_rate = 1.04, account_type = "checking"):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_type = account_type
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

tori.create_New_Account(1000)
brendan.create_New_Account(2100).make_deposit(675).make_withdrawal(1000).display_user_balance()
brendan.create_New_Account(10000, .01, "savings").transfer_money(tori, "checking", 500, "savings")
brendan.yield_user_interest()

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