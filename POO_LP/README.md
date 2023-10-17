# programacion Orientado a objetos (Poo)
### En ingles es objetos orient programing(oop)
es un paradigma de programacion 
> **paradigma** - es un modelo , patron o ejemplo que se debe seguir  

Poo es un modelo de como programar 

**Objetivo** - el objetivo es organizar el codigo de manera que se asemeja a como pensamos en la vida real 

se basa en objetos 
y en la POO un objeto es toda entidad que se puede describir a travez de **atributos** y las **funciones**
que puede realisar la entidad .

# Atributos de clase y atributos de instancia

```python
class celular :
    # atributos de tipo clase 
    # que son iguales para todos los objetos 
    # que se creen 
    
    familia="smart phone"

    # atributos de instancia
    # son atributos propios del objeto
    # creamos una funcion inicializadora 
    def __init__(self,marca,modelo,imei,nrocelular):
        self.marca=marca
        self.modelo=modelo
        self,imei=imei
        self.nrocelular=nrocelular


    # Funcionalidades 
    def llamar(self.destino):
        return f'llamando a {destino}'

    # objeto celular jory 
    llamandojory=celular('poco','x5','42342353523','9353295732') # instanciando mi clase - creando mi objeto celular
    print(llamndojory.marca)
    print(llamndojory.familia)
    print(llamndojory.llamar('china'))

    # objeto celular nadine 

    llamandoNadine=celular('alcatel','basico','4857348634','947638445')
    print(llamandoNadine.marca)
    print(llamandojory.familia)
    print(llamandoNadine.llamar('ollanta'))
```