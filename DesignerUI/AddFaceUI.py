# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFace.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_containAddFaceScreen(object):
    def setupUi(self, Frame_containAddFaceScreen):
        Frame_containAddFaceScreen.setObjectName("Frame_containAddFaceScreen")
        Frame_containAddFaceScreen.resize(800, 429)
        Frame_containAddFaceScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame_containAddFaceScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame = QtWidgets.QFrame(Frame_containAddFaceScreen)
        self.frame.setGeometry(QtCore.QRect(8, 6, 785, 417))
        self.frame.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius:7px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_forShowCamera = QtWidgets.QLabel(self.frame)
        self.label_forShowCamera.setGeometry(QtCore.QRect(20, 16, 529, 309))
        self.label_forShowCamera.setText("")
        self.label_forShowCamera.setObjectName("label_forShowCamera")
        self.label_nhinVaoCamera = QtWidgets.QLabel(self.frame)
        self.label_nhinVaoCamera.setGeometry(QtCore.QRect(84, 354, 375, 49))
        self.label_nhinVaoCamera.setStyleSheet("font: 75 bold 14pt \"Ubuntu\";")
        self.label_nhinVaoCamera.setObjectName("label_nhinVaoCamera")
        self.label_forShowTimeCountdown = QtWidgets.QLabel(self.frame)
        self.label_forShowTimeCountdown.setGeometry(QtCore.QRect(634, 120, 73, 123))
        self.label_forShowTimeCountdown.setStyleSheet("font: 57 bold 80pt \"Ubuntu\";\n"
"color: rgb(0, 170, 127);")
        self.label_forShowTimeCountdown.setObjectName("label_forShowTimeCountdown")

        self.retranslateUi(Frame_containAddFaceScreen)
        QtCore.QMetaObject.connectSlotsByName(Frame_containAddFaceScreen)

    def retranslateUi(self, Frame_containAddFaceScreen):
        _translate = QtCore.QCoreApplication.translate
        Frame_containAddFaceScreen.setWindowTitle(_translate("Frame_containAddFaceScreen", "Frame"))
        self.label_nhinVaoCamera.setText(_translate("Frame_containAddFaceScreen", "VUI LÒNG NHÌN THẲNG VÀO CAMERA"))
        self.label_forShowTimeCountdown.setText(_translate("Frame_containAddFaceScreen", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_containAddFaceScreen = QtWidgets.QFrame()
    ui = Ui_Frame_containAddFaceScreen()
    ui.setupUi(Frame_containAddFaceScreen)
    Frame_containAddFaceScreen.show()
    sys.exit(app.exec_())
