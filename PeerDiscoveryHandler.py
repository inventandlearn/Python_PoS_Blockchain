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
            print('Current Connections:')
            for peer in self.socketCommunication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(5)

# This method ensures that all nodes within the blockchain network can find and establish connections with other nodes that have been newly added.
    def discovery(self):
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
            time.sleep(10)

# This method confirms that both nodes are connected and are ready to exchange information.
    def handshake(self, connected_node):
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connected_node, handshakeMessage)

# This method formats the message that will be sent once there is a handshake between two nodes.
# The format will structure the message to include messageType, data or the list of peers that exist on network, etc.
    def handshakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'Discovery'
        message = Message(ownConnector, messageType, data)
        encodedMessage = BlockchainUtils.encode(message)
        return encodedMessage

# This method handles incoming messages, updating the list of known peers, and establishes connections with new peers if neccessary.
# It ensures that the subject node doesn't connect with itself and avoids adding duplicate peers to the list.
    def handleMessage(self, message):
        peersSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peersSocketConnector):
                newPeer = False
        if newPeer:
            self.socketCommunication.peers.append(peersSocketConnector)

        for peersPeer in peersPeerList:
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown = True
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)
