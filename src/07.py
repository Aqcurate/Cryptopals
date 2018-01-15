from base64 import b64decode
import os

key = "YELLOW SUBMARINE".encode('utf-8').hex()
filename = "07.txt"

command = 'cat {} | openssl enc -base64 -d | openssl enc -aes-128-ecb -d -K {}'.format(filename, key)
os.system(command)

