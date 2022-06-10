class Account:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self,amount):
        self.amount = amount
        if self.amount<=0:
            return f"Deposit must be greater than zero"
        else:
            self.balance+=self.amount
            self.deposits.append(self.amount)
            return f"Hello {self.name} you have deposited {self.amount} and you balance is {self.balance}"

    def withdraw(self,amount):
        self.amount = amount
        self.transaction_cost = 100
        new_amount=amount+self.transaction_cost
        if amount<=0:
            return f"Withadrawals must be greater than zero"
        elif new_amount> self.balance:
            return f"Insufficient funds"
        else:
            self.balance-=new_amount
            self.withdrawals.append(self.amount)
            return f"Hello {self.name}.You have withdrawn {amount} at a transaction cost {self.transaction_cost} You new balance is{self.balance}"

    def deposits_statement(self):
        print("""  Deposit Statement  """)
        for deposit in self.deposits:
            print( f"Your deposit was {deposit}")

    def withdrawal_statement(self):
        print("""  Withdrawal Statement   """)
        for withdrawal in self.withdrawals:
            print( f"Your withdrawal was {withdrawal}")

    def curent_balance(self):
        return f"You current balance is {self.balance}"


   








