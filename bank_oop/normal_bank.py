class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created. \nBalance: {self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}': Balance: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f'Sorry,  account {self.name} only has a balance of {self.balance:.2f}')

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f'\nWithdraw Complete')
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw Interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print("\n*********\n\nBeginning Transfer.....🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer Complete! ✅')
        except BalanceException as error:
            print(f"Transfer Interrupted. ❌ {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit Complete!")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw Complete!")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")





        
        