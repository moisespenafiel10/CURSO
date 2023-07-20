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

# dato = int(input('ingrese numero : '))
# factorial = 1
# if dato == 0 :
#   print('el factorial de 0 es 0')
# else:
#   for numero in range(1,dato + 1):
#     factorial = factorial*numero
#     print(factorial)

# frutas =[]
# while len(frutas)<5:
#     nuevaFruta=input('ingrese una fruta : ')
#     for fruta in frutas:
#       if len(nuevaFruta) == len(fruta):
#          print('misma longitud pendejo ingrese uno nuevo')
#     if nuevaFruta in frutas:
#       print ('esta fruta ya existe')         
#       continue
#     frutas.append(nuevaFruta)
  
# def textolargo(array):
#    longitudtexto=0
#    mostrarFruta=''
#    for index in range(0,len(array)):
#       if len(array[index]) > longitudtexto:
#         longitudtexto=len(array[index])
#         mostrarFruta=array[index]
#       return mostrarFruta
   
#    print(textolargo(frutas))
      
# CREAR UNA LISTA QUE ALMAZENE LOS NUMEROS DEL 1 AL 10 
# CREAR UNA FUNCION QUE ME PERMITA RECIBIR COMO PARAMERTO UNA LISTA
# LA FUNCION TENDR que retornar un nuvo array con todos los numeros pares que existen 


lista = [1,2,3,4,5,6,7,8,9,10]
def numpar (lista:list) -> list:
  newList=[]
  for _ , num in enumerate(lista):
      if num % 2 == 0:
          newList.append(num)
  
  return newList

print (numpar(lista))



    
