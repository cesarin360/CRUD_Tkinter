from tkinter import *
from tkinter import messagebox
import table as t

def info():
	messagebox.showinfo("CRUD de César", "Version 2021 - SentellaCompany")
def licencia_aviso():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
def menuUno(menu):
	archivo=Menu(menu, tearoff=0)
	archivo.add_command(label="Connect DB")
	archivo.add_command(label="Salir", command=quit)
	tools=Menu(menu, tearoff=0)
	tools.add_command(label="Tabla", command=lambda:t.tb().tblib())
	ayuda=Menu(menu, tearoff=0)
	ayuda.add_command(label = "Licencia", command=lambda:licencia_aviso())
	ayuda.add_command(label= "Acerca de...", command=lambda:info())
	menu.add_cascade(label="Conectar", menu= archivo)
	menu.add_cascade(label="Herramientas", menu= tools)
	menu.add_cascade(label="Ayuda", menu= ayuda)
		
	

	
