from Crypto.PublicKey import RSA
from Crypto import Random
import ast

key = RSA.generate(2048)

print(key)

binPrivKey = key.exportKey('DER')
binPubKey =  key.publickey().exportKey('DER')

print("private",binPubKey,"public",binPrivKey)

privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj =  RSA.importKey(binPubKey)

print("public",pubKeyObj,"private",privKeyObj)

msg = "attack at dawn"

encrypted = pubKeyObj.encrypt(msg.encode('utf-8'), 32)
print(encrypted)
dmsg = privKeyObj.decrypt(encrypted)
print(dmsg.decode('utf-8'))