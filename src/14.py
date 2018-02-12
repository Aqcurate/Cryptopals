from block_crypto import encrypt_aes_ecb, detect_ecb
from base64 import b64decode
from random import randint
import os

chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.,;:(){}[]<>? -\n"

# Open unknown secret
with open("12.txt", 'r') as f:
    secret = b64decode(''.join(f.readlines()))

# Generate unknowns
key = os.urandom(16)
prefix = os.urandom(randint(1, 16))

# Target function
def encryption_oracle(a):
    return encrypt_aes_ecb(prefix + a + secret, key)

# Find block size
discovered = False
string = "A".encode()
while not discovered:
    if detect_ecb(encryption_oracle(string)):
        block_fill = string[:-1] + "C".encode()
        discovered = True
    else:
        string += "A".encode()

discovered = False
string = "B".encode()
while not discovered:
    if detect_ecb(encryption_oracle(block_fill+string)):
        block_length = len(string) // 2
        padding = len(block_fill) - len(string)
        discovered  = True
    else:
        string += "B".encode()

block_pad = "A".encode() * padding

# Break with chosen plaintext
answer = b''
i = 0
while True:
    string = b'A'*((block_length - i - 1) % block_length)
    output = encryption_oracle(block_pad+string)
    # Generate a dictionary of the encrypted outputs of last byte in block
    # Check if secret matches anything in dictionary
    for char in chars:
        test = encryption_oracle(block_pad + string+answer+char.encode())
        if test[block_length*((i//block_length)+(len(block_pad)//block_length)+1):block_length*((i//block_length)+(len(block_pad)//block_length)+2)] in output:
            answer += char.encode()
            i += 1
            break
    # If not, we are done
    else:
        break
print(answer.decode())
