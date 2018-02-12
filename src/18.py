from block_crypto import decrypt_aes_ctr
from base64 import b64decode

message = b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')

print(decrypt_aes_ctr(message, 'YELLOW SUBMARINE'))
