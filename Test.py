from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random

# This method serves as a utility function to generate a random string of lowercase letters,
# which will be used as a seed value for the validatorLots and winnerLot functions in the
# ProofofStake consensus algorithm. It is essential to incorporating randomness into the forger selection process.
def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString

if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('bob', 100)
    pos.update('alice', 100)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == 'bob':
            bobWins += 1
        elif forger == 'alice':
            aliceWins += 1

    print('bob won: ' + str(bobWins) + ' times')
    print('alice won: ' + str(aliceWins) + ' times')




