# from pprint import pprint
# #crear un sistema de gestion control de stok de productos.
# # caso de uso 
# # historia de ususario 
# # product over 
# # baclog
# # MVP
# # Prototipos de mie

# # ENTIDAD ENTITIS 
# # la base de datos sobre la que voy a trabajar 
# # las 3 formas normales (normalisacion de base de datos)
# productos=[
#     {
#         "id":1,
#         "nombre":"arroz",
#         "descripcion":"costeño costasl x 100 k",
#         "stok":5,
#         "unidad":"costales",
#         "predcio":125,
#         "moneda":"soles"
#     }
# ]


# class Producto:
#     def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
#             self.nombre=nombre
#             self.descripcion=descripcion
#             self.stock=stock
#             self.unidad=unidad
#             self.precio=precio
#             self.moneda=moneda
# # creacion de metodos

#     def registrar_producto(self):
#         nuevo_id = len (productos)+1
#         producto_nuevo={
#               "id":nuevo_id,
#               "nombre":self.nombre,
#               "descripcion":self.descripcion,
#               "stock":self.stock,
#               "unidad":self.unidad,
#               "precio":self.precio,
#               "moneda":self.moneda
#         }
#         productos.append(producto_nuevo)
#         return f"el siquiente producto se registro exitosamente{producto_nuevo}"
    
#     def mostrar_productos(self):
#         mensaje=f"tienes: {len(productos)} productos, -> {productos}"
#         return mensaje
#     def mostrar_producto(self,id):
#         producto_buscar = productos[id-1]
#         return producto_buscar
    
#     def eliminar_producto(self,id):
#          producto_eliminar=productos.pop(id-1)
#          return f" el siquiente producto fue eliminado {producto_eliminar}"
#     def actualizar_producto(self,id,clave,valor):
#         productos[id-1][clave] = valor

    
# prod=Producto("aceite","extra virgen",2,"botella x litro",12.50)
# pprint(prod.registrar_producto())
# pprint("ol")
# pprint(prod.mostrar_productos())
# pprint(prod.mostrar_producto(1))
# pprint(prod.eliminar_producto(2))
# pprint(prod.mostrar_productos())
## Tarea
#### 1. crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
##### ejemplo:
from pprint import pprint
from bd import *
class Tiendas_comerciales:

    def tienda_gerente(self, bd_negocios,nombe_gerente):
        respuesta = list(filter(lambda el: el ["gerente"] == nombe_gerente, bd_negocios))
        return respuesta
    
    def tienda_mas_categoria(self, bd_negocios):
        respuesta=list(filter(lambda el:len(el["categoria"])<2,bd_negocios))
        return respuesta
    
    def ruc_nombre(self, bd_negocios):
        respuesta=list(map(lambda el:{"nombre_negocio":el["nombre"],"ruc_negocio":el["ruc"]},bd_negocios))
        return respuesta
    
    def elimina_negocio(self, bd_negocios,ruc):
        respuesta=list(filter(lambda el:el ["ruc"]!=ruc,bd_negocios ))
        return respuesta
    
    def crear_negocio(self, ruc: int, nombre: str, categoria: str, horario_atencion: str, gerente: str):
        negocios.append({
        "ruc": ruc,
        "nombre": nombre,
        "categoria": categoria,
        "horario_atencion": horario_atencion,
        "gerente": gerente
    })
    
    def actualizar_horario(self, ruc: int, horario_atencion: dict):
        (negocio.update({'horario_atencion': horario_atencion}) for negocio in negocios if negocio['ruc'] == ruc)
        print(f'Horario de atencion actualizado: {horario_atencion}')


gerente=Tiendas_comerciales()
# pprint(gerente.tienda_gerente(negocios,"china"))
# pprint(gerente.tienda_mas_categoria(negocios))
# pprint(gerente.ruc_nombre(negocios))
#pprint(gerente.elimina_negocio(negocios,1234))
gerente.crear_negocio(ruc=518915, nombre="Mochi", categoria=["Burdel", "Las cariñosas"],horario_atencion={"dia": "8am-2pm"}, gerente="Yerald")
gerente.actualizar_horario(ruc=123456789,horario_atencion={"dia": "9am-6pm"})

# otreo metodo para crear un nuevo negocio 
# otro metodo para actualizar el horario de atencion