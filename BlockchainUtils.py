from Crypto.Hash import SHA256
import json


# This class is used to produce hash outputs from JSON formatted inputs.
# Hash outputs neccessary for signature generation.
class BlockchainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash
