from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint

# Script which instantiates Block class, then demonstrates how a signature is validated as false or true based on the public key string passed through.
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
signatureValid = Wallet.signatureValid(block.payload(), block.signature, fraudulentWallet.publicKeyString())
print(signatureValid)