# The message object is utilized by each node for P2P communication. It will sent and received between two nodes that have an established connection.
class Message():

    def __init__(self, senderConnector, messageType, data):
        self.senderConnector = senderConnector
        self.messageType = messageType
        self.data = data

