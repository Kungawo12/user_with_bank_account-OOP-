from bank_account import BankAccount
# Create a User class with an __init__ method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def open_new_account(self, int_rate=0.02, balance=0, account_name= "checking"):
    #make a bank account instance
        new_account = BankAccount(int_rate, balance)
        print("**************", new_account.balance)
    #add instance to the accounts dictionary
        self.accounts[account_name]= new_account
        return self
# Add a make_deposit method to the User class that calls on its bank account's instance methods.
    def make_deposit(self, amount, account_name):
        self.accounts[account_name].deposit(amount)
        return self
        # your code here
# Add a make_withdrawal method to the User class that calls on its bank account's instance methods.
    def make_withdraw(self, amount, account_name):
        self.accounts[account_name].withdraw(amount)
        return self
# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self,account_name):
        print(self.name)
        self.accounts[account_name].display_account_info()
        return self
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
# def transfer_money(self, amount, other_user):
    def transfer_money(self, from_account, to_account, other_person, amount):
        self.accounts[from_account].withdraw(amount)
        other_person.accounts[to_account].deposit(amount)
        return self
    # #Test
# user1 = User("Tenzin", "te@gmail.com")
# user1.make_deposit(100).make_deposit(250).display_user_balance()

# user2 = User("Kim", "Kim@gmail.com")
# user2.make_deposit(2000).display_user_balance().make_withdraw(450).display_user_balance()

jampa = User("Jampa Woser","janlal@gmail.com")
jampa.open_new_account(0.05, 0)
jampa.make_deposit(100,"checking").display_user_balance("checking")
jampa.open_new_account(0,500, "savings")

sam = User("Sam Nora","nora@gmam.com")
sam.open_new_account(0.045, 300, "savings").display_user_balance("savings")
jampa.transfer_money("checking", "savings", sam, 100).display_user_balance("checking")