# Clase carta

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    
    def __repr__(self): # Método para mostrar la carta
        return f"{self.valor} de {self.palo}"
