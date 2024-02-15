from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
import pprint

# Script which instantiates Block class, then demonstrates how a signature is generated then subsequently assigned to Block object.
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
pprint.pprint(block.toJSON())