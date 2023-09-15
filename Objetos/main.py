# def miObjeto(**valores):
    
#     nuevoObjeto = {
#         "nombre":valores["a"],
#         "apellido":valores["b"],
#         "edad":"",
#         "sexo":"",
#         "direccion":""
    
#  }
#     return nuevoObjeto
# # usuario = {
# #     "jose",
# #     "alvares",
# #     19,
# #     "toda la vida",
# #     "alla"
# # }

# print(miObjeto(a="jose",b="alvares"))


# lista = [2,5,8,4,2]
# def sumaNumeros(arrayNumeros):
#     totalSuma=0
#     for numero in arrayNumeros :
#         totalSuma += numero 
#     return totalSuma
# print(sumaNumeros(lista))

# def numeros_menores(arrayNumeros):
#     menores = 0
#     for numero in arrayNumeros:
#         if numero < menores:
#             menores=numero
#     return menores
# print(numeros_menores)
# def numeros_Mayores(lista):
#     i = 0
#     while i < len(lista):
#      = i + 1
#         while j < len(lista):
#             if lista[i] > lista[j]:
#                 temp = lista[i]
#                 lista[i] = lista[j]
#                 lista[j] = temp
#             j += 1
#         i += 1
#     return lista

# lista = [2,5,8,4,2]
# print(numeros_Mayores(lista))

# crear una funcion que reciba como parametro una lista -> array 
# y retorne una lista de objetos que tendra las caracteristicas  de cada elemento del array

def crear_objetos(lista):
    objetos = []
    for posicion, elemento in enumerate(lista):
        objeto = {
            'longitud': len(elemento),
            'palabra': elemento,
            'posicion': posicion,
            
        }
        objetos.append(objeto)
    return objetos

lista = ["bosque", "vih", "bonorrea"]
objetos_generados = crear_objetos(lista)
print(objetos_generados)

