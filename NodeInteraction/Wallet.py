from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block


# Wallet object that is necessary for parties to transact on blockchain.
# Built with RSA Keypair generator which generates public key and private key for encryption and decryption.
class Wallet():
    def __init__(self):
        self.keyPair = RSA.generate(2048)

# This method reads in already generated public key, private key, and staker key PEM files
# instead of using generated key pairs with the self.keypair attribute.
    def fromKey(self, file):
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.importKey(keyfile.read())
        self.keyPair = key


# Method used to generate a digital signature on the blockchain
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

# Method that verifies if signature belongs to the originator of any transaction on the blockchain.
    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

# Method that generates a string representation of the public key contained in the keyPair attribute defined above.
# Exports the public key in PEM format then decodes it into a utf-8 string.
    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

# Method that initiates a transaction within the sender's wallet.
    def createTransaction(self, receiver, amount, type):
        transaction = Transaction(self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

# Method that assigns signature to Block object. This signature is separate from the signature generated for each transaction.
# The Block object can be generated by a node that is chosen as a forger for the overall blockchain network. The chosen forger would use it's own wallet to do so.
    def createBlock(self, transactions, lastHash, blockCount):
        block = Block(transactions, lastHash, self.publicKeyString(), blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
