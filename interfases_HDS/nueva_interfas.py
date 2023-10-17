# 1. import tkinter -> libreria para la creacion de interfaces grficas 
from tkinter import *
# la libreria tkinter tiene  tiene tres clases para la creacion de interfaces 
# Tk() -> es el mas usado 
# Tkk() -> 
# Tcl()


# 2.-  instacnciar Tk() como generador de interfaz grafica 
nueva_ventana = Tk()

# 3.- frame es tambien una clase Frame() para crear un frmae tengo que primero instanciarlo 
menu_principal = Frame()
# montamos o inicializamos el frame
menu_principal.pack()
# haciendo uso del metodo config le damos un tamaño
menu_principal.config(width='200',height='200')
# haciendo uso del metodo config le asignamos un color 
menu_principal.config(bg='blue')
# metodo de TK() que mantiene la ejecucion del programa en un bucle
nueva_ventana.mainloop()


