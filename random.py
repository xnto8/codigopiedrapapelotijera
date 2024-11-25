import random

# Función que define el juego
def jugar():
    opciones = ["piedra", "papel", "tijera"]
    
    # Entrada del jugador
    jugador = input("Elige entre piedra, papel o tijera: ").lower()
    
    # Verificar si la elección del jugador es válida
    if jugador not in opciones:
        print("Elección no válida. Intenta de nuevo.")
        return
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora elige: {computadora}")
    
    # Determinar el ganador
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡La computadora gana!")

# Iniciar el juego
if __name__ == "__main__":
    jugar()
