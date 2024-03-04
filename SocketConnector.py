# The SocketConnector object is for storing ip, and port values of each connection.
class SocketConnector():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

# This method checks if the connection is secure by matching the inbound and outbound nodes ip and ports respectively.
    def equals(self, connector):
        if connector.ip == self.ip and connector.port == self.port:
            return True
        else:
            return False