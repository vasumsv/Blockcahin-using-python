import time



class Block:
    """
        Block is unit of storage
    """
    def __init__(self,timestamp,last_hash,hash,data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},' 
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash}'
            f'data: {self.data})'
            )
            
    @staticmethod  #to make as static
    def mine_block(last_block, data):   #function to mine a block
        """
        Mines  a block based on the given last_block and data.
        """
        timestamp = time.time_ns()  #to record a time in nano seconds 
        last_hash = last_block.hash
        hash =  f'{timestamp} - {last_hash}'

        return Block(timestamp,last_hash,hash,data)

    @staticmethod  #to make as static
    def genesis(): #firt ever block in the blockchain
        """
        generate the genesis block
        """
        return Block(1,'genesis_last_hash','genesis_hash',[])
        

def main():
    genesis_block =Block.genesis()  #direct from block class
    block = Block.mine_block(genesis_block,'vasu')
    print(block)

if __name__ == '__main__':
    main()