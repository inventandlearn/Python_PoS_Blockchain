from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

# Script which demonstrates the addition of two blocks to the blockchain with each having different types of transactions contained in them.
# Also, built in method that refreshes transaction pool list so that the new block created doesn't contain transactions that have already
# been packaged into block"
if __name__ == '__main__':

    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()


    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')
    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)
    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockOne = forger.createBlock(coveredTransaction, lastHash, blockCount)
    blockchain.addBlock(blockOne)
    pool.removeFromPool(blockOne.transactions)


    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')
    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)
    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockTwo = forger.createBlock(coveredTransaction, lastHash, blockCount)
    blockchain.addBlock(blockTwo)
    pool.removeFromPool(blockTwo.transactions)

    pprint.pprint(blockchain.toJSON())
