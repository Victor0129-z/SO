from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
import os
import time

def browseFiles():
    file = open("archivoTerminado.txt", "w")
    
    with os.scandir(ruta_Carpeta) as ficheros:
        for fichero in ficheros:
            with open(fichero,"r") as archivo:
                for linea in archivo:
                    seccionContador = 0
                    fragmento = ''
                    almacen = ''
                    for caracter in linea:
                        fragmento = fragmento + caracter
                        if caracter == ',':
                            seccionContador = seccionContador + 1
                            if seccionContador == 3:
                                almacen = fragmento[:-1] + ' : ' + almacen
                            fragmento = ''
                        if caracter == ',' and seccionContador == 0:
                            seccionContador = seccionContador + 1
                            fragmento = ''
                        if seccionContador == 0:
                            if caracter == ':':
                                modulo = fragmento
                                convertidorHexadecimalADecimal = int(modulo[:-1], base=16)
                                almacen = almacen + str(convertidorHexadecimalADecimal) + ' : '
                                fragmento = ''
                        if seccionContador == 5:
                            if caracter == '.':
                                convertidorDecimalAHexadecimal = hex(int(fragmento[:-1]))
                                almacen = almacen + convertidorDecimalAHexadecimal[2:].upper() + '.'  
                                fragmento = ''
                            if caracter == "\n":
                                convertidorDecimalAHexadecimal = hex(int(fragmento[:-1]))
                                almacen = almacen + convertidorDecimalAHexadecimal[2:].upper()
                    if almacen != '':
                        file.write(almacen + "\n")
                        Output.insert(INSERT, almacen + "\n") 
            file.close()
            archivo.close()
        time.sleep(5)

def buscadorCarpetas():
    """ruta_Carpeta = '/Users/Victor/Documents/Python/Archivos' """
    global ruta_Carpeta
    ruta_Carpeta = filedialog.askdirectory(initialdir = "/",
                                            title = "Select a File")

window = Tk()
window.title('File Explorer')
window.geometry("740x400")
window.config(background = "white")

label_file_explorer = Label(window,
                            text = "Pr??ctica 01",
                            width = 100, height = 2,
                            fg = "blue")

button_explore = Button(window,
                        text = "Iniciar archivos",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Salir",
                     command = exit)

button_busqueda = Button(window,
                     text = "Seleccionar carpeta",
                     command = buscadorCarpetas)

Output = scrolledtext.ScrolledText(window, height = 6,
                                    width = 90,
                                    bg = "light cyan")

label_Contador = Label(window,text = "Pr??ctica 01", 
                            width = 100, height = 2,
                            fg = "blue")

label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)
Output.grid(column=1, row=4)
button_busqueda.grid(column=1, row=5)

window.mainloop()