from BlockchainUtils import BlockchainUtils


# This Lot object can be thought of as a lottery ticket that is a necessary aspect of the Proof of Stake consensus algorithm.
# The instance of the class is generated with each stake made and it's attributes define respective stakers that have taken part in the lottery.
class Lot():

    def __init__(self, publicKey, iteration, lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.lastBlockHash = lastBlockHash

# This method generates hashes for each Lot object through hash chaining.
    def lotHash(self):
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData