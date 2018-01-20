import os
import random
from block_crypto import encrypt_aes_ecb, encrypt_aes_cbc, detect_ecb

def get_random_bytes():
    return os.urandom(random.randint(5, 11))


def encryption_oracle(a):
    key = os.urandom(16)
    a = get_random_bytes() + a.encode('UTF-8') + get_random_bytes()
    if random.random() < .5:
        print('ECB')
        a = encrypt_aes_ecb(a, key)
    else:
        print('CBC')
        a = b''.join(encrypt_aes_cbc(a, key))
    
    return detect_ecb(a)

print(encryption_oracle('stanislaaaaav'))

