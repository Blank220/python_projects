from normal_bank import *

mark = BankAccount(5000, "Mark")
zeref = BankAccount(3000, "zeref")

mark.getBalance()
zeref.getBalance()

zeref.deposit(300)

mark.withdraw(2500)

mark.transfer(1000,zeref)

grace = InterestRewardsAcct(10000,'Grace')
grace.getBalance()
grace.deposit(200)
grace.transfer(500,mark )

blaze = SavingsAcct(25000,"blaze")
blaze.getBalance()
blaze.deposit(500)
blaze.transfer(10000,zeref)