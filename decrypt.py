
from Crypto.PublicKey import RSA
import base64
import gmpy2

with open('file1.pem') as f:
    pk1 = RSA.import_key(f.read())

with open('file2.pem') as f:
    pk2 = RSA.import_key(f.read())

with open('text1') as f:
    c1 = base64.b64decode(f.read())
    c1 = bytes_to_long(c1)

with open('text2') as f:
    c2 = base64.b64decode(f.read())
    c2 = bytes_to_long(c2)

g, a1, a2 = gmpy2.gcdext(pk1.e, pk2.e)
m = pow(c1, a1, pk1.n) * pow(c2, a2, pk2.n) % pk1.n
print(long_to_bytes(m))
