import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils

# The PeerDiscoveryHandler object frequently checks the network of nodes to verify if new nodes are available or not.
# It broadcasts all the nodes/peers into the network so they can be made available to be connected to by already known nodes/peers.
class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socketCommunication = node

# This method starts threads for the status and discovery methods.
    def start(self):
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()

# This method sends a broadcast message to all nodes within the blockchain network as to whether or not a subject node is connected or disconnected.
    def status(self):
        while True:
            print('Status')
            time.sleep(10)

# This method sends a broadcast message to all nodes within the blockchain network as to what connections a subject node has established with other nodes.
    def discovery(self):
        while True:
            print('Discovery')
            time.sleep(10)