# crear un programa que me pida la edad de una persona si la edad es mayor o
# igual a 18 que me muestre un mensaje 'eres mayor de edad' o sino eres menor de edad 
# edad = int(input('ingrese edad : '))
# if edad >= 18 :
#     print('eres mayor de edad')
# else :
#     print('eres menor de edad')

## una tienda comercial desea hacer un programa de descuento del 20%, crear un programa que me determine
# si el cliente se hace acreedor del descuento teniendo en cuenta los siguiente
# si el cliente realiza una compra de igual o mayoe a 1000 soles mostrara un mensaje que diga 'ganaste el descuento
# en caso la compra no supere los 1000 soles entonces mostrar un mensaje que diga
# 'no aplicas el descuento <mostrar el monto de la cuenta
# compra = int(input('ingrese monto de compra : '))

# if compra >= 1000 :
#     porcentaje = ""
#     descuento = compra * 0.20 
#     valor_pagar = compra - descuento

#     print(f'ganaste el descuento del 20% ahora pagaras {valor_pagar}')
# else :
#     print(f'no aplicas el descuento : {compra} acumula mas puntos ')

    # crear un programa que me pida 5 veces  un nombre y por cada vez que lo pida muestre 
    # la cantidad de veces que ingreso el nombre
# Crear un diccionario vacío para almacenar los nombres y sus frecuencias
nombres = {}
for i in range(1,6):
    nombre = input("Ingrese un nombre: ")
    print(f"Ha ingresado el nombre {i} veces el nombre.")


# crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado
# es el premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira 
# pidiendo el nuemero premiado

numero_ganador = 50
condicion =True
while condicion:
    numero_ingresado = int(input('ingrese numero : '))
    if numero_ingresado == numero_ganador:
        print('ganaste')
        break
    else:
        print('sigue intentando')





 
 
    

