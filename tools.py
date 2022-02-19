import sqlite3 
import logging
from concurrent.futures import ThreadPoolExecutor
from tkinter import messagebox

class CRUD():
	def __init__(self):
		self.ex = ThreadPoolExecutor(max_workers=2)
		self.cn = sqlite3.connect("GestionLibros")
		self.miCursor=self.cn.cursor()
	def insert(self, libro, genero, autor, anio):
		try:
			libros=[
		  		(libro, genero, autor, anio)
			]
			if libro and autor:
				self.miCursor.executemany("INSERT INTO LIBROS VALUES (NULL,?,?,?,?)", libros)
				self.ex.submit(self.cn.commit())
				messagebox.showinfo("Insertar", "Se ha insertado correctamente")
			else:
				messagebox.showinfo("Insertar", "Campos requeridos vacios")
		except:
			messagebox.showerror("Error", "Ha ocurrido un error inesperado")
		finally:
			self.cn.close()
	def delete(self, id):
		try:
			query = "DELETE FROM LIBROS WHERE ID=?"
			self.miCursor.execute(query, (id,))
			self.cn.commit()
			messagebox.showinfo("Eliminar", "Se ha eliminado correctamente")
		except:
			messagebox.showerror("Error", "Ha ocurrido un error inesperado")
		finally:
			self.cn.close()
	def read(self, id):
		try:
			self.miCursor.execute("SELECT * FROM LIBROS where ID=?",(id,))
			self.cn.commit()
			data = self.miCursor.fetchall()
			return list(data[0]) if data else data
		except:
			messagebox.showerror("Error", "Ha ocurrido un error inesperado")
		finally:
			self.cn.close()
	def update(self, id, libro, genero, autor, anio):
		try:
			self.miCursor.execute("UPDATE LIBROS SET LIBRO=?, GENERO=?, AUTOR=?, ANIO=? WHERE ID=?",
				(libro, genero, autor, anio,id,))
			self.cn.commit()
			messagebox.showinfo("Insertar", "Se ha insertado con exito")
		except:
			messagebox.showerror("Error", "Ha ocurrido un error inesperado")
		finally:
			self.cn.close()