from tkinter import*
def enviar_boton(ventana,valor):
    if valor == "=":
        expression=ventana.caja_operaciones.get().replace()
        resultado=eval(expression)
        print(resultado)
    elif valor == "C":
        ventana.operacion_label.config(text="")
        ventana.caja_operaciones.delete(0,END)
    elif valor == "<":
        print("te borro el chikito")
    else:
        valor_actual=ventana.caja_operaciones