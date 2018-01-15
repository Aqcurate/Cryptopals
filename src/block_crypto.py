from Crypto.Cipher import AES

def decrypt_aes_ecb(message, key):
    '''
    Args:
        message (bytes): The message to be decrypted
        key (bytes): The key to use in the decryption
    Return
        Decrypted message
    '''
    cipher = AES.new(key, AES.MODE_ECB)
    msg = cipher.decrypt(message)
    return msg.decode('utf-8')
