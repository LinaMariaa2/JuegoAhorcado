class Palabra:
    def __init__(self, texto):
        self.texto = texto
        self.letras_adivinadas = ['_'] * len(texto)

    def adivinar_letra(self, letra):
        if letra in self.texto:
            for i, l in enumerate(self.texto):
                if l == letra:
                    self.letras_adivinadas[i] = letra
            return True
        return False

    def es_completa(self):
        return '_' not in self.letras_adivinadas

    def __str__(self):
        return ' '.join(self.letras_adivinadas)
