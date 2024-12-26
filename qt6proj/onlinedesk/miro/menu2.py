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
        self.setFixedSize(200,100)
        self.setStyleSheet("background-image: url(fon.jpg);")

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QWidget {background-image: url(fon.jpg); border: 1px solid #fff000;} QPushButton {border-radius: 8px;border: 1px solid #000fff;padding: 5px 15px;}")


        self.setWindowTitle("Login")
        self.setFixedSize(500, 300)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setWindowIcon(QIcon("3.svg"))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0,0,0,0)
        

        self.username_label = QLabel("Логин:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введите логин")

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Вход")
        self.login_button.clicked.connect(self.handle_login)

        self.register_button = QPushButton("Регистрация")
        self.register_button.move(0,0)
        self.register_button.clicked.connect(self.open_registration_window)
        
        layoutEnter = QVBoxLayout()
        layoutEnter.insertWidget(-1,self.login_button)
        layoutEnter.insertWidget(-1,self.register_button)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addSpacing(100)
        layout.addLayout(layoutEnter)
        layout.addWidget(self.register_button)

        central_widget.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "user" and password == "pass":
            print(f"Логин: {username}, Пароль: {password}")
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Warning", "Неверный ввод данных")

    def open_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()
        self.close()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration")
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon("3.svg"))
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setStyleSheet("background-image: url(fon.jpg);")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.username_label = QLabel("Логин:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Введите логин для регистрации")

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.handle_register)

        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.back_to_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        layout.addWidget(self.back_button)

        central_widget.setLayout(layout)

    def handle_register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        print(f"Registered: Логин: {username}, Пароль: {password}")
        QMessageBox.information(self, "Registration", "Регистрация успешна")
        self.back_to_login()

    def back_to_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("3.svg"))
        self.setWindowTitle("Выход")
        button = QWarningButton("Выход")
        button.setCheckable(True)
        button.clicked.connect(self.click)

        self.setCentralWidget(button)

    def click(self):
        print("Кнопка выхода нажата")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
