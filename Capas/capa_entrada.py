import random
def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    jugador = input("Elige tu jugada: piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)