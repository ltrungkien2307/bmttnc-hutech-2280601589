# main.py
from blockchain import Blockchain

my_blockchain = Blockchain()

# Add transactions
my_blockchain.add_transaction("Alice", "Bob", 50)
prev_block = my_blockchain.get_previous_block()
proof = my_blockchain.proof_of_work(prev_block.proof)
my_blockchain.create_block(proof, prev_block.hash)

my_blockchain.add_transaction("Bob", "Charlie", 25)
prev_block = my_blockchain.get_previous_block()
proof = my_blockchain.proof_of_work(prev_block.proof)
my_blockchain.create_block(proof, prev_block.hash)

# Display blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 30)

# Check validity
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
