from PyQt6.QtWidgets import QApplication
from AppMainWindow import AppMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppMainWindow()
    # app.setQuitOnLastWindowClosed(False)
    win.show()
    sys.exit(app.exec())
