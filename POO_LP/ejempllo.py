from pprint import pprint
#crear un sistema de gestion control de stok de productos.
# caso de uso 
# historia de ususario 
# product over 
# baclog
# MVP
# Prototipos de mie

# ENTIDAD ENTITIS 
# la base de datos sobre la que voy a trabajar 
# las 3 formas normales (normalisacion de base de datos)
productos=[
    {
        "id":1,
        "nombre":"arroz",
        "descripcion":"costeño costasl x 100 k",
        "stok":5,
        "unidad":"costales",
        "predcio":125,
        "moneda":"soles"
    }
]


class Producto:
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
            self.nombre=nombre
            self.descripcion=descripcion
            self.stock=stock
            self.unidad=unidad
            self.precio=precio
            self.moneda=moneda
# creacion de metodos

    def registrar_producto(self):
        nuevo_id = len (productos)+1
        producto_nuevo={
              "id":nuevo_id,
              "nombre":self.nombre,
              "descripcion":self.descripcion,
              "stock":self.stock,
              "unidad":self.unidad,
              "precio":self.precio,
              "moneda":self.moneda
        }
        productos.append(producto_nuevo)
        return f"el siquiente producto se registro exitosamente{producto_nuevo}"
    
    def mostrar_productos(self):
        mensaje=f"tienes: {len(productos)} productos, -> {productos}"
        return mensaje
    def mostrar_producto(self,id):
        producto_buscar = productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
         producto_eliminar=productos.pop(id-1)
         return f" el siquiente producto fue eliminado {producto_eliminar}"
    def actualizar_producto(self,id,clave,valor):
        productos[id-1][clave] = valor

    
prod=Producto("aceite","extra virgen",2,"botella x litro",12.50)
pprint(prod.registrar_producto())
pprint("ol")
pprint(prod.mostrar_productos())
pprint(prod.mostrar_producto(1))
pprint(prod.eliminar_producto(2))
pprint(prod.mostrar_productos())
