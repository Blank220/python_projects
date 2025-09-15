class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    

    def deposit(self):
        depo = int(input('Depo: '))
        self.balance += depo
        return f"Remaining bal. : {self.balance}"

    def withdraw(self):
        withdraw = int(input('Withdraw: '))
        self.balance -= withdraw
        return f"Remaining bal. : {self.balance}"

mark = Bank('mark')
print(mark.deposit())
print(mark.withdraw())

    



    
    
