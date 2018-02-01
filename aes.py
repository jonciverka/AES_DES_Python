import logfileio 
import codecs
import gui
def aes_enc(self,nombre,key):
	objeto=logfileio.AESCipher(key)
	print(nombre)
	f= codecs.open(nombre,"r",encoding='utf-8',errors='ignore')	
	aux = f.read()
	f.close()
	print(len(aux))
	msn=objeto.encrypt(aux)
	msn = bytes(msn)
	print("tipo",type(msn))
	f1 = open("final.txt","ab")
	f1.write(msn)
	f1.close()

	gui.Botones.mensaje(self)
	
	print("Archivo encriptado")
def aes_des(llave_aes,mensaje_aes):
	llave_aes = str(llave_aes)
	#print(llave_aes,type(llave_aes), mensaje_aes,type(mensaje_aes))
	objeto=logfileio.AESCipher(llave_aes)
	#f= codecs.open(nombre,"r",encoding='utf-8',errors='ignore')	
	#aux = f.read()
	#print(len(mensaje_aes))
	#for linea in f:
	#	aux=linea
	ms=objeto.decrypt(mensaje_aes)
	f2 = open("documento chido.txt","w")
	f2.write(ms)
	f2.close()
	print("Archivo desencriptado")

#def leer_archivo(self,nombre):
#	f= open(nombre,"r")		
#	for linea in f:
#		aux=linea	
#	b = gui.Botones.enseñar_archivo(self,aux)
	