import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self) -> None:
        self.chain = []                                 # an empty list that we’ll add blocks to
        self.pending_transactions = []                  # non approved transactions will sit in this queue
        self.new_block(previous_hash="Something", proof=100)
        pass
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1
    
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
    
blockchain = Blockchain()
t1 = blockchain.new_transaction("Ash", "Mike", "5 BTC")
t1 = blockchain.new_transaction("Mike", "Ash", "10 BTC")
t1 = blockchain.new_transaction("Ash", "Kim", "25 BTC")

blockchain.new_block(12345)

t1 = blockchain.new_transaction("Mike", "Alice", "5 BTC")
t1 = blockchain.new_transaction("Alice", "Bob", "115 BTC")
t1 = blockchain.new_transaction("Bob", "Mike", "52 BTC")

blockchain.new_block(6789)

print("Blockchain: ", blockchain.chain)
