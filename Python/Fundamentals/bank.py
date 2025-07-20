class Bank:
    def __init__(self,balance=0) -> None:
        self.__balance = balance
    
    def deposit(self, data):
        self.__balance += data

    def withdraw(self, data):
        if self.__balance >= data:
            self.__balance -= data
        else:
            raise Exception("Insufficient Balance. Try again with lower amount.")
    
    def checkBalance(self):
        return(self.__balance)

account = Bank()
account.deposit(100)
print("Balance: ",account.checkBalance())
account.deposit(100)
print("Balance: ",account.checkBalance())

try:
    account.withdraw(2000)
except Exception as e:
    print(str(e))

try:
    account.withdraw(20)
except Exception as e:
    print(str(e))

print("Balance: ", account.checkBalance())