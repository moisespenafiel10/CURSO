class Persona:
    def __init__(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    def comen(self,plato_fav:str):
        return f"yo {self.nombre} estoy comiendo mi {plato_fav}"
    def cagan(self):
        return "pipi popo"
    
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, sexo: str,carrera_profesional):
        super().__init__(nombre, edad, sexo)
        self.carrera_profesional=carrera_profesional
    def estudiar(self):
        return "estoy estudiando en POO"
class Trabajador(Persona)