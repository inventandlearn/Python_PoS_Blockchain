from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint

# Script which instantiates Block class, then demonstrates how a genesis block is added to the Blockchain object.
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

block = wallet.createBlock(pool.transactions, 'lastHash', 1)
blockchain = Blockchain()
pprint.pprint(blockchain.toJSON())