from Crypto.Hash import SHA256
import json
import jsonpickle


# This class is used to produce hash outputs from JSON formatted inputs.
# These hash outputs are necessary to uniquely id transactions within the blockchain network as well as produce signatures for them.
class BlockchainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash


# This method encodes an object that is passed through into a JSON format.
    @staticmethod
    def encode(objectToEncode):
        return jsonpickle.encode(objectToEncode, unpicklable=True)

# This method decodes an object that has been encoded into a JSON format to it's original state/form.
    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)
