from base64 import b64decode
from block_crypto import decrypt_aes_cbc

with open("10.txt", 'r') as f:
    encrypted = b64decode(''.join(f.readlines()))
key = 'YELLOW SUBMARINE'.encode()

print(''.join(decrypt_aes_cbc(encrypted, key)))
