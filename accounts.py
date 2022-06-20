from datetime import datetime
from time import strftime
now =datetime.now()
print(now.strftime('%d/%m/%y'))
print(now.strftime('%d'))

class Account:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.full_statement_info = []
        self.transaction_cost = 100
        self.loan_balance = 0

    def deposit(self,amount):
        self.amount = amount
        if self.amount<=0:
            return f"Deposit must be greater than zero"
        else:
            deposit_date = datetime.now()
            self.balance+=self.amount
            self.deposit_info = {"date":deposit_date.strftime('%x %X'),"amount":self.amount,"narration":"Deposit "}
            self.deposits.append(self.deposit_info)
            self.full_statement_info.append(self.deposit_info)
            return f"Hello {self.name} you have deposited {self.amount} on {deposit_date.strftime('%x %X')}.Your new balance is {self.balance}"

    def withdraw(self,amount):
        new_amount=amount+self.transaction_cost
        if amount<=0:
            return f"Withadrawals must be greater than zero"
        elif new_amount> self.balance:
            return f"Insufficient funds"
        else:
            withdrawal_date = datetime.now()
            self.withdrawal_info = {"date":withdrawal_date.strftime('%x %X'),"amount":amount,"narration":"Withdraw"}
            self.balance-=new_amount
            self.withdrawals.append(self.withdrawal_info)
            self.full_statement_info.append(self.withdrawal_info)
            return f"Hello {self.name}.You have withdrawn {amount} at a transaction cost {self.transaction_cost} on {withdrawal_date.strftime('%x %X')}.You new balance is{self.balance} "

    def deposits_statement(self):
        print("""  Deposit Statement  """)
        for deposit in self.deposits:
            print( f"Your deposit was {deposit}")

    def withdrawal_statement(self):
        print("""  Withdrawal Statement   """)
        for withdrawal in self.withdrawals:
            print( f"Your withdrawal was {withdrawal}")

    def full_statement(self):
        for a in self.full_statement_info:
            self.info_date = a["date"]
            self.info_amount = a["amount"]
            self.info_narration = a["narration"]
            print(f"{self.info_date} ------ {self.info_amount} ----- {self.info_narration}")


    def curent_balance(self):
        return f"You current balance is {self.balance}"

    def borrow_loan(self,amount):
        total = 0
        for deposit in self.deposits:
            total += deposit["amount"] 
        if len(self.deposits)>=10 and amount>=100 and self.balance==0 and amount<=(1/3*(total)):
            borrow_date = datetime.now()
            self.loan_balance+=amount
            self.loan_balance=(self.loan_balance*1/3) + self.loan_balance
            print(f"You have received a loan of {amount} on {borrow_date.strftime('%x %X')} new loan balance is {self.loan_balance}")
        elif len(self.deposits)<=10:
            print("You are currently not eligible for a loan.Keep on depositing to become eligible")  
        elif amount>(1/3*(total)):
            print(f"Failed.Your maximum loan limit is {1/3*(total)}") 
        elif amount<100:
            print("Minimum accessible loan is 100")
        else:
            print("Loan request failed.Ensure that your bank acount balance is 0.00")
        
    def loan_repayment(self,amount):
        if amount<self.loan_balance:
            self.loan_balance = self.loan_balance-amount
            print(f"You have repayed {amount}.New loan balance is {self.loan_balance}")
        elif amount==self.loan_balance:
            amount-self.loan_balance
            print(f"You have fully settled your loan balance.Loan balance is 0.00")
        else:
            excess_payment = amount - self.loan_balance
            self.balance += excess_payment
            print(f"You have fully settled your loan balance.New account balance is {self.balance}") 


    def transfer(self,name,amount):
        self.name = name
        if amount<self.balance:
            self.balance-=amount
            self.name.balance += amount 
        return f"You have transferred {amount} to {self.name} new account balance is {self.balance}"







   








