from Transaction import Transaction
from Wallet import Wallet

# Script which instantiates Transaction class and Wallet class. Also validates if signature is by originator of transaction or not.
if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender, receiver, amount, type)
    wallet = Wallet()
    signature = wallet.sign(transaction.toJSON())
    transaction.sign(signature)

    signatureValid = Wallet.signatureValid(transaction.toJSON(), signature, wallet.publicKeyString())
    print(signatureValid)

