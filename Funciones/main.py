
texto = input('ingrese texto : ')

def cantidad_vocales(texto: str) -> int:
    count = 0
    for _ in list(texto):
        if _ in 'a':
            count +=1
        
    return count
print(f'''el texto tiene: {cantidad_vocales(texto)} vocal \'a\'''')
