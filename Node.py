from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication

# This Node object will serve as the mechanism which connects users via a RESTAPI, p2p communication, and the blockchain.
# It can be seen as a managing agent which allows users to communicate and connect with the Blockchain.
class Node():

    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

# This method creates an instance of the SocketCommunication object and then calls it's respective method to initiate socket communication.
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication()