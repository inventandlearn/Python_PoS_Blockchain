from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain

# This Node object will serve as the mechanism which connects users via a RESTAPI, p2p communication, and the blockchain.
# It can be seen as a managing agent which allows users to communicate and connect with the Blockchain.
class Node():

    def __init__(self):
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
