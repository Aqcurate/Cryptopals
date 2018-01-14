from hamming import guess_key_len
from base64 import b64decode
from xor import break_repeating_xor, repeating_key_xor 

filename = '06.txt'

with open(filename, 'r') as f:
    message = b64decode(''.join(f.readlines()))

key_len = guess_key_len(message)[0]
key = break_repeating_xor(message)
print('The found key is: ', key.decode('UTF-8'))

# Slight error with key.
# Terminator X: Bring the ioise -> Terminator X: Bring the noise
# 'n' was the second best key for that character

key = b'Terminator X: Bring the noise'
print('\nThe revised key is: ', key.decode('UTF-8'))

res = repeating_key_xor(message, key).decode('UTF-8')
print('\n'+res)
