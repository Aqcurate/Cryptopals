from xor import xor
a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
b = bytes.fromhex('686974207468652062756c6c277320657965')

res = xor(a, b).hex()
expected = '746865206b696420646f6e277420706c6179'
assert(res == expected)
