from base_usuarios import usuarios

class Usuario:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def actualizar_edad(self, dni, nueva_edad):
        for u in self.usuarios:
            if u["dni"] == dni:
                u["edad"] = nueva_edad

    def verificar_registro(self, usuario):
        usuarios_registrados = list(filter(lambda u: u["usuario"] == usuario, self.usuarios))
        return len(usuarios_registrados) > 0

    def validar_credenciales(self, usuario, password):
        usuarios_registrados = list(filter(lambda u: u["usuario"] == usuario, self.usuarios))
        if len(usuarios_registrados) == 0:
            return "usuario valido"
        usuario_registrado = usuarios_registrados[0]
        return usuario_registrado["password"] == password

# Ejemplo de uso
gestor_usuarios = Usuario(usuarios)

# Actualizar la edad de un usuario por DNI
# gestor_usuarios.actualizar_edad(10, 38)
# print(usuarios)

# # # Verificar si un usuario está registrado
print(gestor_usuarios.verificar_registro("moises"))  # Debería devolver True

# # Validar credenciales de un usuario
# print(gestor_usuarios.validar_credenciales("mochi", "1234"))  # Debería devolver True

