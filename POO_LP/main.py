# haciendo uso de la Poo crear un objeto para la entidad celular 
# class Celular:
#     def __init__(self, marca, modelo, almacenamiento, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.almacenamiento = almacenamiento
#         self.color = color


# mi_celular = Celular(marca="Samsung", modelo="Galaxy S21", almacenamiento="128GB", color="Negro")


# print("Marca:", mi_celular.marca)
# print("Modelo:", mi_celular.modelo)
# print("Almacenamiento:", mi_celular.almacenamiento)
# print("Color:", mi_celular.color)


# # 2.- haciendo uso de la POO crear un objeto para la entidad avion 

# class Avion:
#     def __init__(self, modelo, capacidad_pasajeros, alcance_km, velocidad_maxima_kmh):
#         self.modelo = modelo
#         self.capacidad_pasajeros = capacidad_pasajeros
#         self.alcance_km = alcance_km
#         self.velocidad_maxima_kmh = velocidad_maxima_kmh

# # Crear un objeto de la clase Avion
# mi_avion = Avion(modelo="Boeing 737", capacidad_pasajeros=150, alcance_km=3000, velocidad_maxima_kmh=900)

# # Acceder a los atributos del avión
# print("Modelo:", mi_avion.modelo)
# print("Capacidad de Pasajeros:", mi_avion.capacidad_pasajeros)
# print("Alcance (en kilómetros):", mi_avion.alcance_km)
# print("Velocidad Máxima (en km/h):", mi_avion.velocidad_maxima_kmh)



# # 3.- haciendo el uso de la poo crear un objeto para la entidad vehiculo

# class Vehiculo:
#     def __init__(self, marca, modelo, año, color, asientos):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#         self.color = color
#         self.asientos = asientos

# mi_vehiculo = Vehiculo (marca = 'Nisan', modelo = 'corolla' , año = '2015', color ='negro', asientos = '6')        
 
# print("marca: ", Vehiculo .marca)
# print("modelo: ", Vehiculo .modelo)
# print("año: ", Vehiculo .año)
# print("color: ", Vehiculo .color)
# print('asientos:',Vehiculo .asientos)

# # 4.- hacuiendo uso de la POO crear un objeto para un heroe de dota 2 
# class Personaje :
#     def __init__ (self, fuersa, agilidad, inteligencia) :
#         self.fuersa = fuersa
#         self.agilidad = agilidad
#         self.inteligencia = inteligencia

# mi_personaje = Personaje (fuersa = 'Cada punto en fuerza aumenta la salud máxima en 22', agilidad = ' Cada punto en agilidad aumenta la armadura en 0.167', inteligencia=' Cada punto en inteligencia aumenta el maná máximo en 12, la regeneración de maná en 0.05')

# print("fuersa: ", Personaje .fuersa)
# print("agilidad: ", Personaje .agilidad)
# print("inteligencia: ", Personaje .inteligencia)

# # 5.- haciendo usode la POO crear un objeto para una pc

# class PC:
#     def encender(self):
#         self.encendida = True
#         return "La PC se ha encendido."

#     def apagar(self):
#         self.encendida = False
#         return "La PC se ha apagado."


# mi_pc = PC()


# mi_pc.marca = "Dell"
# mi_pc.modelo = "XPS 13"
# mi_pc.procesador = "Intel Core i7"
# mi_pc.memoria_ram = "16GB"
# mi_pc.almacenamiento = "512GB SSD"


# mi_pc.encender()


# mi_pc.apagar()

# print("Marca:", mi_pc.marca)
# print("Modelo:", mi_pc.modelo)
# print("Procesador:", mi_pc.procesador)
# print("Memoria RAM:", mi_pc.memoria_ram)
# print("Almacenamiento:", mi_pc.almacenamiento)

# haciendo uso de la POO crear un objeto para una impresora 
# class Impresora:
#     def controlar(self, opcion):
#         if opcion == 1:
#             self.encender()
#         elif opcion == 2:
#             self.apagar()
#         else:
#             print("Opción no válida. Usa 1 para encender y 2 para apagar.")
#     def encender(self):
#         self.encendida = True
#         print("La impresora se ha encendido.")

#     def apagar(self):
#         self.encendida = False
#         print("La impresora se ha apagado.")

#     def imprimir(self, documento):
#         if self.encendida:
#             print(f"Imprimiendo '{documento}'...")
#         else:
#             print("No puedes imprimir, la impresora está apagada.")
    
#     def controlar(self, opcion):
#         if opcion == 1:
#             self.encender()
#         elif opcion == 2:
#             self.apagar()
#         else:
#             print("Opción no válida. Usa 1 para encender y 2 para apagar.")

# Crear un objeto de la clase Impresora
# mi_impresora = Impresora()

# Encender la impresora
# mi_impresora.encender()

# Imprimir un documento
# mi_impresora.imprimir("Documento1.txt")

# Apagar la impresora
# mi_impresora.apagar()

# Intentar imprimir después de apagar
# mi_impresora.imprimir("Documento2.txt")






    
    