# from tkinter import *
# ventana=Tk()
# ventana.title("monchi")
# ventana.geometry("500x500")
# colum_izquierda=Frame()
# colum_izquierda.grid(row=0,column=0)
# colum_izquierda.config(width=200,height=5)
# etiqueta=Label(ventana,text="esta es mi etiqueta")
# etiqueta.grid(row=0,column=1)
# ventana.mainloop()

# CREAR ETIQUETAS CON DOS CUADROS DE TEXTO CUADRO DE TEXTO A LA DERECHA 
# INGRESE OTRO NUMERO CUADRO DE TEXTO A LA DERECHA 
# RESULTADO CUADRO DE TEXTO A LA DERECHA 
# BOTTON DE  SUMAR Y BOTTON DE LIMPIAR 

from tkinter import *

# Función para sumar los números ingresados
def sumar():
    # try:
        num1 = float(entry_numero1.get())
        num2 = float(entry_numero2.get())
        resultado = int(num1 + num2)  # Convertir el resultado a entero
        entry_resultado.delete(0,END)  # Borrar el contenido anterior
        entry_resultado.insert(0, resultado)
    # except ValueError:
    #     entry_resultado.delete(0,END)
    #     entry_resultado.insert(0, "Error")

# Función para limpiar los cuadros de texto
def limpiar():
    entry_numero1.delete(0,END)
    entry_numero2.delete(0,END)
    entry_resultado.delete(0,END)

# Crear la ventana principal
ventana =Tk()
ventana.title("Calculadora")

# Crear los cuadros de texto y etiquetas
label_numero1 = Label(ventana, text="Número 1:")
entry_numero1 = Entry(ventana)

label_numero2 = Label(ventana, text="Número 2:")
entry_numero2 = Entry(ventana)

label_resultado = Label(ventana, text="Resultado:")
entry_resultado = Entry(ventana)

# Crear los botones
boton_sumar =Button(ventana, text="Sumar", command=sumar)
boton_limpiar =Button(ventana, text="Limpiar", command=limpiar)

# Colocar los elementos en la ventana
label_numero1.grid(row=0, column=0)
entry_numero1.grid(row=0, column=1)
label_numero2.grid(row=1, column=0)
entry_numero2.grid(row=1, column=1)
label_resultado.grid(row=2, column=0)
entry_resultado.grid(row=2, column=1)
boton_sumar.grid(row=3, column=0)
boton_limpiar.grid(row=3, column=1)

# Ejecutar la aplicación
ventana.mainloop()