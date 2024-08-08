from juego import Juego
from jugador import Jugador

class Main:
    def __init__(self):
        self.palabras = ['casa', 'negro', 'pedro', 'perrito','confianza']
        self.juego = Juego(self.palabras)

    def iniciar(self):
        nombre_jugador = input("Introduce tu nombre: ")
        jugador = Jugador(nombre_jugador)
        self.juego.jugar(jugador)

if __name__ == "__main__":
    main = Main()
    main.iniciar()
