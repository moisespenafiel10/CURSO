from pprint import pprint

def form() -> dict:
    nombre = input("Ingrese el nombre: ")
    ruc = int(input("Ingrese su RUC: "))
    direccion = input("Ingrese su direccion: ")
    sucursales = input("Ingrese sus sucursales separados por \",\" : ").split(",")
    diaHorario = input("Ingrese su horario en el dia: ")
    tardeHorario = input("Ingrese su horario en la tarde: ")

    return {"Nombre": nombre,
            "RUC": ruc,
            "Direccion": direccion,
            "Sucursales": sucursales,
            "Horario":{
                "dia": diaHorario,
                "tarde": tardeHorario
                }}

pprint(form())


# --ssl-insecure --script /home/lion/dev/rulLocal.py --set block_global=false --listen-host 0.0.0.0 --listen-port 8999