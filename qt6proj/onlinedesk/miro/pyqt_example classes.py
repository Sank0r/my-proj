import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

class QWarningButton(QPushButton):
    def __init__(self,title):
        super().__init__(icon=QIcon("strelka.svg"),text=title)
        self.setFixedSize(250, 250)
        
        
# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        button = QWarningButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("click")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
