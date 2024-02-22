from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils

# Script which instantiates Block class, then demonstrates how a block is added to the Blockchain object after the genesis block has been added.
# Validation methods are implemented to ensure each block being added corresponds to the previous blockCount and hash.
# Added structure to how data is printed to console/terminal with pprint module.
if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

wallet = Wallet()
fraudulentWallet = Wallet()
pool = TransactionPool()
transaction = wallet.createTransaction(receiver, amount, type)

if pool.transactionExists(transaction) == False:
    pool.addTransaction(transaction)

blockchain = Blockchain()
lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
blockCount = blockchain.blocks[-1].blockCount + 1
block = wallet.createBlock(pool.transactions, lastHash, blockCount)

if not blockchain.lastBlockHashValid(block):
    print('lastBlockHash is not valid')
elif not blockchain.blockCountValid(block):
    print('Blockcount is not valid')
elif blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
    blockchain.addBlock(block)

pprint.pprint(blockchain.toJSON())