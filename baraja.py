import random
from carta import Carta

class Baraja:
    pals = ["Cors", "Diamants", "Trèvols", "Piques"]
    valors = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cartes = []
        for pal in self.pals:
            for valor in self.valors:
                cartacreada = Carta(pal, valor)
                self.cartes.append(cartacreada)
    
    def mostrar(self): # Método para mostrar la carta
        for carta in self.cartes:
            print(carta)

    def treure_carta(self):
        return self.cartes.pop()
    
    def barajar(self):
        random.shuffle(self.cartes) # Le paso una lista a shuffle y me la mexcla