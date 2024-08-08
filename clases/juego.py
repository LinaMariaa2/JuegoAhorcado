import random
from palabra import Palabra
from jugador import Jugador

class Juego:
    def __init__(self, palabras):
        self.palabras = palabras
        self.palabra_actual = None
        self.jugador = None

    def elegir_palabra(self):
        self.palabra_actual = Palabra(random.choice(self.palabras))

    def jugar(self, jugador):
        self.jugador = jugador
        self.elegir_palabra()
        
        while self.jugador.intentos > 0 and not self.palabra_actual.es_completa():
            print(f"\nPalabra: {self.palabra_actual}")
            print(self.jugador)
            
            letra = self.jugador.hacer_adivinanza()
            if not self.palabra_actual.adivinar_letra(letra):
                self.jugador.perder_intento()
                print(f"Letra incorrecta. {self.jugador}")

            if self.palabra_actual.es_completa():
                print(f"¡Felicidades {self.jugador.nombre}! Has adivinado la palabra: {self.palabra_actual}")
                return
        
        if self.jugador.intentos == 0:
            print(f"¡Juego terminado, {self.jugador.nombre}! La palabra era: {self.palabra_actual.texto}")
