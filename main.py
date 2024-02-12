from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

# Script which instantiates Transaction Pool class, then demonstrates how a newly created transaction is added to the Transaction Pool.
# It also demonstrates that a duplicate transaction cannot be added to the Transaction Pool.
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

if pool.transactionExists(transaction) == False:
    pool.addTransaction(transaction)

print(pool.transactions)