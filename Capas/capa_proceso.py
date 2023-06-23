

resultado = match jugador., computadora:
        case _ if jugador == computadora:
            "Empate"
        case ("piedra", "tijera"), ("papel", "piedra"), ("tijera", "papel"):
            "¡Ganaste!"
        case _:
            "¡La computadora gana!"

    print("Tu jugada es:", jugador)
    print("La jugada de la computadora es:", computadora)
    print(resultado)
