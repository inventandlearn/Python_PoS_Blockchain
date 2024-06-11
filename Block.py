import time
import copy

# The Block object is used to extract transactions from the Transaction Pool object, contain them, and subsequently link to a
# Block previously created on the blockchain or become the genesis block within the blockchain.
class Block():

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.blockCount = blockCount
        self.transactions = transactions
        self.lastHash = lastHash
        self.timestamp = time.time()
        self.forger = forger
        self.signature = ''

# This static method generates a genesis block. The genesis block is the first block of the blockchain. It's timestamp is set to 0
# so that it can be easily identified as the genesis block within the Blockchain.
    @staticmethod
    def genesis():
        genesisBlock = Block([], 'genesisHash', 'genesis', 0)
        genesisBlock.timestamp = 0
        return genesisBlock


# This method returns attributes of the Block object in a dictionary format.
    def toJSON(self):
        data = {}
        data['blockCount'] = self.blockCount
        data['lastHash'] = self.lastHash
        data['signature'] = self.signature
        data['forger'] = self.forger
        data['timestamp'] = self.timestamp
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJSON())
        data['transactions'] = jsonTransactions
        return data

# Method that keeps signature consistent for each Block. In other words the signature of the last Block doesn't carry over to the following Block.
# After each Block object is added to the chain with a unique signature the next Block instantiated has it's signature reset to an empty string.
# Once the block has been successfully added to the chain, the signature created will fill the empty string.
    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJSON())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

# This method is accessed by the Wallet object so that a signature can be generated separately and assigned to the Block object.
    def sign(self, signature):
        self.signature = signature

