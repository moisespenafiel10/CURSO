from tkinter import *

# Crear la ventana principal
ventana =Tk()
ventana.title("Formulario de Datos")

# Crear etiquetas de texto y cajas de texto
etiqueta_nombre_apellido =Label(ventana, text="Nombre y Apellido:")
entrada_nombre_apellido =Entry(ventana)

etiqueta_dni =Label(ventana, text="DNI:")
entrada_dni = Entry(ventana)

etiqueta_celular = Label(ventana, text="Celular:")
entrada_celular = Entry(ventana)

# Colocar las etiquetas y cajas de texto en la ventana
etiqueta_nombre_apellido.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_nombre_apellido.grid(row=0, column=1, padx=10, pady=10)

etiqueta_dni.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_dni.grid(row=1, column=1, padx=10, pady=10)

etiqueta_celular.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_celular.grid(row=2, column=1, padx=10, pady=10)

widget_uno = Frame()

widget_uno.grid(row = '3', column = '0', padx=5, pady=10,rowspan=10,columnspan=2)
widget_uno.config(width = '300', height = '200')
widget_uno.config(bg='red')
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
