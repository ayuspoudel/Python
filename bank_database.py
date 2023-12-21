"""Create a class called BankAccount with attributes like account number, 
account holder name, and balance. Implement methods for deposit, withdrawal, 
and checking the account balance. Also, implement a method to display the account details."""

class BankAccount:
    def __init__(self,acc_no,acc_name,acc_balance,password):
        self.__acc_no=acc_no
        self.acc_name=acc_name
        self.__acc_balance = acc_balance
        self.password = password
    def deposit(self, amount):
        self.__acc_balance += amount
    def withdraw(self, amount):
        if self.__acc_balance>=amount:
            self.__acc_balance-=amount
        else:
            print("You Broke")
    def show_balance(self, ent_password):
        if ent_password == self.password:

            print(f"Standard Chartered Bank Pvt Ltd\nAccount Holder name = {self.acc_name}\nAccount Number = {self.__acc_no}\nAccount Balance = {self.__acc_balance}")
        else:
            print("Invalid Password")

acc_database = [
    BankAccount("1234567890", "Norma Tshering", 1000.0, "pass123"),
    BankAccount("2345678901", "Cheyenne Van Helden", 9.34, "taken"),
    BankAccount("3456789012", "Alice Johnson", 500.0, "qwerty"),
    BankAccount("4567890123", "Bob Williams", 1500.0, "secret"),
    BankAccount("5678901234", "Sarah Davis", 2000.0, "password1"),
    BankAccount("6789012345", "Michael Brown", 3000.0, "letmein"),
    BankAccount("7890123456", "Emily Wilson", 1200.0, "test123"),
    BankAccount("8901234567", "David Lee", 1800.0, "abc123"),
    BankAccount("9012345678", "Jessica Taylor", 900.0, "hello123"),
    BankAccount("0123456789", "Kevin Thompson", 2200.0, "password123"),
]

uacc_no = input("Enter your account number = ")
user_acc = None
for acc in acc_database:
    if uacc_no == acc._BankAccount__acc_no:
        user_acc = acc
        break

if user_acc:
    ent_password = input(f"Hello {user_acc.acc_name}\n Please Enter your password = ")
    user_acc.show_balance(ent_password)
    transaction_type = input(f"Hello {user_acc.acc_name}\nPlease Enter 'D' to deposit or 'W' to withdraw = ")
    if transaction_type.upper() == "D":
        dep = float(input("Enter the amount to Deposit = "))
        user_acc.deposit(dep)
    elif transaction_type.upper() == "W":
        wit = float(input("Enter the amount to Withdraw = "))
        user_acc.withdraw(wit)
    else:
        print("Invalid Transaction Type")
    user_acc.show_balance(ent_password)

else:
    print("Invalid Account Number")
          
    

