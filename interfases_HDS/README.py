from tkinter import Tk, Button

ventana = Tk()

ventana.title("Mnovel.com")
ventana.geometry("400x300")

boton = Button(ventana, text="tocame !!")
boton.pack()
ventana.mainloop()