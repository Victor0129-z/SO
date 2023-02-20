"""
Procesar por lotes un archivo con el siguiente formato:
b06:bf51:ef0f:7995:d321:4c8b:811c:1e99, Tabby, Jackett, tjackett9@flickr.com, Female, 148.202.30.5 

Intrucciones:
1.- Los primeros números están en hexadecimal; convertirlos a decimal
DECIMAL : DECIMAL : DECIMAL : DECIMAL : DECIMAL : DECIMAL : DECIMAL : DECIMAL :

2.- Eliminar las cadenas de texto y solo nos quedamos con la SEGUNDA CADENA de texto.
3.- Convertir a hexadecimal (letras en mayúscula) los últimos 4 datos: 148.202.30.5 
148 = 94
202 = CA
30 = 1E
5 = 5

4.- Reescribir en el archivo de salida con el siguiente formato:
Primero: la segunda cadena. 
Segundo: los números en decimal.
Tercero: los números en hexadecimal.

Ejemplo:
b06:bf51:ef0f:7995:d321:4c8b:811c:1e99,Tabby,Jackett,tjackett9@flickr.com,Female,105.18.162.229

Resultado:
Jackett : 2822 : 48977 : 61199 : 31125 : 54049 : 19595 : 33052 : 7833 : 94.CA.1E.5
""" 
import tkinter
import tkinter.ttk as ttk

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tkinter.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

main_window = tkinter.Tk()

combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True)
combo.config(width=600, height=600)

combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
combo.txt.config(borderwidth=3, relief="sunken")

style = ttk.Style()
style.theme_use('clam')

main_window.mainloop()