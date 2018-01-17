from block_crypto import padding

string = "YELLOW SUBMARINE".encode()
padding_size = 20

print(padding(string, padding_size))
