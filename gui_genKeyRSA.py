from tkinter import *
import tkinter
import logfileio 
import aes
import RSA
from tkinter.filedialog import askopenfilename
class Botones:
	"""docstring for Botones"""
	def __init__(self, root):
		root.geometry("680x50")	
		root.title("Herramienta de encriptamiento")
		self.label3 = Label(root, text="Escriba nombre del alumno")
		self.label3.grid(row=0,column=0)
		self.nombre = Entry(root,width=60)
		self.nombre.grid(row=0,column=1)
		self.archivo = Button(root, text = "Generar llave", command=lambda:RSA.gen_key(self.nombre.get()))
		self.archivo.grid(row=0,column=2)			


	
		

		
