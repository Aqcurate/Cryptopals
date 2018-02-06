from block_crypto import encrypt_aes_ecb, detect_ecb
from base64 import b64decode
import os

chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.,;:(){}[]<>? -\n"

# Open unknown secret
with open("12.txt", 'r') as f:
    secret = b64decode(''.join(f.readlines()))

# Generate unknown key
key = os.urandom(16)

# Target function
def encryption_oracle(a):
    return encrypt_aes_ecb(a+secret, key)

# Find block size
discovered = False
string = "A".encode()
while not discovered:
    if detect_ecb(encryption_oracle(string)):
        block_length = len(string) // 2
        discovered = True
    else:
        string += "A".encode()

# Break with chosen plaintext
answer = b''
i = 0
while True:
    string = b'A'*((block_length - i - 1) % block_length)
    output = encryption_oracle(string)
    # Generate a dictionary of the encrypted outputs of last byte in block
    # Check if secret matches anything in dictionary
    for char in chars:
        test = encryption_oracle(string+answer+char.encode())
        if test[0:block_length*((i//16)+1)] in output:
            answer += char.encode()
            i += 1
            break
    # If not, we are done
    else:
        break
print(answer.decode())
