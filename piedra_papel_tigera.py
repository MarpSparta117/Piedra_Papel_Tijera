import sys

from PyQt5.QtWidgets import QApplication

from game.view_qt import VentanaPrincipal

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())