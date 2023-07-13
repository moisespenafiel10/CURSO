
# Obteniendo los datos 
def getElements(lista: list) -> list:
    while len(lista) <5:
        dato=input('Ingresa un dato: ')
        lista.append(dato)
    return lista


def checkDisco(lista):
    indice, palabra = None, None
    for texto in range(0, len(lista)):
        if lista[texto]== 'disco':
            palabra=lista[texto]
            indice=texto
    return palabra, indice
    
    

