# The SocketConnector object is for storing ip, and port values of each node's socket.
class SocketConnector():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

# This method is for connection management between nodes. It prevents duplicate connections.
# The connection is secured by matching the inbound and outbound nodes ip and ports respectively.
    def equals(self, connector):
        if connector.ip == self.ip and connector.port == self.port:
            return True
        else:
            return False