import hashlib

key = b"str"
my_string = b"this is a normal string. nothing to see here"

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)
