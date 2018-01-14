from base64 import b64decode
import os

key = "YELLOW SUBMARINE".encode('utf-8').hex()

command = 'cat 07.txt | openssl enc -base64 -d | openssl enc -aes-128-ecb -d -K {}'.format(key)

os.system(command)

