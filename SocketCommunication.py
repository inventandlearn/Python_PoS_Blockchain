from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from BlockchainUtils import BlockchainUtils
import json

# The SocketCommunication object is utilized by different nodes within the blockchain network to discover and connect to each other for transactions, and data exchange.
class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)

# This method allows newly created nodes created to establish a connection with the very first node instantiated
# on the blockchain network. The newly created nodes can thereafter participate in the blockchain network's activities
    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost', 10001)

# This method is used for the initiation of socket communication between nodes. This method is inherited from the Node class.
    def startSocketCommunication(self, node):
        self.node = node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()

# This method is a callback method that is used when a new inbound connection is made with another node that exists on the blockchain network.
    def inbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)

# This method is a callback method that is used when a new outbound connection is made with another node that exists on the blockchain network.
    def outbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)

# This method sends messages between nodes that have established a connection with each other.
    def node_message(self, connected_node, message):
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == 'Discovery':
            self.peerDiscoveryHandler.handleMessage(message)
        elif message.messageType == 'Transaction':
            transaction = message.data
            self.node.handleTransaction(transaction)
        elif message.messageType == 'Block':
            block = message.data
            self.node.handleBlock(block)
        elif message.messageType == 'BLOCKCHAINREQUEST':
            self.node.handleBlockchainRequest(connected_node)
        elif message.messageType == 'Blockchain':
            blockchain = message.data
            self.node.handleBlockchain(blockchain)

# This method allows for the sending of messages to specific nodes that aren't directly connected.
# The differentiation between this method and the node_message method is the directional flow of
# messages between all nodes present on the network. So a message sent between two connected nodes or a message sent
# by two or more unconnected nodes that however are still peers.
    def send(self, receiver, message):
        self.send_to_node(receiver, message)

# This method allows for the broadcasting of messages to all nodes within the network.
    def broadcast(self, message):
        self.send_to_nodes(message)


