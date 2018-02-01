from tkinter import *
import tkinter
import logfileio 
import aes
import RSA
from tkinter.filedialog import askopenfilename
class Botones:
	"""docstring for Botones"""
	def __init__(self, root):
		self.root = root
		self.root.geometry("680x150")	
		self.root.title("Herramienta de encriptamiento")
		self.label3 = Label(self.root, text="Escriba Key")
		self.label3.grid(row=0,column=0)
		self.key = Entry(root,width=60)
		self.key.grid(row=0,column=1)
		keys = self.key.get()

		self.label4 = Label(self.root, text="Key_public:")
		self.label4.grid(row=1,column=0)
		self.entry = Entry(self.root,width=60)
		self.entry.grid(row=1,column=1)
		self.archivo = Button(self.root, text = "subir Llave publica.",command=lambda:self.subirLLave(self.root))
		self.archivo.grid(row=1,column=2)

		self.label4 = Label(self.root, text="Archivo:")
		self.label4.grid(row=2,column=0)
		self.entry = Entry(root,width=60)
		self.entry.grid(row=2,column=1)
		self.archivo = Button(self.root, text = "subir Archivo para encriptar", command=lambda:self.subirArchivo(self.root))
		self.archivo.grid(row=2,column=2)			
		
		
	def subirArchivo(self,root):
		self.filename = askopenfilename()
		self.frame = Frame(self.root)
		self.frame.grid(row=3,column=1)
		label2 = Label(self.root, text=self.filename)
		label2.grid(row=2,column=1)
		#b = aes.leer_archivo(self,self.filename)
		self.Aes = Button(self.root, text = "encriptar", command=lambda:aes.aes_enc(self,self.filename,self.key.get()))
		self.Aes.grid(row=4,column=1)

	def subirLLave(self,root):
		self.filename = askopenfilename()
		self.frame1 = Frame(self.root)
		self.frame1.grid(row=1,column=1)
		label2 = Label(self.frame1, text=self.filename)
		label2.grid(row=0,column=0)
		self.ok = Button(self.root, text = "Ok",command=lambda:RSA.RSA_enc(self,self.filename,self.key.get()))
		self.ok.grid(row=1,column=3)

	def mensaje(self):
		self.label3 = Label(self.root, text="ARCHIVO ENCRIPTADO")
		self.label3.grid(row=5,column=1)

	def mensaje_key(self):
		self.label4 = Label(self.root, text="Llave ingresada correctamente")
		self.label4.grid(row=3,column=1)

	def asignarLlave(self):
		print(self.key.get())


	
		

		
