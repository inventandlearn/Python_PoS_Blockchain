from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

# The Blockchain object acts as a linked list that connects every new block created to previous blocks.
class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()

# This method adds each block created to a linked list of previously created blocks.
    def addBlock(self, block):
        self.blocks.append(block)

# This method returns a dictionary of all the blocks that have been added to the Blockchain object.
    def toJSON(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJSON())
        data['blocks'] = jsonBlocks
        return data

# This method validates whether or not a block is subsequent to the previous block by one unit.
    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

# This method validates that the new block being added to the blockchain has the last block's hash.
    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if latestBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False

# This method iterates through a list of transactions and checks if the sender has a sufficient balance to cover the respective transaction.
    def getCoveredTransactionSet(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print("These transactions cannot be completed. Balances of senders are insufficient!")
        return coveredTransactions

# This method check is the sender has a sufficient balance to cover a TRANSFER type transaction.
    def transactionCovered(self, transaction):
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False