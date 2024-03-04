from p2pnetwork.node import Node

# The SocketCommunication object is utilized by different nodes within the blockchain network to discover and connect to each other for transactions, and data exchange.
class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)

# This method is used for the initiation of socket communication between nodes. This method is inherited from the Node class.
    def startSocketCommunication(self):
        self.start()


