
from base_usuarios import *

class Usuario:
    def __init__(self, dni, nombre, f_nacimiento, edad, usuario, password):
        self.dni = dni
        self.nombre = nombre
        self.f_nacimiento = f_nacimiento
        self.edad = edad
        self.usuario = usuario
        self.password = password

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def verificar_existencia(self, usuarios, usuario):
        return any(u.usuario == usuario for u in usuarios)

    def validar_credenciales(self, usuarios, usuario, password):
        return list(filter(lambda u: u.usuario == usuario and u.password == password, usuarios))

# Ejemplo de uso:
usuarios = [
    Usuario(1231465789, "moises", "28/08/1990", 33, "admin", "1234"),
    Usuario(1231465789, "lucia", "05/08/2000", 23, "lele", "1234"),
    Usuario(1231465789, "mochi", "05/08/1998", 25, "mochisito", "1234"),
    Usuario(1231465789, "mariluz", "28/08/1990", 33, "juan", "5462"),
    Usuario(1231465789, "maritza", "28/08/1990", 33, "admin", "1234")
]

# Ejemplo de uso de los métodos:
usuario1 = usuarios[0]
usuario1.actualizar_edad(34)

existe_usuario = usuario1.verificar_existencia(usuarios, "admin")
print("¿Existe el usuario 'admin'?", existe_usuario)

usuarios_validos = usuario1.validar_credenciales(usuarios, "admin", "1234")
print("Usuarios válidos:", usuarios_validos)
