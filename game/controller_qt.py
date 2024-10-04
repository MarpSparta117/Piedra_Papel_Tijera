from game.model import Juego  # Importamos la clase Juego del modelo


class Controlador:
    def __init__(self, vista):
        self.vista = vista    # Creamos una instancia de la vista
        self.juego = Juego()  # Creamos una instancia del modelo

    def jugar_ronda(self, eleccion_jugador):
        """
        Esta función se ejecutará cuando el jugador haga clic en un botón.
        Recibe la elección del jugador como argumento.
        """

        # Obtener la opcionde la computadora
        eleccion_computadora = self.juego.obtener_eleccion_computadora()

        # Actualizar el modelo con la elección del jugador.
        resultado = self.juego.determinar_ganador(eleccion_jugador, eleccion_computadora)

        # Actualizar la vista con el resultado y los puntajes.
        self.actualizar_vista(resultado, eleccion_jugador, eleccion_computadora)

        # Verificar si el juego ha terminado.
        if self.juego.juego_terminado():
            ganador = "Jugador" if self.juego.puntaje_jugador > self.juego.puntaje_computadora else "Computadora"
            self.vista.result_label.setText(f"¡{ganador} gana el juego!\n\n"
                                            f"Presiona 'Volver a empezar' para jugar de nuevo.")
            self.vista.mostrar_botones_eleccion(False)
            self.vista.mostrar_boton_reiniciar(True)

    def reiniciar_juego(self):
        """Reinicia el modelo del juego."""
        self.juego = Juego()
        self.vista.actualizar_marcador()

    def actualizar_vista(self, resultado, eleccion_jugador, eleccion_computadora):
        """Actualiza la etiqueta de resultado y los puntajes en la vista."""
        self.vista.result_label.setText(
            f"Elegiste: {eleccion_jugador}\n"
            f"La computadora eligió: {eleccion_computadora}\n"
            f"Resultado: {resultado}"
        )
        self.vista.actualizar_marcador()
