from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils


# Wallet object that is necessary for parties to transact on blockchain.
# Built with RSA Keypair generator which generates public key and private key for encryption and decryption.
class Wallet():
    def __init__(self):
        self.KeyPair = RSA.generate(2048)

# Method used to generate a digital signature on the blockchain
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.KeyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()



