from Transaction import Transaction
from Wallet import Wallet

# Script which instantiates Transaction class and Wallet class. Also validates if signature is by originator of transaction or not.
if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

wallet = Wallet()
fraudulentWallet = Wallet()
transaction = wallet.createTransaction(receiver, amount, type)
signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudulentWallet.publicKeyString())
print(signatureValid)