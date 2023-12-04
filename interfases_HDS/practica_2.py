from tkinter import *

# Función para realizar la operación (suma o resta)
def calcular():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = 0

    if operacion.get() == "Sumar":
        resultado = num1 + num2
    elif operacion.get() == "Restar":
        resultado = num1 - num2

    resultado_label.config(text=f"Resultado: {resultado}")

# Crear una ventana
ventana = Tk()
ventana.title("Calculadora")

# Etiqueta y entrada para el primer número
label_num1 = Label(ventana, text="Primer número:")
label_num1.grid()
entry_num1 = Entry(ventana)
entry_num1.grid()

# Etiqueta y entrada para el segundo número
label_num2 = Label(ventana, text="Segundo número:")
label_num2.grid()
entry_num2 = Entry(ventana)
entry_num2.grid()

# Opciones de operación (Sumar o Restar)
operacion = StringVar()
operacion.set("Sumar")  # Opción predeterminada
radio_sumar = Radiobutton(ventana, text="Sumar", variable=operacion, value="Sumar")
radio_restar = Radiobutton(ventana, text="Restar", variable=operacion, value="Restar")
radio_sumar.grid(row=2, column=2)
radio_restar.grid(row=1, column=2)

resultado_label = Label(ventana, text="Total: ")
resultado_label.grid()


# Botón para realizar el cálculo
calcular_button = Button(ventana, text="Calcular", command=calcular)
calcular_button.grid()

# Etiqueta para mostrar el resultado

# Iniciar la ventana
ventana.mainloop()
