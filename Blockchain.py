# The Blockchain object acts as a linked list that connects every new block created to previous blocks.
class Blockchain():

    def __init__(self):
        self.blocks = []

# This method adds each block created to a linked list of previously created blocks.
    def addBlock(self, block):
        self.blocks.append(block)