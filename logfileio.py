import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import ast

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        #print(raw)
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

class RSACipher(object):
    def __init__(self):
        self.key = RSA.generate(2048) 

    def GenKey(self): 
        binPrivKey = self.key.exportKey('DER')
        binPubKey =  self.key.publickey().exportKey('DER')
        return binPrivKey,binPubKey

    def RSA_Encrypt(msg,key):
        pubKeyObj =  RSA.importKey(key)
        return pubKeyObj.encrypt(msg.encode('latin-1'), 32)

    def RSA_Decrypt(msg,key):
        privKeyObj = RSA.importKey(key)
        return privKeyObj.decrypt(msg)

