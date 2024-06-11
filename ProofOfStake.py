from Lot import Lot
from BlockchainUtils import BlockchainUtils
import os

# This ProofOfStake object tracks the stakes associated with each account in the AccountModel.
# It maps each stake to it's respective account.
class ProofOfStake():

    def __init__(self):
        self.stakers = {}
        self.setGenesisNodeStake()

# This method initializes the staking system, ensuring that the genesis node has a stake allocated to it from the beginning.
    def setGenesisNodeStake(self):
        current_directory = os.getcwd()
        genesisPublicKey = open('./keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesisPublicKey] = 1


# This method updates the stake of a given account in the AccountModel.
    def update(self, publicKeyString, stake):
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake


# This method gets the stake of a given account in the AccountModel.
    def get(self, publicKeyString):
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None

# This method generates lots for each staker based on the amount they've staked.
# The seed value is used for generating random numbers.
    def validatorLots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots

# This method determines the winning lot from a list of lots based
# on their proximity to a reference hash value generated from the
# seed input.
    def winnerLot(self, lots, seed):
        winnerLot = None
        distanceOffset = None
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue - referenceHashIntValue)
            if distanceOffset is None or offset < distanceOffset:
                distanceOffset = offset
                winnerLot = lot
        return winnerLot

# This method ties together the previous two methods (validatorLots and winnerLot)
# to select the forger for the next block based on the stakers'
# stakes and a random seed derived from the last block's hash.
    def forger(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey