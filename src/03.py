from xor import break_single_xor, single_byte_xor

a = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

# Key seems to be second best
key = break_single_xor(a)[1]

res = single_byte_xor(a, bytes([key])).decode('UTF-8')
print(res)
