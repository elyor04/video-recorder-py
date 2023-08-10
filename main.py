from PyQt6.QtWidgets import QApplication
from AppMainWindow import AppMainWindow
from sys import exit as sys_exit, argv as sys_argv


if __name__ == "__main__":
    app = QApplication(sys_argv)
    win = AppMainWindow()
    # app.setQuitOnLastWindowClosed(False)
    win.show()
    sys_exit(app.exec())
