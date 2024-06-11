# The Account Model object stores the state of each wallet's balance and it's corresponding publicKeyString that is on the Blockchain.
class AccountModel():

    def __init__(self):
        self.accounts = []
        self.balances = {}

# This method initializes newly created accounts onto the blockchain with a beginning balance of 0.
    def addAccount(self, publicKeyString):
        if not publicKeyString in self.accounts:
            self.accounts.append(publicKeyString)
            self.balances[publicKeyString] = 0

# This method returns the balance of a wallet and it's corresponding publicKeyString.
    def getBalance(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        return self.balances[publicKeyString]

# This method updates the balance of a given wallet and it's corresponding publicKeyString after it has transacted on the blockchain.
    def updateBalance(self, publicKeyString, amount):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        self.balances[publicKeyString] += amount