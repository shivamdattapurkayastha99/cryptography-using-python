import hashlib,binascii
# crypt=hashlib.md5()
# crypt.update(b"hello")
# print(crypt.hexdigest())
# print(crypt.digest_size)
# dk = hashlib.pbkdf2_hmac('sha256', b'hello', b'salt', 100000)
# print(dk.hex())
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print(binascii.hexlify(dk))