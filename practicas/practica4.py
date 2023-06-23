vocales='aeiouAEIOU'

ingresaV=input('ingrese vocal : ')
if len (ingresaV)==1 :

    if ingresaV in vocales :
        print('es una vocal minuscula')
    else:
        print('no es una vocal ni minuscula ni mayuscula')
else :
    print('ingrese solo un caracter')


    

