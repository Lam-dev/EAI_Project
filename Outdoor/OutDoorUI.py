# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutDoor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(402, 271)
        Frame.setStyleSheet("background-color: rgb(188, 188, 188);")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineEdit_inputNumber = QtWidgets.QLineEdit(Frame)
        self.lineEdit_inputNumber.setGeometry(QtCore.QRect(96, 34, 293, 45))
        self.lineEdit_inputNumber.setObjectName("lineEdit_inputNumber")
        self.pushbutton_exit = QtWidgets.QPushButton(Frame)
        self.pushbutton_exit.setGeometry(QtCore.QRect(48, 204, 99, 27))
        self.pushbutton_exit.setObjectName("pushbutton_exit")
        self.pushButtonEnter = QtWidgets.QPushButton(Frame)
        self.pushButtonEnter.setGeometry(QtCore.QRect(236, 202, 99, 27))
        self.pushButtonEnter.setObjectName("pushButtonEnter")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(12, 40, 45, 39))
        self.label.setObjectName("label")
        self.lineEdit_inputPort = QtWidgets.QLineEdit(Frame)
        self.lineEdit_inputPort.setGeometry(QtCore.QRect(96, 104, 293, 45))
        self.lineEdit_inputPort.setObjectName("lineEdit_inputPort")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(14, 106, 45, 39))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushbutton_exit.setText(_translate("Frame", "Hủy"))
        self.pushButtonEnter.setText(_translate("Frame", "Xác nhận"))
        self.label.setText(_translate("Frame", "IP"))
        self.label_2.setText(_translate("Frame", "PORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
