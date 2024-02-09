"""
pyuic6 -o AppMainWindow/ui_form.py "path/to/file.ui"
"""

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QSystemTrayIcon,
    QMenu,
    QStyle,
    QMessageBox,
    QFileDialog,
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QDir, QTimer, QDateTime, QFileInfo
from .ui_form import Ui_MainWindow
from HKIPcamera import HKIPcamera
from os.path import join, dirname
import sys


def mkdir_cd(path: QDir, dirName: str) -> bool:
    path.mkdir(dirName)
    return path.cd(dirName)


class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.hkipc = HKIPcamera()

        self.trayIcon = QSystemTrayIcon(self)
        self.myTm = QTimer(self)
        self.recDir = str()

        self.isStarted = False
        self.success = False

        self.setupUi(self)
        self._init()

    def __del__(self) -> None:
        self.hkipc.release()

    def _init(self) -> None:
        self.ipAddress.setText("192.168.11.250")
        self.userName.setText("admin")
        self.password.setText("abcd1234")
        self.port.setText("8000")

        self.okButton.clicked.connect(self.okButton_clicked)
        self.browseTB.clicked.connect(self.browseTB_clicked)
        self.startButton.clicked.connect(self.startButton_clicked)
        self.stopButton.clicked.connect(self.stopButton_clicked)
        self.myTm.timeout.connect(self.refreshRecording)

        def quitAction():
            self.trayIcon.hide()
            QApplication.quit()

        icon_m = QMenu(self)
        icon_m.addAction(QAction("Show", self, triggered=self.show))
        icon_m.addAction(QAction("Hide", self, triggered=self.hide))
        icon_m.addSeparator()
        icon_m.addAction(QAction("Quit", self, triggered=quitAction))

        icon_i = QIcon(join(dirname(__file__), "resources", "icon.png"))

        def activatedIcon(reason):
            qAR = QSystemTrayIcon.ActivationReason
            if reason in [qAR.Trigger, qAR.DoubleClick]:
                self.showNormal()

        self.setWindowIcon(icon_i)
        self.trayIcon.setIcon(icon_i)
        self.trayIcon.setContextMenu(icon_m)
        self.trayIcon.activated.connect(activatedIcon)
        self.trayIcon.show()

    def refreshRecording(self) -> None:
        if self.isStarted:
            myDir = QDir(self.folder.text())
            now = QDateTime.currentDateTime()

            mkdir_cd(myDir, now.toString("yyyy"))
            mkdir_cd(myDir, now.toString("MM"))
            mkdir_cd(myDir, now.toString("dd"))

            myFile = myDir.filePath(now.toString("hh_mm_ss") + ".mp4")
            self.hkipc.saveRealData(myFile)

            sec = self.duration.value() * 60 - int(now.toString("ss"))
            self.myTm.start((sec + 1) * 1000)

        else:
            self.hkipc.stopSaveRealData()
            self.myTm.stop()

    def okButton_clicked(self) -> None:
        self.hkipc.release()
        self.hkipc.init()

        if self.hkipc.login(
            self.ipAddress.text(),
            self.userName.text(),
            self.password.text(),
            int(self.port.text()),
        ) and self.hkipc.realPlay(int(self.videoLabel.winId())):
            self.success = True
            QMessageBox.information(
                self, "Start process", "Success\nYou can go to another page"
            )
        else:
            self.videoLabel.clear()
            self.success = False
            QMessageBox.warning(self, "Start process", "Failed\nTry again")

    def browseTB_clicked(self) -> None:
        _f = QFileDialog.getExistingDirectory(
            self, "Choose a Folder to save Recordings"
        )
        if (not _f.isspace()) and (_f != ""):
            self.folder.setText(_f)

    def startButton_clicked(self) -> None:
        if not self.success:
            QMessageBox.about(self, "Record process", "No camera connected")
            return
        if self.isStarted:
            QMessageBox.about(self, "Record process", "Already started")

        elif QFileInfo(self.folder.text()).isDir():
            self.isStarted = True
            self.refreshRecording()
            QMessageBox.information(
                self, "Record process", "Success\nRecording started"
            )
        else:
            QMessageBox.warning(self, "Record process", "Error\nInvalid folder")

    def stopButton_clicked(self) -> None:
        if self.isStarted:
            self.isStarted = False
            self.refreshRecording()
            QMessageBox.information(
                self, "Record process", "Success\nRecording stopped"
            )
        else:
            QMessageBox.warning(self, "Record process", "Error\nNothing to stop")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppMainWindow()
    win.show()
    sys.exit(app.exec())
