from block import Block
class Blockchain:

    def __init__(self):  #init function
        self.chain = [Block.genesis()]

    def add_block(self,data):  #add a new block function 
        self.chain.append(Block.mine_block(self.chain[-1],data))  #last_block and data the first block -1 represent the first block


    def __repr__(self):  #represent method
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()