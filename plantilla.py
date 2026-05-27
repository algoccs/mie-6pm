from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt
# Agregar el resto de componentes segun requiera

# CONSTANTES (parametros de inicializacion)
ANCHO, ALTO = 700, 400
TITULO = 'Plantilla PyQt5'
text_btn = 'Enviar'
text_input = 'Ingrease algo...'

# CLASE PRINCIPAL (VENTANA)
class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.set_window()
        self.config_window()
        self.event_handler()
        self.show()

    def set_window(self):
        # Estructurar el diseño de mi ventana
        self.btn = QPushButton(text_btn)
        self.texto = QLabel()
        self.input = QLineEdit(text_input)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.input, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.texto, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

    def config_window(self):
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)
        # Adaptar segun requiera

    def event_handler(self):
        # GESTION Y MANEJO DE EVENTOS (INTERACCION DEK USUARIO)
        self.btn.clicked.connect(self.set_text)

    def set_text(self):
        cadena = self.input.text()
        self.texto.setText(cadena)

# FUNCION PARA EJECUTAR LA APP
def run():
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()