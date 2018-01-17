from block_crypto import detect_ecb


with open("08.txt", 'r') as f:
    encrypted = [bytes.fromhex(line.strip("\n")) for line in f.readlines()]

for line in encrypted:
    if detect_ecb(line):
        print(line.hex())
