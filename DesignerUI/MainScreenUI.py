# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_containMainWindow(object):
    def setupUi(self, Frame_containMainWindow):
        Frame_containMainWindow.setObjectName("Frame_containMainWindow")
        Frame_containMainWindow.resize(800, 480)
        Frame_containMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        Frame_containMainWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame_containMainWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containLogoAndDeviceName = QtWidgets.QFrame(Frame_containMainWindow)
        self.frame_containLogoAndDeviceName.setGeometry(QtCore.QRect(0, 0, 800, 50))
        self.frame_containLogoAndDeviceName.setStyleSheet("background-color: rgb(150, 220, 170);")
        self.frame_containLogoAndDeviceName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containLogoAndDeviceName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containLogoAndDeviceName.setObjectName("frame_containLogoAndDeviceName")
        self.label_centerName = QtWidgets.QLabel(self.frame_containLogoAndDeviceName)
        self.label_centerName.setGeometry(QtCore.QRect(78, 2, 577, 23))
        self.label_centerName.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 bold 13pt \"Ubuntu\";")
        self.label_centerName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_centerName.setObjectName("label_centerName")
        self.label_logo = QtWidgets.QLabel(self.frame_containLogoAndDeviceName)
        self.label_logo.setGeometry(QtCore.QRect(660, 6, 139, 37))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../../Desktop/EcotekProject/TheoryFaceRecognition/icon/iconEcotek.png"))
        self.label_logo.setObjectName("label_logo")
        self.pushButton_settingButton = QtWidgets.QPushButton(self.frame_containLogoAndDeviceName)
        self.pushButton_settingButton.setGeometry(QtCore.QRect(6, 0, 57, 49))
        self.pushButton_settingButton.setStyleSheet("border-style:solid;\n"
"border-radius:5px;")
        self.pushButton_settingButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_settingButton.setIcon(icon)
        self.pushButton_settingButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_settingButton.setObjectName("pushButton_settingButton")
        self.label_deviceName = QtWidgets.QLabel(self.frame_containLogoAndDeviceName)
        self.label_deviceName.setGeometry(QtCore.QRect(76, 28, 583, 21))
        self.label_deviceName.setStyleSheet("color: rgb(160, 0, 0);\n"
"font: 75 bold 14pt \"Ubuntu\";")
        self.label_deviceName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_deviceName.setObjectName("label_deviceName")
        self.frame = QtWidgets.QFrame(Frame_containMainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 50, 800, 429))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Frame_containMainWindow)
        QtCore.QMetaObject.connectSlotsByName(Frame_containMainWindow)

    def retranslateUi(self, Frame_containMainWindow):
        _translate = QtCore.QCoreApplication.translate
        Frame_containMainWindow.setWindowTitle(_translate("Frame_containMainWindow", "Frame"))
        self.label_centerName.setText(_translate("Frame_containMainWindow", "CÔNG TY CỔ PHẦN CÔNG NGHỆ KỸ THUẬT ECOTEK"))
        self.label_deviceName.setText(_translate("Frame_containMainWindow", "Thiết bị lấy mẫu vân tay, khuôn mặt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_containMainWindow = QtWidgets.QFrame()
    ui = Ui_Frame_containMainWindow()
    ui.setupUi(Frame_containMainWindow)
    Frame_containMainWindow.show()
    sys.exit(app.exec_())
