from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from game.controller_qt import Controlador  # Importamos la clase Controlador


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Piedra, Papel o Tijera")
        self.setGeometry(
            100, 100, 500, 400
        )  # Aumentamos un poco el tamaño de la ventana

        # Paleta de colores para el fondo con degradado
        paleta = QPalette()
        paleta.setColor(QPalette.Window, QColor("#2C3E50"))  # Color de fondo azul oscuro
        self.setPalette(paleta)

        # Etiqueta para mostrar el resultado con fuente más grande y estilo "gamer"
        self.result_label = QLabel(
            "¡Prepárate para jugar!", self
        )  # Renombrado a result_label
        fuente_etiqueta = QFont("Orbitron", 24, QFont.Bold)  # Fuente futurista
        self.result_label.setFont(fuente_etiqueta)
        self.result_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
        self.result_label.setStyleSheet(
            "color: #E74C3C; padding: 20px;"
        )  # Color rojo y padding

        # Etiquetas para los puntajes
        self.jugador_label = QLabel("Jugador: 0", self)
        self.computadora_label = QLabel("Computadora: 0", self)
        self.jugador_label.setFont(fuente_etiqueta)
        self.computadora_label.setFont(fuente_etiqueta)
        self.jugador_label.setAlignment(Qt.AlignCenter)
        self.computadora_label.setAlignment(Qt.AlignCenter)

        # Layout horizontal para los puntajes
        layout_puntajes = QHBoxLayout()
        layout_puntajes.addWidget(self.jugador_label)
        layout_puntajes.addWidget(self.computadora_label)

        # Botones para las opciones con colores, estilos y efectos hover
        self.boton_piedra = QPushButton("Piedra", self)
        self.boton_papel = QPushButton("Papel", self)
        self.boton_tijera = QPushButton("Tijera", self)

        # Botón "Volver a empezar" (inicialmente oculto)
        self.boton_reiniciar = QPushButton("Volver a empezar", self)
        self.boton_reiniciar.setStyleSheet(
            """
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Orbitron', sans-serif;
            }
            QPushButton:hover {
                background-color: #219653;
                box-shadow: 0 0 10px #219653;
            }
            """
        )
        self.boton_reiniciar.clicked.connect(self.reiniciar_juego)
        self.boton_reiniciar.hide()  # Ocultar el botón al inicio

        # Aplicar estilos a los botones con efectos hover
        self.boton_piedra.setStyleSheet(
            """
            QPushButton {
                background-color: #9B59B6;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Orbitron', sans-serif;
            }
            QPushButton:hover {
                background-color: #8E44AD;
                box-shadow: 0 0 10px #8E44AD;
            }
            """
        )
        self.boton_papel.setStyleSheet(
            """
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Orbitron', sans-serif;
            }
            QPushButton:hover {
                background-color: #219653;
                box-shadow: 0 0 10px #219653;
            }
            """
        )
        self.boton_tijera.setStyleSheet(
            """
            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                border-radius: 10px;
                font-family: 'Orbitron', sans-serif;
            }
            QPushButton:hover {
                background-color: #21618C;
                box-shadow: 0 0 10px #21618C;
            }
            """
        )

        # Layouts para organizar los widgets
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()

        # Agregar los botones a los layouts
        layout_vertical.addWidget(self.boton_reiniciar)  # Moved this line
        layout_horizontal.addWidget(self.boton_piedra)
        layout_horizontal.addWidget(self.boton_papel)
        layout_horizontal.addWidget(self.boton_tijera)

        # Agregar la etiqueta y el layout horizontal al layout vertical
        layout_vertical.addWidget(
            self.result_label
        )  # Usamos el nuevo nombre
        layout_vertical.addLayout(
            layout_puntajes
        )  # Agregamos el layout de puntajes
        layout_vertical.addLayout(layout_horizontal)

        # Establecer el layout principal de la ventana
        self.setLayout(layout_vertical)

        # Crear una instancia del controlador
        self.controlador = Controlador(self)

        # Conectar los botones a la función jugar_ronda del controlador
        self.boton_piedra.clicked.connect(
            lambda: self.controlador.jugar_ronda("piedra")
        )
        self.boton_papel.clicked.connect(
            lambda: self.controlador.jugar_ronda("papel")
        )
        self.boton_tijera.clicked.connect(
            lambda: self.controlador.jugar_ronda("tijera")
        )

    def mostrar_botones_eleccion(self, mostrar):
        """Muestra u oculta los botones de elección."""
        self.boton_piedra.setVisible(mostrar)
        self.boton_papel.setVisible(mostrar)
        self.boton_tijera.setVisible(mostrar)

    def mostrar_boton_reiniciar(self, mostrar):
        """Muestra u oculta el botón "Volver a empezar"."""
        self.boton_reiniciar.setVisible(mostrar)

    def reiniciar_juego(self):
        """Reinicia el juego y la vista."""
        self.controlador.reiniciar_juego()
        self.result_label.setText("¡Prepárate para jugar!")
        self.actualizar_marcador()
        self.mostrar_botones_eleccion(True)
        self.mostrar_boton_reiniciar(False)

    def actualizar_marcador(self):
        """Actualiza las etiquetas de los puntajes con los valores del controlador."""
        self.jugador_label.setText(f"Jugador: {self.controlador.juego.puntaje_jugador}")
        self.computadora_label.setText(
            f"Computadora: {self.controlador.juego.puntaje_computadora}"
        )
