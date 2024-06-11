from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils
import copy

# This Node object will serve as the mechanism which connects users via a RESTAPI, p2p communication, and the blockchain.
# It can be seen as a managing agent which allows users to communicate and connect with the Blockchain.
class Node():

    def __init__(self, ip, port, key=None):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        if key is not None:
            self.wallet.fromKey(key)

# This method creates an instance of the SocketCommunication object and then calls it's respective startSocketCommunication method to initiate socket communication.
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

# This method attaches Rest API component to Node object.
    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

# This method manages each stage of a transaction during it's execution. Once transaction is executed and
# deemed valid, it is then moved to the transaction pool. Added conditions that ensure a transaction exists
# and is not in any existing blocks it can then be added to the newly forged block.
    def handleTransaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        signatureValid = Wallet.signatureValid(data, signature, signerPublicKey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        transactionInBlock = self.blockchain.transactionExists(transaction)
        if not transactionExists and not transactionInBlock and signatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector, 'Transaction', transaction)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
            forgingRequired = self.transactionPool.forgerRequired()
            if forgingRequired:
                self.forge()

# This method ensures that only valid blocks are added to the blockchain and spread across the network. It
# performs multiple validations on the block and processes it if all validations pass.
    def handleBlock(self, block):
        forger = block.forger
        blockHash = block.payload()
        signature = block.signature
        blockCountValid = self.blockchain.blockCountValid(block)
        lastBlockHashValid = self.blockchain.lastBlockHashValid(block)
        forgerValid = self.blockchain.forgerValid(block)
        transactionValid = self.blockchain.transactionValid(block.transactions)
        signatureValid = Wallet.signatureValid(blockHash, signature, forger)
        if not blockCountValid:
            self.requestChain()
        if lastBlockHashValid and forgerValid and transactionValid and signatureValid:
            self.blockchain.addBlock(block)
            self.transactionPool.removeFromPool(block.transactions)
            message = Message(self.p2p.socketConnector, 'Block', block)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)

# This method is responsible for broadcasting a request to other nodes
# in the blockchain network to send their respective blockchain copies.
# Blockchain synchronization is achieved with this method.
    def requestChain(self):
        message = Message(self.p2p.socketConnector, 'BLOCKCHAINREQUEST', None)
        encodedMessage = BlockchainUtils.encode(message)
        self.p2p.broadcast(encodedMessage)

# This method handles a blockchain request from a specific node within the network. It
# enables blockchain synchronization by allowing nodes to request and receive blockchain data
# from other nodes in the network.
    def handleBlockchainRequest(self, requestingNode):
        message = Message(self.p2p.socketConnector, 'Blockchain', self.blockchain)
        encodedMessage = BlockchainUtils.encode(message)
        self.p2p.send(requestingNode, encodedMessage)

# This method is the final piece in maintaining blockchain synchronization amongst each node that is a part of the network.
# Upon receiving a blockchain from another node, a node typically compares the block counts and adds any new blocks to
# its local copy, ensuring that its blockchain remains consistent with the network's state.
    def handleBlockchain(self, blockchain):
        localBlockchainCopy = copy.deepcopy(self.blockchain)
        localBlockCount = len(localBlockchainCopy.blocks)
        receivedChainBlockCount = len(blockchain.blocks)
        if localBlockCount < receivedChainBlockCount:
            for blockNumber, block in enumerate(blockchain.blocks):
                if blockNumber >= localBlockCount:
                    localBlockchainCopy.addBlock(block)
                    self.transactionPool.removeFromPool(block.transactions)
            self.blockchain = localBlockchainCopy

# This method is responsible for determining whether the current node is the next forger to create a
# new block in the blockchain.
    def forge(self):
        forger = self.blockchain.nextForger()
        if forger == self.wallet.publicKeyString():
            print('I am the next forger')
            block = self.blockchain.createBlock(self.transactionPool.transactions, self.wallet)
            self.transactionPool.removeFromPool(block.transactions)
            message = Message(self.p2p.socketConnector, 'Block', block)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
        else:
            print('I am not the next forger')


