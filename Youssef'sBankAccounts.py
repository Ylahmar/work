class BankAccounts:
    def __init__(self, first_name, last_name, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = []        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount
    def withdrawal(self, amount, limit=600):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                   '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)
    def fee_calculation(self):
        if self.balance <= 1000:
           self.balance -= 10
           print("$10 was taken out of your account because your balancae is under $1000")
    def Interest(self):
        self.balance += self.balance *0.03
        return "3% of intrest was added to your balance"
           
         
        
            
            
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_initial_deposit(self):
        return self.balance
    def get_balance(self):
        return self.balance
    def get_Fee(self):
        return self.Fee
    def RecentTransactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()
Account = BankAccounts('Youssef', 'Lahmar', 1000)
print('first name =', Account.get_first_name())
print('last name =', Account.get_last_name())
print('Initial Deposit =', Account.get_initial_deposit())
print('deposit =', Account.deposit(20))
print('recent transaction is:', Account.RecentTransactions())
print('account balance =', Account.get_balance())
print('withdrawal =', Account.withdrawal(50))
print('recent transaction is =', Account.RecentTransactions())
print('account balance =', Account.get_balance())
print('withdrawal =', Account.withdrawal(900))
print('recent transaction is =', Account.RecentTransactions())
print('account balance =', Account.get_balance())
print('Fee Calculations =', Account.fee_calculation())
print('account balance =', Account.get_balance())
print('withdrawal =', Account.withdrawal(20))
print('account balance =', Account.get_balance())
print(' Interest =', Account.Interest())
print('account balance =', Account.get_balance())

