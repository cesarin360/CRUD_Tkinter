from tkinter import *
from tkinter import ttk
import sqlite3


class tb():
    def __init__(self):
        self.window = Tk()
        self.window.title("Table Books")
        self.window.eval('tk::PlaceWindow . center')
        self.window.iconbitmap("source/book.ico")
        self.window.geometry("-625-250")
        self.cn = sqlite3.connect("GestionLibros")
        self.frame = Frame(self.window)
        self.frame.pack()
        self.table = ttk.Treeview(self.frame, height=15, columns=('#0', '#1', '#2', '#3'))
        self.table.grid(row=2, column=0, columnspan=5)
        self.search_entry = Entry(self.frame, width=15)
    def search(self):
        query = self.search_entry.get()
        selections = []
        for child in self.table.get_children():
            # compare strings in  lower cases.
            ls =str(self.table.item(child)['values'])
            if query.lower() in ls.lower():
                print(self.table.item(child)['values'])
                selections.append(child)
        print('search completed')
        self.table.selection_set(selections)
        curItem = self.table.focus()
        print(self.table.item(curItem)["values"])
    def tblib(self):
        cnCursor = self.cn.cursor()
        lb1 = Label(self.frame, text="Search:")
        lb1.grid(row=1, column=2, padx=120, pady=2, sticky=E)
        self.search_entry.grid(row=1, column=2, padx=10,
                               pady=10, sticky=E, rowspan=1)
        btn = Button(self.frame, text="search", width=10, command=self.search)
        btn.grid(row=1, column=3, padx=10, pady=5, sticky="nsew")
        boton1 = Button(self.frame, text="Actualizar", command=lambda: self.window.destroy(
        ) or self.window.after(0, tb().tblib()))
        boton1.grid(row=1, column=4, padx=10, pady=5, sticky="nsew")
        self.table.heading("#0", text="ID")
        self.table.heading("#1", text="LIBRO")
        self.table.heading("#2", text="GENERO")
        self.table.heading("#3", text="AUTOR")
        self.table.heading("#4", text="AÑO")
        self.table.column("#0", width=40)
        self.table.column("#1", width=150)
        self.table.column("#2", width=90)
        self.table.column("#3", width=100)
        self.table.column("#4", width=70)
        cnCursor.execute("SELECT * FROM LIBROS")
        productos = cnCursor.fetchall()
        print(productos)
        for pr in productos:
            print(pr)
            self.table.insert('', 0, text=pr[0], values=(pr[1],
                pr[2], pr[3], pr[4], pr[5]))
        self.cn.commit()
        self.cn.close()
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        if __name__ == '__main__':        
            self.window.mainloop()