import logfileio 
import gui
from tkinter import *
import tkinter
import gui_des

import gui_genKeyRSA

def main():
	root=Tk()	
	menu = Menu(root)
	root.config(menu=menu)
	subMenu = Menu(menu)
	menu.add_cascade(label="Nuevo", menu=subMenu)
	subMenu.add_command(label ="Encriptar", command=lambda:gui.Botones(root))
	subMenu.add_command(label ="Desencriptar", command=lambda:gui_des.Botoness(root))
	subMenu.add_command(label ="Generar Key", command=lambda:gui_genKeyRSA.Botones(root))
	subMenu.add_separator()
	subMenu.add_command(label="exit", command=root.quit)
	
	root.mainloop()	
main()