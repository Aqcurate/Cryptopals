from letter_freq import english_chi_squared
from hamming import guess_key_len

def xor(a, b):
    '''
    Args:
        a (bytes): List of bytes
        b (bytes): List of bytes
    Return:
        Byte object a ^ b
    '''
    return bytes([i ^ j for i, j in zip(a, b)])

def single_byte_xor(a, b):
    '''
    Args:
        a (bytes): List of bytes
        b (byte): Single-byte key
    Return:
        Byte object a ^ b
    '''
    return xor(a, b * len(a))

def repeating_key_xor(a, b):
    '''
    Args:
        a (bytes): List of bytes
        b (bytes): Multi-byte key
    Return:
        Byte object a ^ b
    '''
    q, r = divmod(len(a), len(b))
    return xor(a, b * q + b[:r])

def break_single_xor(a):
    '''
    Args:
        a (bytes): List of bytes
    Return:
        Most likely key based on english freq analysis
    '''

    return sorted(range(0, 256), key=lambda byte: english_chi_squared(single_byte_xor(a, bytes([byte]))))

def break_repeating_xor(a):
    '''
    Args:
        a (bytes): List of bytes
    Returns:
        Most likely key based on english freq analysis
    '''
    key_len = guess_key_len(a)[0]
    return bytes([break_single_xor(a[k::key_len])[0] for k in range(key_len)])
