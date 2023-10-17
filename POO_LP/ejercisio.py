# crear un objeto CLASE laptop con dos atributos de clase 
# y 5 atributos de instancia devera tenerhasta 3 funcionalidades como minimo 
# crear 3 objetos instancia de clases distintos 


class Laptop:
    # Atributos de clase
    tecladoNumerico = True
    tipo='pc portatil'

    def __init__(self, modelo, almacenamiento, capacidad, procesador, ram):
        # Atributos de instancia
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.capacidad = capacidad
        self.procesador = procesador
        self.ram = ram

    def mostrar_informacion(self):
        # Funcionalidad 1: Mostrar información de la laptop
        print(f"Marca: {Laptop.tecladoNumerico}")
        print(f"Modelo: {self.tipo}")
        print(f"cap almacenamiento: Gbytes {self.almacenamiento}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Sistema Operativo: {Laptop.tipo}")

    def cambiar_sistema_operativo(self, nuevo_so):
        # Funcionalidad 2: Cambiar el sistema operativo
        Laptop.sistema_operativo = nuevo_so
        print(f"Sistema operativo cambiado a {nuevo_so}")

    def aumentar_ram(self, cantidad_gb):
        # Funcionalidad 3: Aumentar la cantidad de RAM
        self.ram += cantidad_gb
        print(f"RAM aumentada a {self.ram} GB")

# Crear objetos de la clase Laptop
laptop1 = Laptop("Dell XPS 13", 1200, 512, "Intel Core i7", 16)
laptop2 = Laptop("HP Pavilion", 800, 256, "AMD Ryzen 5", 8)
laptop3 = Laptop("dell", 1200, 512, "Intel Core i9", 8)
# Mostrar información de las laptops
laptop1.mostrar_informacion()
laptop2.mostrar_informacion()
laptop3.mostrar_informacion()
# Cambiar el sistema operativo de todas las laptops
laptop1.cambiar_sistema_operativo("Windows 11")
laptop2.cambiar_sistema_operativo("linux")
laptop3.cambiar_sistema_operativo("Mac os")
# Aumentar la RAM de una laptop
laptop1.aumentar_ram(64)
laptop1.mostrar_informacion()

        
