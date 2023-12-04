# importamos la liberria
from tkinter import *

# instanciamos nuestra clase TK

ventana = Tk() # clase para crear una ventana 
ventana.title("clase radiobutton") # haciendo usi del metodo title para el titulo de la ventana 
ventana.geometry("400x300") # haciendo uso del metodo geometry para asignarle un tamaño de ventana

# instanciar mi clase Label 
etiqueta = Label(ventana,text="radio buttons") # clase para crear una etiqueta 
# indicar la parte de mi ventana qwue deseo que se muestre
# puedo usar los metodos grid o pack 
etiqueta.config(fg="red",font=50)# para el color de letra, espaciado (heigth),(font) tamaño de texto
etiqueta.pack()

# instanciar la clase radiobutton
info=IntVar()
def mostrar_radio():
    respuesta = "eres masculino" if info.get()==1 else "eres femenino"
    etiquetaRespuesta=Label(ventana,text=respuesta)
    etiquetaRespuesta.pack()



radiomasculino= Radiobutton(ventana,text="masculino",value=1,variable=info)
radiomasculino.pack()
radiofemenino= Radiobutton(ventana,text="femenino",value=0,variable=info)
radiofemenino.pack()

# instanciar la clase button 
botons=Button(ventana,text="enviar",command=mostrar_radio)
botons.pack()

# llamar al metodo de Tk que me permite tener tener persistencia al mostra la ventana 
ventana.mainloop()

# 