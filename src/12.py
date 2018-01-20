from block_crypto import encrypt_aes_ecb, encrypt_aes_cbc, detect_ecb
from base64 import b64decode
import os

chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.,;:(){}[]<>? "
variations = {}

with open("12.txt", 'r') as f:
    secret = b64decode(''.join(f.readlines())).replace(b"\n", b"")
key = os.urandom(16)

discovered = False
string = "A".encode()

def encryption_oracle(a):
    return encrypt_aes_ecb(a+secret, key)

while not discovered:
    if detect_ecb(encryption_oracle(string)):
        block_length = (len(string) // 2) - 1
        discovered = True
    else:
        string += "A".encode()

answer = []

for i in range(20):
    string = b''.join(["A".encode() for _ in range(block_length - i)])
    for char in chars:
        variations[char] = string + ''.join(answer).encode() + char.encode()
    for char in chars:
        if detect_ecb(encryption_oracle(variations[char] + string)):
            answer.append(char)

print(''.join(answer))
