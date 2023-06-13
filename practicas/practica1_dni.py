dni = input("INGRESE NUMERO DE DNI : ")

longitud = len(dni)

if longitud <= 8:
    nombre = input("INGRESE NOMBRE COMPLETO : ")
    
    mensaje = f"""
    =========================
    HOLA BIENVENIDO {nombre}
    =========================
    """
else:
    print("el dni es incorrecto") 

