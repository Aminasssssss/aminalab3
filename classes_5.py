#5. Create a bank account class that has attributes `owner`, `balance` 
# and two methods `deposit` and `withdraw`. Withdrawals may not exceed the 
# available balance. Instantiate your class, make several deposits and withdrawals, and test
#  to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance):
        self.owner = owner  
        self.balance = balance  


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  
            print("you deposited", amount, "     current balance:", self.balance)
        else:
            print("amount must be positive!")



    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough, your balance is only: ", self.balance)
        elif amount <= 0:
            print("amount must be positive!")
        else:
            self.balance -= amount  # Decrease the balance
            print("withdrew is:", amount, "      current balance:", self.balance)



    def display(self):
        print("Owner's name:", self.owner)
        print("Current Balance:", self.balance)




my_account = Account("Amina", 1000)
my_account.display()
my_account.deposit(500) 
my_account.withdraw(300)  
my_account.display()