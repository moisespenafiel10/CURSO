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


lista = [2,5,8,4,2]
# def sumaNumeros(arrayNumeros):
#     totalSuma=0
#     for numero in arrayNumeros :
#         totalSuma += numero 
#     return totalSuma
# print(sumaNumeros(lista))

def numeros_menores(arrayNumeros) -> list:
    menores = 0
    for numero in arrayNumeros:
        if numero < menores:
            menores=numero
    return menores
print(numeros_menores)