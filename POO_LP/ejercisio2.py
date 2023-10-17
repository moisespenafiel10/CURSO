# crear una clase puesto de mercado que tenga un atributo de clase 5 atributos de instancia y 5 funcionalidades 
# debera crear 4 instancia de la clase puesto de mercado ejemplo puesto mechita,puesto la gringa,puesto ojo de uva

class PuestoDeMercado:
    # Atributo de clase
    num_puestos = 0

    def __init__(self, nombre, productos, lugar, horario, dueño):
        # Atributos de instancia
        self.nombre = nombre
        self.productos = productos
        self.lugar = lugar
        self.horario = horario
        self.dueño = dueño
        PuestoDeMercado.num_puestos += 1

    def mostrar_informacion(self):

        print(f"Nombre del puesto: {self.nombre}")
        print(f"Productos: {', '.join(self.productos)}")
        print(f"Ubicación: {self.lugar}")
        print(f"Horario: {self.horario}")
        print(f"dueño: {self.dueño}")

    def cambiar_dueño(self, nuevo_dueño):
        self.dueño = nuevo_dueño
        print(f"El nuevo dueño de {self.nombre} es {self.dueño}")

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        print(f"Se ha agregado {nuevo_producto} a la lista de productos de {self.nombre}")

    def abrir_puesto(self):
        print(f"{self.nombre} está abierto y disponible para clientes.")

    def cerrar_puesto(self):
        print(f"{self.nombre} está cerrado por hoy.")


# Crear instancias de la clase PuestoDeMercado
PuestoMechita = PuestoDeMercado("Puesto Mechita", ["Frutas", "Verduras", "Pan"], "Plaza Principal", "8:00 AM - 6:00 PM", "Carlos")
PuestoLaGringa = PuestoDeMercado("Puesto La Gringa", ["Tacos", "Burritos", "Salsas"], "Calle de los Sabores", "10:00 AM - 9:00 PM", "Maria")
PuestoOjoDeUva = PuestoDeMercado("Puesto Ojo de Uva", ["Vinos", "Quesos", "Aceitunas"], "Mercado Central", "9:00 AM - 7:00 PM", "Juan")

# información de los puestos
PuestoMechita.mostrar_informacion()
PuestoLaGringa.mostrar_informacion()
PuestoOjoDeUva.mostrar_informacion()

# Realizar acciones en los puestos
PuestoMechita.agregar_producto("Jugos Naturales")
PuestoLaGringa.cambiar_dueño("Luis")
PuestoOjoDeUva.abrir_puesto()
PuestoOjoDeUva.cerrar_puesto()

