import random
from config import OPCIONES

class Juego:
    """
    Clase que representa el juego Piedra, Papel o Tijera.
    """

    def __init__(self):
        """
        Inicializa el juego con los puntajes en cero.
        """
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        self.rondas_jugadas = 0


    def obtener_eleccion_computadora(self):
        """
        Genera una elección aleatoria para la computadora.
        """
        return random.choice(OPCIONES)

    def determinar_ganador(self, eleccion_jugador, eleccion_computadora):
        """
        Determina el ganador de la ronda en función de las elecciones del jugador
        y la computadora.

        Actualiza el puntaje del jugador y la computadora, así como el número
        de rondas jugadas.

        Args:
          eleccion_jugador: La elección del jugador ("piedra", "papel" o "tijera").
          eleccion_computadora: La elección de la computadora ("piedra", "papel" o "tijera").

        Returns:
          Un string que indica el resultado de la ronda: "¡Ganaste!", "¡Perdiste!" o "Empate".
        """

        self.rondas_jugadas += 1

        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
                (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
                (eleccion_jugador == "tijera" and eleccion_computadora == "papel"):
            self.puntaje_jugador += 1
            return "¡Ganaste!"
        else:
            self.puntaje_computadora += 1
            return "¡Perdiste!"


    def juego_terminado(self):
        """
        Verifica si el juego ha terminado (algun jugador llega a 3 puntos).
        """
        return self.puntaje_jugador >= 3 or self.puntaje_computadora >= 3
