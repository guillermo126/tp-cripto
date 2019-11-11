from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import os
from tkinter import messagebox

root = Tk()
selec = IntVar()


# aca van a estar todos los metodos de mis ventanas
# ademas para crear la ventana y agregar boton, entradas de texto, etc..
class File:
    def __init__(self, window):  # constructor
        self.wind = window  # almaceno window en 'self.wind' para ponerle titulo
        self.wind.title("Cryptography Application")
        self.wind.geometry("600x500")

        frame = Frame(self.wind, width=100, height=100, relief="solid", bd=1)
        # le ponemos titulo al recuadro
        # frame.grid(row=0, column=0, columnspan=3, pady=20, padx=80)
        # manera en la que vamos a pocisionar los elementos mediante grid

        frame.place(x=155, y=80)

        text = Label(
            frame, text="Ingrese el archivo que desea Encriptar/Desencriptar"
        ).grid(row=1, column=0, pady=30)

        self.text = Entry(frame, width=30)
        self.text.place(x=10, y=70, width=250, height=30)
        self.text.configure(state="readonly")

        self.botonAbrir = Button(
            frame, text="Seleccionar archivo", command=lambda: abrir_archivo(self.text)
        )
        self.botonAbrir.grid(row=3, column=0, pady=30)

        self.radioButtonEncrypt = Radiobutton(
            frame, text="Encriptar      ", value=1, variable=selec
        ).grid(row=4, column=0)

        self.radioButtonEncrypt = Radiobutton(
            frame, text="Desencriptar", padx=90, value=2, variable=selec
        ).grid(row=5, column=0)

        selec.set(1)

        self.botonComenzar = Button(
            frame, text="Comenzar", command=lambda: comenzar(self.text), padx=30
        )
        self.botonComenzar.grid(row=6, column=0, pady=30)


def comenzar(text):
    if len(text.get()) != 0:
        if text.get().endswith(".bmp"):
            if selec.get() == 1:
                messagebox.showinfo("Title", "Encriptar")
            else:
                messagebox.showinfo("Title", "Desencriptar")
        else:
            messagebox.showinfo(
                "Error",
                "Ingrese archivo con extensi" + unichr(243).encode("utf8") + "n .bmp",
            )
    else:
        messagebox.showinfo(
            "Error",
            "Ingrese archivo con extensi" + unichr(243).encode("utf8") + "n .bmp",
        )


def abrir_archivo(text):
    archivo_abierto = filedialog.askopenfilename(
        initialdir="/",
        title="Seleccione archivo",
        filetypes=(("bmp files", "*.bmp"), ("all files", "*.*")),
    )
    abs_path = os.path.abspath(archivo_abierto)
    text.configure(state="normal")
    text.delete(0, END)
    text.insert(0, abs_path)
    text.configure(state="readonly")


# funcion main la cual ejecutara nuestra ventana
File(root)
root.mainloop()

