from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key
print(key)
publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('hola'.encode('utf-8'), 32)
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted message:', encrypted) #ciphertext
f = open ('enc_RSA.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('enc_RSA.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(message)))

print ('decrypted', decrypted)

f = open ('des_RSA.txt', 'w')

f.write(decrypted.decode('utf-8'))
f.close()