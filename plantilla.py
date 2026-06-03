from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont # Parametros unificados de fuentes


ANCHO, ALTO = 700, 400
TITULO = "PyQt5 Plantilla"
text_btn = "Enviar"
text_input = "Ingrese algo..."

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        
        self.set_Window()
        self.config_Window()
        self.event_handler()
        self.show()

    def set_Window(self):
        
        self.btn = QPushButton(text_btn)
        # Parametros de estulo INDIVIDUALES
        self.btn.setStyleSheet('''
                    color: #ffffff;
                    background-color: #102db0;
                    border-radius: 15px;
                    padding: 10px;
                    font-weight: 600;
        ''')
        self.texto = QLabel("Historial: ")
        self.input = QLineEdit()
        self.input.setPlaceholderText(text_input)

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.input, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.texto, alignment=Qt.AlignLeft)

        self.setLayout(self.main_layout)

    def config_Window(self):
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)
        # Configuracion de fuente unificada
        font = QFont('Arial', 14, QFont.Cursive, True)
        self.setFont(font)

    def event_handler(self):
        self.btn.clicked.connect(self.set_text)
        
    def set_text(self):
        cadena = self.input.text()
        if cadena: 
            self.texto.setText(f"Registro: {cadena}")
            self.input.clear()

def run():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show() 
    app.exec_()

if __name__ == "__main__":
    run()
