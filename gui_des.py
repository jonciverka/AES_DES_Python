from tkinter import *
import tkinter
import logfileio 
import aes
import RSA
from tkinter.filedialog import askopenfilename
class Botoness:
	"""docstring for Botones"""
	def __init__(self, root):
		self.root= root
		self.root.geometry("680x100")	
		self.root.title("Herramienta de encriptamiento")


		self.label4 = Label(self.root, text="Key priv:")
		self.label4.grid(row=0,column=0)
		self.entry = Entry(self.root,width=60)
		self.entry.grid(row=0,column=1)
		self.archivo = Button(self.root, text = "LLave privada", command=lambda:self.subirLLave(self.root))
		self.archivo.grid(row=0,column=2)

		self.label4 = Label(self.root, text="Archivo:")
		self.label4.grid(row=1,column=0)
		self.entry = Entry(self.root,width=60)
		self.entry.grid(row=1,column=1)
		self.archivo = Button(self.root, text = "Archivo para desencriptar", command=lambda:self.subirArchivo(self.root))
		self.archivo.grid(row=1,column=2)

	def subirLLave(self,root):
		self.name_key = askopenfilename()
		self.frame1 = Frame(self.root)
		self.frame1.grid(row=0,column=1)
		label2 = Label(self.frame1, text=self.name_key)
		label2.grid(row=0,column=0)
		
	def subirArchivo(self,root):
		self.filename = askopenfilename()
		self.frame = Frame(root)
		self.frame.grid(row=2,column=1)
		label2 = Label(self.root, text=self.filename)
		label2.grid(row=1,column=1)
		#b = aes.leer_archivo(self,self.filename)
		self.Aes = Button(self.frame, text = "Desencriptar", command=lambda:RSA.RSA_des(self.name_key,self.filename))
		self.Aes.grid(row=1,column=0)

	

	#def enseñar_archivo(self,archivo):
	#	self.entry.insert(0,archivo)
	def mensaje(self):
		label3 = Label(self.frame, text="ARCHIVO DESENCRIPTADO")
		label3.grid(row=2,column=0)
	def asignarLlave(self):
		print(self.key.get())

	
		

		
