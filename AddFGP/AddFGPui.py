# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFGPscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_ContainAddFGPscreen(object):
    def setupUi(self, Frame_ContainAddFGPscreen):
        Frame_ContainAddFGPscreen.setObjectName("Frame_ContainAddFGPscreen")
        Frame_ContainAddFGPscreen.resize(800, 429)
        Frame_ContainAddFGPscreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame_ContainAddFGPscreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame = QtWidgets.QFrame(Frame_ContainAddFGPscreen)
        self.frame.setGeometry(QtCore.QRect(8, 6, 785, 417))
        self.frame.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius:7px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_utTrai = QtWidgets.QLabel(self.frame)
        self.label_utTrai.setGeometry(QtCore.QRect(130, 16, 44, 270))
        self.label_utTrai.setText("")
        self.label_utTrai.setPixmap(QtGui.QPixmap("../icon/finger/utTraiTrang.png"))
        self.label_utTrai.setObjectName("label_utTrai")
        self.label_nhanTrai = QtWidgets.QLabel(self.frame)
        self.label_nhanTrai.setGeometry(QtCore.QRect(174, 14, 52, 270))
        self.label_nhanTrai.setText("")
        self.label_nhanTrai.setPixmap(QtGui.QPixmap("../icon/finger/nhanTraiTrang.png"))
        self.label_nhanTrai.setObjectName("label_nhanTrai")
        self.label_giuaTrai = QtWidgets.QLabel(self.frame)
        self.label_giuaTrai.setGeometry(QtCore.QRect(226, 14, 48, 270))
        self.label_giuaTrai.setText("")
        self.label_giuaTrai.setPixmap(QtGui.QPixmap("../icon/finger/giuaTraiTrang.png"))
        self.label_giuaTrai.setObjectName("label_giuaTrai")
        self.label_troTrai = QtWidgets.QLabel(self.frame)
        self.label_troTrai.setGeometry(QtCore.QRect(270, 14, 57, 270))
        self.label_troTrai.setText("")
        self.label_troTrai.setPixmap(QtGui.QPixmap("../icon/finger/troTraiTrang.png"))
        self.label_troTrai.setObjectName("label_troTrai")
        self.label_caiTrai = QtWidgets.QLabel(self.frame)
        self.label_caiTrai.setGeometry(QtCore.QRect(322, 14, 49, 270))
        self.label_caiTrai.setText("")
        self.label_caiTrai.setPixmap(QtGui.QPixmap("../icon/finger/caiTraiTrang.png"))
        self.label_caiTrai.setObjectName("label_caiTrai")
        self.label_troPhai = QtWidgets.QLabel(self.frame)
        self.label_troPhai.setGeometry(QtCore.QRect(438, 14, 52, 270))
        self.label_troPhai.setText("")
        self.label_troPhai.setPixmap(QtGui.QPixmap("../icon/fingerRight/troPhaiTrang.png"))
        self.label_troPhai.setObjectName("label_troPhai")
        self.label_giuaPhai = QtWidgets.QLabel(self.frame)
        self.label_giuaPhai.setGeometry(QtCore.QRect(490, 14, 48, 270))
        self.label_giuaPhai.setStyleSheet("")
        self.label_giuaPhai.setText("")
        self.label_giuaPhai.setPixmap(QtGui.QPixmap("../icon/fingerRight/giuaPhaiTrang.png"))
        self.label_giuaPhai.setObjectName("label_giuaPhai")
        self.label_caiPhai = QtWidgets.QLabel(self.frame)
        self.label_caiPhai.setGeometry(QtCore.QRect(386, 14, 53, 270))
        self.label_caiPhai.setText("")
        self.label_caiPhai.setPixmap(QtGui.QPixmap("../icon/fingerRight/caiPhaiTrang.png"))
        self.label_caiPhai.setObjectName("label_caiPhai")
        self.label_utPhai = QtWidgets.QLabel(self.frame)
        self.label_utPhai.setGeometry(QtCore.QRect(590, 16, 44, 270))
        self.label_utPhai.setText("")
        self.label_utPhai.setPixmap(QtGui.QPixmap("../icon/fingerRight/utPhaiTrang.png"))
        self.label_utPhai.setObjectName("label_utPhai")
        self.label_nhanPhai = QtWidgets.QLabel(self.frame)
        self.label_nhanPhai.setGeometry(QtCore.QRect(538, 14, 52, 270))
        self.label_nhanPhai.setText("")
        self.label_nhanPhai.setPixmap(QtGui.QPixmap("../icon/fingerRight/nhanPhaiTrang.png"))
        self.label_nhanPhai.setObjectName("label_nhanPhai")
        self.frame_containAnoument = QtWidgets.QFrame(self.frame)
        self.frame_containAnoument.setGeometry(QtCore.QRect(72, 316, 641, 80))
        self.frame_containAnoument.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containAnoument.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containAnoument.setObjectName("frame_containAnoument")
        self.label_forShowNotify = QtWidgets.QLabel(self.frame_containAnoument)
        self.label_forShowNotify.setGeometry(QtCore.QRect(36, 16, 563, 43))
        self.label_forShowNotify.setStyleSheet("font: 75 bold 16pt \"Ubuntu\";")
        self.label_forShowNotify.setAlignment(QtCore.Qt.AlignCenter)
        self.label_forShowNotify.setObjectName("label_forShowNotify")

        self.retranslateUi(Frame_ContainAddFGPscreen)
        QtCore.QMetaObject.connectSlotsByName(Frame_ContainAddFGPscreen)

    def retranslateUi(self, Frame_ContainAddFGPscreen):
        _translate = QtCore.QCoreApplication.translate
        Frame_ContainAddFGPscreen.setWindowTitle(_translate("Frame_ContainAddFGPscreen", "Frame"))
        self.label_forShowNotify.setText(_translate("Frame_ContainAddFGPscreen", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_ContainAddFGPscreen = QtWidgets.QFrame()
    ui = Ui_Frame_ContainAddFGPscreen()
    ui.setupUi(Frame_ContainAddFGPscreen)
    Frame_ContainAddFGPscreen.show()
    sys.exit(app.exec_())
