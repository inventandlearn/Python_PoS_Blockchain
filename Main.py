from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys


# Script which instantiates the Node object with SocketCommunication attributes then passes through an ip and port.
# Once a node is instantiated with the port 10002, communication between both nodes is then established. Thereafter messages can be sent back and forth.
# Script has been updated to include a genesisPrivateKey.pem keyFile that will be read in to generate the genesisNodeStaker to begin the forging process.

if __name__ == '__main__':

    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyFile = None
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(apiPort)
