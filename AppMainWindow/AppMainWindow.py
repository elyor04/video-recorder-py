"""
pyuic6 -o ui_form.py "/home/user/Documents/qt-projects/ip-cam/mainwindow.ui"
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
from PyQt6.QtGui import QImage, QPixmap, QAction
from PyQt6.QtCore import QDir, QTimer, QDateTime, QFileInfo
from .ui_form import Ui_MainWindow
from HKIPcamera import HKIPcamera
from cv2 import VideoWriter, Mat, resize, INTER_AREA
from sys import exit as sys_exit, argv as sys_argv

DURATION = 1  # recording minute


def mkdir_cd(path: QDir, dirName: str) -> bool:
    path.mkdir(dirName)
    return path.cd(dirName)


def cvMatToQImage(inMat: Mat) -> QImage:
    height, width, channel = inMat.shape
    bytesPerLine = 3 * width
    qImg = QImage(inMat.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
    return qImg.rgbSwapped()


def cvMatToQPixmap(inMat: Mat) -> QPixmap:
    return QPixmap.fromImage(cvMatToQImage(inMat))


def f_ImageDataCallBack(bgrMat: Mat, myWin: "AppMainWindow") -> None:
    height, width, channel = bgrMat.shape

    if myWin.reOpen:
        if myWin.writer.isOpened():
            myWin.writer.release()
        myWin.reOpen = False

    if myWin.isReady:
        if not myWin.writer.isOpened():
            myDir = QDir(myWin.recDir)
            now = QDateTime.currentDateTime()

            mkdir_cd(myDir, now.toString("yyyy"))
            mkdir_cd(myDir, now.toString("MM"))
            mkdir_cd(myDir, now.toString("dd"))

            myFile = myDir.filePath(now.toString("hh_mm_ss") + ".mp4")
            codec = VideoWriter.fourcc(*"mp4v")
            fps = 13
            frameSize = (width, height)

            myWin.writer.open(myFile, codec, fps, frameSize)

        else:
            myWin.writer.write(bgrMat)

    elif myWin.writer.isOpened():
        myWin.writer.release()

    if myWin.tabWidget.currentIndex() == 1:
        smallMat = resize(
            bgrMat,
            (myWin.videoLabel.width(), myWin.videoLabel.height()),
            interpolation=INTER_AREA,
        )
        myWin.videoLabel.setPixmap(cvMatToQPixmap(smallMat))


class AppMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.hkipc = HKIPcamera()
        self.writer = VideoWriter()

        self.trayIcon = QSystemTrayIcon(self)
        self.myTm = QTimer(self)
        self.recDir = str()

        self.isReady = False
        self.success = False
        self.reOpen = False

        self.setupUi(self)
        self._init()

    def __del__(self) -> None:
        self.hkipc.release()
        self.writer.release()

    def _init(self) -> None:
        self.ipAddress.setText("192.168.64.12")
        self.userName.setText("admin")
        self.password.setText("abcd1234")
        self.port.setText("8000")

        self.okButton.clicked.connect(self.okButton_clicked)
        self.browseTB.clicked.connect(self.browseTB_clicked)
        self.startButton.clicked.connect(self.startButton_clicked)
        self.stopButton.clicked.connect(self.stopButton_clicked)

        def quitAction():
            self.trayIcon.hide()
            QApplication.quit()

        icon_m = QMenu(self)
        icon_m.addAction(QAction("Show", self, triggered=self.show))
        icon_m.addAction(QAction("Hide", self, triggered=self.hide))
        icon_m.addSeparator()
        icon_m.addAction(QAction("Quit", self, triggered=quitAction))

        qSP = QStyle.StandardPixmap
        icon_i = self.style().standardIcon(qSP.SP_FileDialogListView)

        def activatedIcon(reason):
            qAR = QSystemTrayIcon.ActivationReason
            if reason in [qAR.Trigger, qAR.DoubleClick]:
                self.showNormal()

        self.setWindowIcon(icon_i)
        self.trayIcon.setIcon(icon_i)
        self.trayIcon.setContextMenu(icon_m)
        self.trayIcon.activated.connect(activatedIcon)
        self.trayIcon.show()

        def myTimer():
            now = QDateTime.currentDateTime()
            sec = DURATION * 60 - int(now.toString("ss"))
            self.myTm.stop()
            self.myTm.start((sec + 1) * 1000)
            self.reOpen = True

        self.myTm.timeout.connect(myTimer)
        self.myTm.start(10)

    def okButton_clicked(self) -> None:
        if self.success:
            self.hkipc.release()
            self.success = False

        if self.hkipc.login(
            self.ipAddress.text(),
            self.userName.text(),
            self.password.text(),
            int(self.port.text()),
        ):
            self.hkipc.setImageDataCallBack(f_ImageDataCallBack, self)
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
        if self.isReady:
            QMessageBox.about(self, "Record process", "Already started")
        elif QFileInfo(self.folder.text()).isDir():
            self.recDir = self.folder.text()
            self.isReady = True
            QMessageBox.information(
                self, "Record process", "Success\nRecording started"
            )
        else:
            QMessageBox.warning(self, "Record process", "Error\nInvalid folder")

    def stopButton_clicked(self) -> None:
        if self.isReady:
            self.isReady = False
            QMessageBox.information(
                self, "Record process", "Success\nRecording stopped"
            )
        else:
            QMessageBox.warning(self, "Record process", "Error\nNothing to stop")


if __name__ == "__main__":
    app = QApplication(sys_argv)
    win = AppMainWindow()
    win.show()
    sys_exit(app.exec())
