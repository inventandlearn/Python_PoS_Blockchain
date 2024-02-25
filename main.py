from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node

# Script which instantiates the Node object which will be the access point for users to interact with the Blockchain, and it's various componenets.
if __name__ == '__main__':
    node = Node()
    print(node.blockchain)
    print(node.transactionPool)
    print(node.wallet)
