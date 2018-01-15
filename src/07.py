from base64 import b64decode
from block_crypto  import decrypt_aes_ecb
import os

key = "YELLOW SUBMARINE".encode('utf-8')
filename = "07.txt"

with open(filename, 'r') as f:
    encrypted = b64decode(''.join(f.readlines()))

print(decrypt_aes_ecb(encrypted, key))
