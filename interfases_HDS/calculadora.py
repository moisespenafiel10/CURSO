from tkinter import *

# Función para calcular el resultado
def calcular():
    expresion = entrada.get()
    if expresion:
        resultado = eval(expresion)
        resultado_label.config(text="Resultado: " + str(resultado))
    else:
        resultado_label.config(text="")

# Configuración de la ventana
ventana = Tk()
ventana.title("Calculadora de mochi")

# Crear una entrada de texto
entrada = Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=4)

# Función para añadir caracteres a la entrada
def agregar_caracter(caracter):
    entrada.insert(END, caracter)

# Botones numéricos y operadores
botones = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '/', '='
]

row, col = 1, 0
for boton in botones:
    if boton == '=':
        Button(ventana, text=boton, width=7, height=2, command=calcular).grid(row=row, column=col)
    else:
        Button(ventana, text=boton, width=7, height=2, command=lambda b=boton: agregar_caracter(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Etiqueta de resultado
resultado_label = Label(ventana, text="")
resultado_label.grid(row=6, column=0, columnspan=4)

ventana.mainloop()
