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
compra = int(input('ingrese monto de compra : '))

if compra >= 1000 :
    porcentaje = ""
    descuento = compra * 0.20 
    valor_pagar = compra - descuento

    print(f'ganaste el descuento del 20% ahora pagaras {valor_pagar}')
else :
    print(f'no aplicas el descuento : {compra} acumula mas puntos ')

