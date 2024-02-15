import time

# The Block object is used to extract transactions from the Transaction Pool object, contain them, and subsequently link to a
# Block previously created on the blockchain or become the genesis block within the blockchain.
class Block():

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

# This method returns attributes of the Block object in a dictionary format.
    def toJSON(self):
        data = {}
        data['lastHash'] = self.lastHash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] = self.timestamp
        data['signature'] = self.signature
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJSON())
        data['transactions'] = jsonTransactions
        return data
