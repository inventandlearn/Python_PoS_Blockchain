from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block

# Script which instantiates Block class, then demonstrates how transactions are extracted from the Transaction Pool object and then pacakaged into
# a Block object. This Block object has its own attributes which list x amount of transactions, it's blockcount, hash, etc.
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

block = Block(pool.transactions, 'lastHash', 'forger', 1)
print(block.toJSON())