from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector

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
    def startSocketCommunication(self):
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
        print(message)

# This method allows for the sending of messages to specific nodes that aren't directly connected.
# The differentiation between this method and the node_message method is the directional flow of
# messages between all nodes present on the network. So a message sent between two connected nodes or a message sent
# by two or more unconnected nodes that however at still peers.
    def send(self, receiver, message):
        self.send_to_node(receiver, message)

# This method broadcast allows for the broadcasting of messages to all nodes within the network.
    def broadcast(self, message):
        self.send_to_nodes(message)


