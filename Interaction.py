from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests

# This method posts transactions to the blockchain network based on the
# peer to peer connections that have been established with the existing nodes on the network.
def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), amount, type)
    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)


# This script demonstrates how the functionality of each API endpoint works.
# This specific endpoint is used for posting transactions to the blockchain via Rest API.
if __name__ == '__main__':

    bob = Wallet()
    alice = Wallet()
    alice.fromKey('./keys/stakerPrivateKey.pem')
    exchange = Wallet()

    # forger: genesis
    postTransaction(exchange, alice, 100, 'EXCHANGE')
    postTransaction(exchange, bob, 100, 'EXCHANGE')
    postTransaction(exchange, bob, 10, 'EXCHANGE')

    # forger: Alice
    postTransaction(alice, alice, 25, 'Stake')
    postTransaction(alice, bob, 1, 'Transfer')
    postTransaction(alice, bob, 1, 'Transfer')
