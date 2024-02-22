from Block import Block

# The Blockchain object acts as a linked list that connects every new block created to previous blocks.
class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]

# This method adds each block created to a linked list of previously created blocks.
    def addBlock(self, block):
        self.blocks.append(block)

# This method returns a dictionary of all the blocks that have been added to the Blockchain object.
    def toJSON(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJSON())
            data['blocks'] = jsonBlocks
            return data
