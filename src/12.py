from block_crypto import encrypt_aes_ecb, encrypt_aes_cbc, detect_ecb
from base64 import b64decode
import os

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("12.txt", 'r') as f:
    secret = b64decode(''.join(f.readlines())).decode()
key = os.urandom(16)

discovered = False
string = "A".encode()

def encryption_oracle(a):
    return detect_ecb(encrypt_aes_ecb(a, key))

while not discovered:
    if encryption_oracle(string):
        block_length = (len(string) // 2) - 1
        discovered = True
    else:
        string += "A".encode()

string = b''.join(["A".encode() for _ in range(block_length)])
answer = []

for sec in secret:
    for char in chars:
        final = string + sec.encode() + string + char.encode()
        if encryption_oracle(final):
            answer.append(sec)   

print(''.join(answer))
