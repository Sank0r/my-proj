import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox, QSizePolicy  
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class QWarningButton(QPushButton):
    def __init__(self, title):
        super().__init__(icon=QIcon("strelka.svg"), text=title)
        self.setFixedSize(200, 200)
        self.setStyleSheet("background-image: url(fon.jpg);")

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.setFixedSize(400,200)
        self.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.setWindowIcon(QIcon("3.svg"))
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setStyleSheet("background-image: url(fon.jpg);")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        
        self.username_label = QLabel("Логин:")
        self.username_label.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введите логин")

        self.password_label = QLabel("Пароль:")
        self.password_label.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.textChanged.connect(self.password_text_changed)
        
        self.exo_label = QLabel(" ")
        self.password_input.textChanged.connect(self.exo_label.setText)
        
        

        self.login_button = QPushButton("Вход")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.exo_label)
        layout.addWidget(self.login_button)
        

        central_widget.setLayout(layout)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        self.setDisabled(True)
    
    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "user" and password == "pass":
            print(f"Логин: {username}, Пароль: {password}")
            self.open_main_window()
            self.setWindowTitle("New title")
        else:
            QMessageBox.warning(self, "warning", "Неверный ввод данных")

    def password_text_changed(self,text):
        self.exo_label.setText(text)
        

        
    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exit")
        button = QWarningButton("Выход")
        button.setCheckable(True)
        button.clicked.connect(self.click)

        self.setCentralWidget(button)

    def click(self):
        print(" click")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
