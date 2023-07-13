from capa_entrada import listaVacia, indice, palabra

from capa_proceso import getElements, checkDisco

from capa_salida import printMensaje, printError


# obteniendo 5 elemntos
lista = getElements(listaVacia)


# obteniendo palabra 'disco' e indice 
palabra, indice = checkDisco(lista)


# verificando si palabra e indice es None
if palabra is None and indice is None:
    #imprimiendo mensaje de error
    printError()
else:
    # imprimiendo indice y la palabra en un mensaje 
    printMensaje(indice, palabra)



