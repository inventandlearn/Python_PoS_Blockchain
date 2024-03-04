from p2pnetwork.node import Node

# The SocketCommunication object is utilized by different nodes within the blockchain network to discover and connect to each other for transactions, and data exchange.
class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)

# This method is used for the initiation of socket communication between nodes. This method is inherited from the Node class.
    def startSocketCommunication(self):
        self.start()

# This method is a callback method that is used when a new inbound connection is made with another node that exists on the blockchain network.
    def inbound_node_connected(self, connected_node):
        print("inbound connection")
        self.send_to_node(connected_node, 'Your node has connected successfully to this node')

# This method is a callback method that is used when a new outbound connection is made with another node that exists on the blockchain network.
    def outbound_node_connected(self, connected_node):
        print("outbound connection")
        self.send_to_node(connected_node, 'This node is the initializer of communication between the connected nodes')

# This method sends messages between nodes that have established a connection with each other.
    def node_message(self, connected_node, message):
        print(message)



