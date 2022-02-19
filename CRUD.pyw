from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Menu as mymenu
import tools as tl

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("250x540-600-150")
        self.raiz.iconbitmap("source/Play_Books_30007.ico")
        self.raiz.title("CRUD")
        self.menu = Menu(self.raiz)
        self.raiz.config(menu=self.menu)
        menu1 = mymenu
        menu1.menuUno(self.menu)

        self.libro = StringVar()
        self.genero = StringVar()
        self.autor = StringVar()
        self.anio = StringVar()
        self.id = IntVar()
        self.cd = BooleanVar()

        db = PhotoImage(master=self.raiz,
                        file='source/configuracion-de-la-base-de-datos.png')

        self.imagen1 = ttk.Label(self.raiz, image=db,
                                 anchor="center", width="45")
        self.lbl = ttk.Label(self.raiz,
                             text="ID:")
        self.lbl_id = ttk.Entry(self.raiz, textvariable=self.id, width=10)
        self.boton3 = Button(self.raiz, text="Eliminar",
                             command=self.eliminar, bg="#FF7876")
        self.boton4 = ttk.Button(self.raiz, text="Leer", command=self.read)
        self.separ2 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.etiq3 = ttk.Label(self.raiz,
                               text="NOMBRE DE LIBRO:")
        self.dist = ttk.Entry(self.raiz, textvariable=self.libro,
                              width=10)
        self.etiq1 = ttk.Label(self.raiz,
                               text="GENERO:")
        self.dist1 = ttk.Entry(self.raiz, textvariable=self.genero,
                               width=10)
        self.etiq4 = ttk.Label(self.raiz, text="AUTOR: ")
        self.coste = ttk.Entry(self.raiz, textvariable=self.autor,
                               width=10)
        self.etiq5 = ttk.Label(self.raiz, text="AÑO: ")
        self.coste5 = ttk.Entry(self.raiz, textvariable=self.anio,
                                width=10)
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self.raiz, text="Insertar", command=lambda:tl.CRUD().
                                 insert(self.libro.get(), self.genero.get(), self.autor.get(), self.anio.get()) or self.void())
        self.boton2 = ttk.Button(self.raiz, text="Update", state=DISABLED,
                                 command=self.update)
        self.imagen1.pack(side=TOP, fill=BOTH, expand=True,
                          padx=10, pady=5)
        self.lbl.pack(side=TOP, fill=BOTH, expand=True,
                      padx=10, pady=5)
        self.lbl_id.pack(side=TOP, fill=BOTH, expand=True,
                         padx=10, pady=5)
        self.boton3.pack(expand=False, fill=BOTH, padx=10, pady=10)
        self.boton4.pack(expand=False, fill=BOTH, padx=10, pady=0)
        self.separ2.pack(side=TOP, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.etiq3.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.dist.pack(side=TOP, fill=X, expand=True,
                       padx=20, pady=5)
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.dist1.pack(side=TOP, fill=X, expand=True,
                        padx=20, pady=5)
        self.etiq4.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.coste.pack(side=TOP, fill=X, expand=True,
                        padx=20, pady=5)
        self.etiq5.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.coste5.pack(side=TOP, fill=X, expand=True,
                         padx=20, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True,
                         padx=10, pady=10)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True,
                         padx=10, pady=10)
        self.raiz.mainloop()

    def void(self):
        self.dist.delete(0, END)
        self.dist1.delete(0, END)
        self.coste.delete(0, END)
        self.coste5.delete(0, END)

    def eliminar(self):
        if not self.id.get():
            valor = messagebox.showinfo("Error", "Campo es igual a 0")
        else:
            valor = messagebox.askokcancel(
                "Eliminar", "¿Estas seguro de eliminar este registro de la BD?")
            if valor:
                tl.CRUD().delete(self.id.get())
    def read(self):
        var = tl.CRUD().read(self.lbl_id.get())
        if not var:
            messagebox.showinfo("Error", "ID incorrecto")
        else:
            print(var)
            if not self.cd.get():
                self.libro.set(var[1])
                self.genero.set(var[2])
                self.autor.set(var[3])
                self.anio.set(var[4])
                self.boton2.config(state="normal")
                self.boton1.config(state="disabled")
                self.boton4.config(text="Limpiar")
                self.lbl_id.config(state="disable")
                self.cd.set(True)
            else:
                self.id.set(0)
                self.dist.delete(0, END)
                self.dist1.delete(0, END)
                self.coste.delete(0, END)
                self.coste5.delete(0, END)
                self.boton2.config(state="disabled")
                self.boton1.config(state="normal")
                self.boton4.config(text="Leer")
                self.lbl_id.config(state="normal")
                self.cd.set(False)

    def update(self):
        tl.CRUD().update(self.id.get(), self.libro.get(), self.genero.get(), self.autor.get(),
                       self.anio.get())
        self.dist.delete(0, END)
        self.dist1.delete(0, END)
        self.coste.delete(0, END)
        self.coste5.delete(0, END)
        self.boton2.config(state="disabled")
        self.boton1.config(state="normal")
        self.boton4.config(text="Leer")
        self.lbl_id.config(state="normal")
        self.cd.set(False)
def main():
    mi_app = Aplicacion()
    return 0
if __name__ == '__main__':
    main()
