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
        self.executeTransactions(block.transactions)
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
                print("These transactions cannot be completed. Balance(s) of senders are insufficient!")
        return coveredTransactions

# This method checks if the sender has a sufficient balance to cover a TRANSFER type transaction. It also checks if the transaction is of type EXCHANGE.
    def transactionCovered(self, transaction):
        if transaction.type == 'EXCHANGE':
            return True
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False

# This method iterates through a list of transactions waiting to be executed.
    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)

# This method executes a transaction by updating the balance(s) of the parties/wallet(s) involved in the transaction with the account model object method.
    def executeTransaction(self, transaction):
        sender = transaction.senderPublicKey
        receiver = transaction.receiverPublicKey
        amount = transaction.amount
        self.accountModel.updateBalance(sender, -amount)
        self.accountModel.updateBalance(receiver, amount)