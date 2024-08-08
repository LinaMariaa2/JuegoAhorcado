class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos = 6

    def hacer_adivinanza(self):
        return input(f"{self.nombre}, adivina una letra: ").lower()

    def perder_intento(self):
        self.intentos -= 1

    def __str__(self):
        return f"{self.nombre} - Intentos restantes: {self.intentos}"
