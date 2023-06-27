##for numero in range (1,21):
# print(numero)

##Listas

### se separa con comas y entre corchetes [ ]
#vocales = ['a','e','i','o','u']

#for vocal in vocales:
#  print(vocal)

# colores = ['amarillo','rojo','azul','marron','anaranjado',]
# clr = input('ingrese color : ')
# for color in colores:
#   if color == clr :
#     print(color)
#     print(f"Se encontro el color:{color}")
#     break
#   print(color)

# dato = int(input('ingrese numero : '))
 
# for numero in range(1,12):
#     multiplicacion = dato * numero
#     print(f"""{dato}*{numero} = {multiplicacion} """)

dato = int(input('ingrese numero : '))
factorial = 1
if dato == 0 :
  print('el factorial de 0 es 0')
else:
  for numero in range(1,dato + 1):
    factorial = factorial*numero
    print(factorial)

    