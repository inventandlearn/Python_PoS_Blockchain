
# This Transaction Pool object forms the block size on the blockchain with x amount of transactions.
class TransactionPool():

    def __init__(self):
        self.transactions = []

# This method adds a validated transaction to a list of transactions to form the transaction pool.
    def addTransaction(self, transaction):
        self.transactions.append(transaction)

# This method ensures that a transaction isn't added to the pool twice by checking for it's existence already.
    def transactionExists(self, transaction):
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
        return False

# This method removes transactions that have already been added to a block, so that a fresh list of transactions can be added to the pool.
    def removeFromPool(self, transactions):
        newPoolTransactions = []
        for poolTransaction in self.transactions:
            insert = True
            for transaction in transactions:
                if poolTransaction.equals(transaction):
                    insert = False
            if insert == True:
                newPoolTransactions.append(poolTransaction)
        self.transactions = newPoolTransactions

# This method checks if the TransactionPool object has stored x amount of transactions.
# If the x amount of transactions has been reached the forger selection process will initiate.
    def forgerRequired(self):
        if len(self.transactions) >= 3:
            return True
        else:
            return False

