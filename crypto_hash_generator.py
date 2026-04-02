import hashlib
from Crypto.Hash import keccak

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def keccak256_hash(text):
    k = keccak.new(digest_bits=256)
    k.update(text.encode())
    return k.hexdigest()

if __name__ == "__main__":
    msg = "blockchain2026"
    print("SHA256:", sha256_hash(msg))
    print("Keccak256:", keccak256_hash(msg))
