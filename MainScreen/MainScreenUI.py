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
        self.frame_containLogoAndDeviceName.setStyleSheet("background-color: rgb(100, 202, 150);")
        self.frame_containLogoAndDeviceName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containLogoAndDeviceName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containLogoAndDeviceName.setObjectName("frame_containLogoAndDeviceName")
        self.labe_thietBiLayMauVanTayVV = QtWidgets.QLabel(self.frame_containLogoAndDeviceName)
        self.labe_thietBiLayMauVanTayVV.setGeometry(QtCore.QRect(152, 4, 517, 35))
        self.labe_thietBiLayMauVanTayVV.setStyleSheet("font: 75 BOLD 16pt \"Ubuntu\";")
        self.labe_thietBiLayMauVanTayVV.setObjectName("labe_thietBiLayMauVanTayVV")
        self.label_logo = QtWidgets.QLabel(self.frame_containLogoAndDeviceName)
        self.label_logo.setGeometry(QtCore.QRect(680, 10, 99, 29))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../icon/logo_.png"))
        self.label_logo.setObjectName("label_logo")
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
        self.labe_thietBiLayMauVanTayVV.setText(_translate("Frame_containMainWindow", "THIẾT BỊ LẤY MẪU VÂN TAY VÀ KHUÔN MẶT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_containMainWindow = QtWidgets.QFrame()
    ui = Ui_Frame_containMainWindow()
    ui.setupUi(Frame_containMainWindow)
    Frame_containMainWindow.show()
    sys.exit(app.exec_())
