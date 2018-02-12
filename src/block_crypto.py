from Crypto.Cipher import AES
from xor import xor
from struct import pack

def padding(string, padding_size=16):
    '''
    Args:
        string (bytes): The message to be padded
        padding_size (int): The desired final length of the string
    Return:
        String padded to the desired length
    '''
    padding_digit = padding_size - (len(string) % padding_size)
    padding = (chr(padding_digit) * padding_digit).encode()
    return string + padding

def remove_pad(string):
    '''
    Args:
        string (bytes): The padded message to be stripped
    Return:
        String without padding
    '''
    padding_size = string[-1]
    padding = string[-1:]
    removed = string[:-padding_size]
    if string[-padding_size:].strip(padding) != b"":
        raise ValueError('Incorrect padding')
    return removed

def decrypt_aes_ecb(message, key, block_size = 16):
    '''
    Args:
        message (bytes): The message to be decrypted
        key (bytes): The key to use in the decryption
    Return:
        Decrypted message
    '''
    cipher = AES.new(key, AES.MODE_ECB)
    msg = b''.join([message[i:i+block_size] for i in range(0, len(message), block_size)])
    return cipher.decrypt(msg)

def encrypt_aes_ecb(message, key, pad=True, block_size = 16):
    '''
    Args:
        message (bytes): The message to be encrypted
        key (bytes): The key to use in the encryption
        pad (bool): Whether the message should be padded
    Return:
        Encrypt message
    '''
    cipher = AES.new(key, AES.MODE_ECB)
    msg = b''.join([message[i:i+block_size] for i in range(0, len(message), block_size)])
    if pad:
        msg = padding(msg)
    return cipher.encrypt(msg)

def decrypt_aes_cbc(message, key, iv = (chr(0) * 16).encode()):
    '''
    Args:
        message (bytes): The message to be derypted
        key (bytes): The key to use in the decryption
        iv (optional bytes): The initialization vector for CBC mode
    Return:
        Decrypted message
    '''
    block_size = 16
    enc_message = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    dec_message = []
    dec_string = iv
    for i in range(0, len(enc_message)):
        decrypted = xor(decrypt_aes_ecb(enc_message[i], key), dec_string)
        dec_message.append(decrypted.decode())
        dec_string = enc_message[i]
    return ''.join(dec_message)

def encrypt_aes_cbc(message, key, iv = (chr(0) * 16).encode()):
    '''
    Args:
        message (bytes): The message to be encrypted
        key (bytes): The key to use in the encrypted
        iv (optional bytes): The initialization vector for CBC mode
    Return:
        Encrypted message
    '''
    block_size = 16
    message = padding(message)
    dec_message = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    enc_message = []
    enc_string = iv
    for i in range(0, len(dec_message)):
        encrypted = encrypt_aes_ecb(xor(dec_message[i], enc_string), key, False)
        enc_message.append(encrypted)
        enc_string = enc_message[i]
    return b''.join(enc_message)

def decrypt_aes_ctr(message, key, nounce = (chr(0) * 8).encode()):
    '''
    Args:
        message (bytes): The message to be derypted
        key (bytes): The key to use in the decryption
        nounce (optional bytes): 8 byte little endian initialization
    Return:
        Decrypted message
    '''
    ans = b''
    i = 0
    for x in message:
        if i % 16 == 0:
            count = pack('<Q', i // 16)
            keystream = encrypt_aes_ecb(nounce+count, key, False)
        ans += bytes([x ^ keystream[i % 16]])
        i += 1
    return ans

def detect_ecb(message):
    '''
    Args:
        message (bytes): The message to check
    Return:
        Wheter the encryption was made in ECB mode
    '''
    block_size = 16
    enc_message = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    return len(enc_message) != len(set(enc_message))
