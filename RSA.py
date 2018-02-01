import logfileio
import codecs
import ast
import aes
import linecache
import gui
def gen_key(name):
	objeto = logfileio.RSACipher()
	privada, publica = objeto.GenKey()
	print(type(publica))
	f = open(name+"_public.txt","wb")
	f.write(publica)
	f.close()
	print("llave publica guardada")
	f = open(name+"_private.txt","wb")
	f.write(privada)
	f.close()
	print("llave privada guardada")

def RSA_enc(self,name,key_aes):
	f= open(name,"rb")	
	key_public = f.read()
	f.close()
	key_public = bytearray(key_public)
	key_public = bytes(key_public)
	enc = logfileio.RSACipher.RSA_Encrypt(key_aes,key_public)
	enc1 = str(enc) 
	f = open("final.txt","a")
	f.write(enc1+"\n")
	f.close()
	print("key ingresada")
	gui.Botones.mensaje_key(self)

def RSA_des(name_key,name_file):
	f= open(name_key,"rb")	
	key_private = f.read()
	f.close()	
	key_private = bytearray(key_private)
	key_private = bytes(key_private)
	f= open(name_file,"r")		
	file = f.readline()
	print(type(file))
	lineas = len(f.readlines())
	print("numero =", lineas)	
	for x in range(0, lineas):
		print("stoy aqui")
		line = linecache.getline(name_file, x+1)	
		file = ast.literal_eval(line) 
		llave_aes = logfileio.RSACipher.RSA_Decrypt(file,key_private)	
		print(len(llave_aes))
		if len(llave_aes) == 256:
			print("hola")
		else:
			print("es la chida")
			break

	
	f.close()
	f=open(name_file,"rb")
	for i,linea in enumerate(f):
	  if i<lineas:
	    continue
	  mensaje_aes = linea
	mensaje_aes = str(mensaje_aes,'utf-8')
	llave_aes = str(llave_aes,'utf-8')
	aes.aes_des(llave_aes,mensaje_aes)
