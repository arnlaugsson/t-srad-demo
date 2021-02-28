class Account:
    numberOfAccounts = 0
    
    def __init__(self):
        Account.numberOfAccounts += 1
        self.number = Account.numberOfAccounts
    
    @classmethod
    def reset(cls):
        Account.numberOfAccounts = 0
