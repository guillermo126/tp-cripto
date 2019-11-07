from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import os

root = Tk()


# aca van a estar todos los metodos de mis ventanas
# ademas para crear la ventana y agregar boton, entradas de texto, etc..
class File:
    def __init__(self, window):  # constructor
        self.wind = window  # almaceno window en 'self.wind' para ponerle titulo
        self.wind.title("Cryptography Application")
        self.wind.geometry("500x400")

        frame = LabelFrame(self.wind, text="Encripta un nueva archivo")
        # le ponemos titulo al recuadro
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        # manera en la que vamos a pocisionar los elementos mediante grid

        Label(frame, text="Ingrese el archivo que desea Encriptar/Desencriptar").grid(
            row=2, column=0
        )

        self.text = Entry(frame, width=60)

        self.botonAbrir = Button(
            frame, text="Seleccionar archivo", command=lambda: abrir_archivo(self.text)
        )
        self.botonAbrir.grid(row=3, column=0)


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
    text.grid(row=0, column=0)


# funcion main la cual ejecutara nuestra ventana
if __name__ == "__main__":
    window = Tk()
    application = File(window)
    window.mainloop()

