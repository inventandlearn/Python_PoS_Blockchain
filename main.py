from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block  import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

# Script which instantiates Account Model object hereby showing the balance of each wallet and it's corresponding publicKeyString.
if __name__ == '__main__':

    wallet = Wallet()
    accountModel = AccountModel()
    accountModel.updateBalance(wallet.publicKeyString(), 10)
    accountModel.updateBalance(wallet.publicKeyString(), -5)

    print(accountModel.balances)