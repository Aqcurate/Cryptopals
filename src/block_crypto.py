from Crypto.Cipher import AES
from xor import xor

def padding(string, padding_size=16):
    '''
    Args:
        string (bytes): The message to be padded
        key (bytes): The desired final length of the string
    Return:
        String padded to the desired length
    '''
    padding_digit = padding_size - len(string)
    padding = (chr(padding_digit) * padding_digit).encode()
    return string + padding

def decrypt_aes_ecb(message, key):
    '''
    Args:
        message (bytes): The message to be decrypted
        key (bytes): The key to use in the decryption
    Return:
        Decrypted message
    '''
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.decrypt(message)
    return msg

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
    enc_message = []
    dec_message = []
    dec_string = iv
    for i in range(0, len(message), block_size):
        enc_message.append(padding(message[i:i+block_size]))
    for i in range(0, len(enc_message)):
        decrypted = xor(decrypt_aes_ecb(enc_message[i], key), dec_string)
        dec_message.append(decrypted.decode())
        dec_string = enc_message[i]
    return dec_message
