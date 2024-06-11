from flask_classful import FlaskView, route
from flask import Flask, jsonify, request
from BlockchainUtils import BlockchainUtils
node = None

# The NodeAPI object is the Rest API component of the Node object within the blockchain system and is the foundation for the API endpoints.
class NodeAPI(FlaskView):

    def __init__(self):
        self.app = Flask(__name__)

# This method starts the Flask application.
    def start(self, apiPort):
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='0.0.0.0', port=apiPort)

# This method injects the Node object so that it can be accessed when any of the API's are called.
    def injectNode(self, injectedNode):
        global node
        node = injectedNode

# This endpoint returns a confirmation message with a GET method.
    @route('/info', methods=['GET'])
    def info(self):
        return 'This is a communication interface to a nodes blockchain', 200

# This endpoint returns a JSON format of the blockchain state.
    @route('/blockchain', methods=['GET'])
    def blockchain(self):
        return node.blockchain.toJSON(), 200

# This endpoint returns a JSON format of the transactions within the transaction pool.
    @route('/transactionPool', methods=['GET'])
    def transactionPool(self):
        transactions = {}
        for counter, transaction in enumerate(node.transactionPool.transactions):
            transactions[counter] = transaction.toJSON()
        return jsonify(transactions), 200

# This endpoint handles the logic for transactions executed on the blockchain.
    @route('/transaction', methods=['POST'])
    def transaction(self):
        values = request.get_json()
        if not 'transaction' in values:
            return 'Missing transaction value', 400
        transaction = BlockchainUtils.decode(values['transaction'])
        node.handleTransaction(transaction)
        response = {'message': 'Received Transaction'}
        return jsonify(response), 201
