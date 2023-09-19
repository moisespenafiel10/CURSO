# REPASO  DE PYTHON
### Primer paso para imprimir en consola
Para mostrar un mensaje en una consola en python utilizamos la funcion print ejemplo :
```python 
print ('hola mundo')
 ```
>## Tipos de Datos
#### STRING

```python 
a ## esto es un tipo de dato string
 ```
 > ## Controles de flujo 
 ### Decisiones  
solo se ejecuta el codigo si cumple o la condicion es verdadera , podemos hacer ue si la condicion sea falsa se ejecute otro codigo 
#### SINTAXIS 
primero especificar el codigo que se ejecutara si cumple una condicion
```python 
if <condicion> :
    # el codigo que deseamos ejecutar si la condicion es verdad
 ```
 si queremos que ejecute un codigo en caso sea falso
 ```python 
 if <condicion falsa>:
    print("solo imprimime si es verdad")
else :
    print("solo imprime si es falso ")
 ```
#### ejemplo 1
```python
if 15 > 18 :
    print('si es verdad imprime esto')
else:
     print('si es falso imprime esto')
```


 ### Ciclos
  existen dos tipos 
  ### cuando sabemos la cantidad de veces que vamos a repetir 

  para esto existe el **For**
  #### SINTAXIS
  despues de la palbra reservada for debemos crear una variablw que almacene el numero que iremos iterando.
  luego tendremos que indicar el arngi a iterar a los elementos 
  ```python
  vocales = 'a','e','i','o','u',
  for i in vocales :
    print(i)
```



  ### cuando no sabemos la cantidad de veces a repetir

  para esto existe el **while**
  ####  SINTAXIS
  ```python
  condicion = true
  while condicon:
    print('hola')
    texto = input('ingrese tu nombre o salir para terminar el programa')
    if texto == 'salir':
        condicon = false
```
> ## Funciones
exiaten dos tipos de funciones 

**1.- Propias del lenguage**  
ya biene creadas e insertadas en python y estan listas para ser usadas

**2.- Funciones creadas**  
tiene el nombre seguido de parentesis **( )**
dentro de los parentesis podremos pasarle datos que necesita la funcon para ejecutarse

**Print**

esta funcion nos permite imprimir

```python
print('hola')

# esta funcion nos permite saber la longitud de una lista o de un string

len ()

# len nos devuelve un numero

print(len([,2,3,,5,,7,8]))
```
es una funcion que se detiene a esperar que el usuario introdusca informacion

entre parentesis podremos escribir un mensaje que indique que accion reliza el usuario
```python
input('ingresa')
```
**Max**

 esta funcion nos muestra el numero mayor de una lista 
```python
lista = [45,12,78,3,24,50]
numero_mayor = max (litsta) 
print(numero_mayor)

resultado = 78
```
**Min**

 esta funcion nos muestra el numero menor de una lista 
```python
lista = [45,12,78,3,24,50]
numero_menor = min (litsta) 
print(numero_menor)

resultado = 3
```
**int** 

Funcion para convertir de un string a un numero entero

```python
int ('100') # ->> 100 ->> entero
```

**str**

Funcion para convertir un entero a un string

```python
str (100) # ->> '100' ->> str
```
**append**

Funcion de python que nos permite agregar elementos al final de una lista
```python
lista = [15,12,78]
elemento = 100
lista.append(elemento)
print (lista)

# resultado = [15,12,78,100]
```
**pop**

Funcion de python que nos permite eliminar los elementos que se encuentran al final de una lista
y almacena el elemento eliminado
```python
lista = [15,12,78]
elemento = 100
lista.pop()
print (lista)

#resultado = [15,12]
```
**insert**

Funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene qyue pasar dos parametros , primero indicarle el indice y segundo el dato que se va agregar .
```python
lista_nombre = ['jory','nadine','bichota']
lista_nombres.insert(1,'satan')
print (lista_nombres)

# resultado = ['jory','satan','nadine','bichota']
```
**remove**

Funcion de python que nos permite eliminar elementos de cualquier posicion de una lista , esta funcion ecibe solo el elemneto que deseamos eliminar
```python
lista = [4,5,6,7,8]
lista.remove(6)
print(lista)

# resultado = [4,5,7,8]
```
****
Funcion que nos permite dividir una lista en una cadena 
```python
cadena = 'hola como estan'
lista = cadena.split()
print(lista)

 #resultado = ['hola','como', 'estan']

 # ejemplo 
 url='wwww.golle.com/id=78923345'
 id = url.split('=').pop()
 print(id)

 # resultado =  78923345
```
## FUNCIONES CREADAS
> **Funcion** - son mini programas tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo.
#### PASOS PARA CREAR UNA FUNCION PROPIA
1.- Hacer uso de la palabra reservada def

2.- Definir un nombre de una funcion que describa que tarea va arealizar 

3.- Establecer los parametros que resivira la funcion parentecis ( ) .

4.- Establecer que valor o dato va a retornar mi       funcion con la palabra reservada return
> **Observacion** -
Tambien podemos hacer uso de la funcion print( ) para retornar un mensaje en nuestra funcion




