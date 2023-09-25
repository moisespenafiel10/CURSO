## Funciones utilizadas en pytho**

**append()** 

Esta función se utiliza para agregar elementos a una lista existente.

   Ejemplo:
   ```python
   mi_lista = [1, 2, 3]
   mi_lista.append(4)
   ```

**split()** 

divide una cadena en una lista de subcadenas según un delimitador especificado.

   Ejemplo:
   ```python
   frase = "Hola, mundo"
   palabras = frase.split(", ")
   ```

**join()** 

se usa para concatenar elementos de una lista en una sola cadena, utilizando un separador específico.

   Ejemplo:
   ```python
   palabras = ["Hola", "mundo"]
   frase = ", ".join(palabras)
   ```
****strip()**,**lstrip()**, **rstrip()** 

Estas funciones se utilizan para eliminar espacios en blanco u otros caracteres específicos del principio y/o final de una cadena.

   Ejemplo:
   ```python
   texto = "   Hola, mundo   "
   limpio = texto.strip()
   ```

**max()** y **min()**

 Se usan para encontrar el valor máximo y mínimo en una secuencia, respectivamente.

   Ejemplo:
   ```python
   numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
   maximo = max(numeros)
   minimo = min(numeros)
   ```

** **sum()** 

Calcula la suma de todos los elementos en una secuencia, como una lista o una tupla.

   Ejemplo:
   ```python
   numeros = [1, 2, 3, 4, 5]
   suma = sum(numeros)
   ```

**sorted()** 
**Ordena una secuencia en orden ascendente y devuelve una nueva lista ordenada.

   Ejemplo:
   ```python
   numeros = [5, 2, 1, 4, 3]
   numeros_ordenados = sorted(numeros)
   ```

**enumerate()** Se utiliza para obtener tanto el índice como el valor de los elementos en una secuencia.

   Ejemplo:
   ```python
   frutas = ["manzana", "banana", "cereza"]
   for indice, fruta in enumerate(frutas):
       print(f"Índice {indice}: {fruta}")
   ```

**zip()** 

Combina dos o más secuencias en tuplas emparejadas.

   Ejemplo:
   ```python
   nombres = ["Alice", "Bob", "Charlie"]
   edades = [25, 30, 35]
   resultado = zip(nombres, edades)
   ```

**abs()**   

Devuelve el valor absoluto de un número.

   Ejemplo:
   ```python
   numero = -5
   valor_absoluto = abs(numero)
   ```

## Algunas herramientas populares para crear entornos virtuales en Python
Crear entornos virtuales en Python es una práctica común para gestionar las dependencias de proyectos de forma aislada. Algunas de las herramientas populares para crear entornos virtuales en Python son:

1. **virtualenv**

 Virtualenv es una de las herramientas más antiguas y ampliamente utilizadas para crear entornos virtuales en Python. Te permite crear entornos virtuales independientes en los que puedes instalar paquetes y dependencias específicas para cada proyecto. Para usarlo, primero debes instalarlo con `pip` y luego crear un entorno virtual.

   ```bash
   pip install virtualenv
   virtualenv nombre_del_entorno
   source nombre_del_entorno/bin/activate  # En Linux/Mac
   nombre_del_entorno\Scripts\activate    # En Windows
   ```

2. **venv**

Venv es un módulo de la biblioteca estándar de Python que se utiliza para crear entornos virtuales. Es similar a virtualenv pero se incluye con Python 3.x, por lo que no es necesario instalarlo por separado.

   ```bash
   python -m venv nombre_del_entorno
   source nombre_del_entorno/bin/activate  # En Linux/Mac
   nombre_del_entorno\Scripts\activate    # En Windows
   ```

3. **conda** 

 Conda es una herramienta de gestión de paquetes y entornos desarrollada por Anaconda, que es especialmente útil para la ciencia de datos y la informática científica. Puedes crear entornos virtuales con conda usando los siguientes comandos:

   ```bash
   conda create --name nombre_del_entorno python=3.x
   conda activate nombre_del_entorno
   ```

4. **Pipenv**

Pipenv es una herramienta más moderna que combina la funcionalidad de `virtualenv` y `pip`. Además de crear entornos virtuales, también gestiona automáticamente un archivo `Pipfile` para gestionar las dependencias del proyecto.

   ```bash
   pip install pipenv
   pipenv --python 3.x
   pipenv shell
   ```

5. **poetry**

 Poetry es una herramienta de gestión de dependencias y creación de entornos virtuales que se ha vuelto cada vez más popular en la comunidad de desarrollo de Python. Puedes utilizarlo para crear un entorno virtual y gestionar las dependencias de tu proyecto.

   ```bash
   pip install poetry
   poetry new nombre_del_proyecto
   poetry install
   ```

