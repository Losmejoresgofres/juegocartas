from baraja import Baraja
from carta import Carta
from ma import Ma

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
    
    def jugar(self): # Método para mostrar la carta
        ma_jugador = Ma()
        carta = self.baraja.treure_carta()
        ma_jugador.afegir_carta(carta)
        ma_jugador.mostrar_cartes()
        print("Punts:", ma_jugador)

        while ma_jugador.valor < 21:

            acció = input("Vols una altra carta? (s/n): ")

            if acció == "s":
                carta = self.baraja.treure_carta()
                ma_jugador.afegir_carta(carta)
                ma_jugador.mostrar_cartes()
            else:
                break
        
        if ma_jugador == 21:
            print("¡Enhorabuena, compadre! Has ganado.")
        elif ma_jugador > 21:
            print("¡Ay, te has pasado! Has perdido, inténtalo de nuevo.")
        else: # Continuar el jugo,supongo