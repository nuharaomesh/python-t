class BankAccount:
    
    balance = 0
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
    
    def deposit(self, amount):
        if amount < 0:
            return
        self.balance += amount
        print(self.balance)
    
    def withdraw(self, amount):
        if self.balance < amount and amount < 0:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(self.balance)
    
    def check_balance(self):
        print("Your balance is: ", self.balance)
        
user_account = BankAccount("Omesh")
user_account.deposit(40)
user_account.withdraw(10)
user_account.check_balance()
