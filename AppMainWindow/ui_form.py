# Form implementation generated from reading ui file '/home/user/Documents/qt-projects/ip-cam/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 511))
        self.tabWidget.setStyleSheet("font: 14pt;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 60, 281, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ipAddress = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.ipAddress.setText("")
        self.ipAddress.setObjectName("ipAddress")
        self.gridLayout.addWidget(self.ipAddress, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.userName = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.userName.setText("")
        self.userName.setObjectName("userName")
        self.gridLayout.addWidget(self.userName, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.password.setText("")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.port.setText("")
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.videoLabel = QtWidgets.QLabel(parent=self.tab_2)
        self.videoLabel.setGeometry(QtCore.QRect(20, 20, 750, 425))
        self.videoLabel.setStyleSheet("background: rgb(154, 153, 150);")
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 110, 351, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.folder = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.folder.setObjectName("folder")
        self.gridLayout_2.addWidget(self.folder, 0, 1, 1, 2)
        self.browseTB = QtWidgets.QToolButton(parent=self.layoutWidget1)
        self.browseTB.setObjectName("browseTB")
        self.gridLayout_2.addWidget(self.browseTB, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 2)
        self.duration = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.duration.setMinimum(1)
        self.duration.setMaximum(60)
        self.duration.setObjectName("duration")
        self.gridLayout_2.addWidget(self.duration, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(28, 18, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 2, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recorder"))
        self.label.setText(_translate("MainWindow", "Ip address:"))
        self.label_2.setText(_translate("MainWindow", "User name:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Port:"))
        self.okButton.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Live Stream"))
        self.label_5.setText(_translate("MainWindow", "Folder:"))
        self.browseTB.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Duration (minutes):"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Record"))
