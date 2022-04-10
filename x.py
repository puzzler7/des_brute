#!/usr/bin/env python3

from pydes import mydes

# ct = bytes.fromhex('29c28bc2992056c3b7c29fc28bc28c425f2a596237c3b850c3a563c399c39ec392c39632')
# ct = bytes.fromhex('c229c28b2099c356c2b7c29fc28b428c2a5f6259c33750b8a5c3c363c399c39ec3923296')
ct = open("clearence_code").read()
print(ct, len(ct))

d = mydes()

def num_to_key(n):
    out = []
    while n > 0:
        out.append(n&0xff)
        n >>= 8
    while len(out) < 7:
        out.append(0)
    return bytes(out[::-1])

# keyfile = open("weak", 'r').read().splitlines()
# keys = [bytes.fromhex(i.strip()) for i in keyfile]
# for key in keys:
#     key1 = key
#     key2 = bytes([i^0x1 for i in key])
#     for new_key in [key1, key2]:
#         print(new_key)
#         plain = d.decrypt(new_key, ct)
#         if 'jctf' in plain:
#             print(plain)
#             exit()
#         print(plain)
#         print(new_key)



for i in range(2**22, -1, -1):
    key = num_to_key(i)
    plain = d.decrypt(key, ct)
    if 'jctf' in plain:
        print(plain)
        print(key)
        exit()
    if i % 1000 == 0:
        print(i, '/', 2**22)