# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowInfomationScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 429)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2 = QtWidgets.QFrame(Frame)
        self.frame_2.setGeometry(QtCore.QRect(6, 6, 273, 415))
        self.frame_2.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius:7px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_forShowImage = QtWidgets.QLabel(self.frame_2)
        self.label_forShowImage.setGeometry(QtCore.QRect(32, 68, 209, 261))
        self.label_forShowImage.setText("")
        self.label_forShowImage.setPixmap(QtGui.QPixmap("../../.designer/icon/iconImageRepresent.png"))
        self.label_forShowImage.setObjectName("label_forShowImage")
        self.frame_3 = QtWidgets.QFrame(Frame)
        self.frame_3.setGeometry(QtCore.QRect(288, 6, 505, 415))
        self.frame_3.setStyleSheet("background-color: rgb(191, 191, 191);\n"
"border-radius:7px")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_VuiLongKiemTraVV = QtWidgets.QLabel(self.frame_3)
        self.label_VuiLongKiemTraVV.setGeometry(QtCore.QRect(8, 6, 493, 39))
        self.label_VuiLongKiemTraVV.setStyleSheet("font: 57 bold 12pt \"Ubuntu\";")
        self.label_VuiLongKiemTraVV.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VuiLongKiemTraVV.setObjectName("label_VuiLongKiemTraVV")
        self.label_hayBaoChoNhanVienVV = QtWidgets.QLabel(self.frame_3)
        self.label_hayBaoChoNhanVienVV.setGeometry(QtCore.QRect(50, 40, 399, 27))
        self.label_hayBaoChoNhanVienVV.setStyleSheet("font: 57 12pt \"Ubuntu\";\n"
"color: rgb(255, 0, 0);")
        self.label_hayBaoChoNhanVienVV.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hayBaoChoNhanVienVV.setObjectName("label_hayBaoChoNhanVienVV")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(4, 80, 497, 327))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:7px;\n"
"border-width:1px;\n"
"border-color: rgb(173, 173, 173);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setGeometry(QtCore.QRect(0, 36, 497, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setGeometry(QtCore.QRect(0, 72, 497, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setGeometry(QtCore.QRect(0, 108, 497, 1))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_4)
        self.line_4.setGeometry(QtCore.QRect(0, 144, 497, 1))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_4)
        self.line_5.setGeometry(QtCore.QRect(0, 180, 497, 1))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame_4)
        self.line_6.setGeometry(QtCore.QRect(0, 216, 497, 1))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame_4)
        self.line_7.setGeometry(QtCore.QRect(0, 252, 497, 1))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_hoVaTen = QtWidgets.QLabel(self.frame_4)
        self.label_hoVaTen.setGeometry(QtCore.QRect(10, 10, 165, 21))
        self.label_hoVaTen.setStyleSheet("border-width: 0px")
        self.label_hoVaTen.setObjectName("label_hoVaTen")
        self.label_ngaySinh = QtWidgets.QLabel(self.frame_4)
        self.label_ngaySinh.setGeometry(QtCore.QRect(10, 46, 165, 21))
        self.label_ngaySinh.setStyleSheet("border-width: 0px")
        self.label_ngaySinh.setObjectName("label_ngaySinh")
        self.label_soCMTND = QtWidgets.QLabel(self.frame_4)
        self.label_soCMTND.setGeometry(QtCore.QRect(10, 80, 165, 21))
        self.label_soCMTND.setStyleSheet("border-width: 0px")
        self.label_soCMTND.setObjectName("label_soCMTND")
        self.label_ngayCap = QtWidgets.QLabel(self.frame_4)
        self.label_ngayCap.setGeometry(QtCore.QRect(10, 116, 111, 21))
        self.label_ngayCap.setStyleSheet("border-width: 0px")
        self.label_ngayCap.setObjectName("label_ngayCap")
        self.label_queQuan = QtWidgets.QLabel(self.frame_4)
        self.label_queQuan.setGeometry(QtCore.QRect(8, 190, 109, 21))
        self.label_queQuan.setStyleSheet("border-width: 0px")
        self.label_queQuan.setObjectName("label_queQuan")
        self.label_noiCap = QtWidgets.QLabel(self.frame_4)
        self.label_noiCap.setGeometry(QtCore.QRect(10, 154, 111, 21))
        self.label_noiCap.setStyleSheet("border-width: 0px")
        self.label_noiCap.setObjectName("label_noiCap")
        self.line_8 = QtWidgets.QFrame(self.frame_4)
        self.line_8.setGeometry(QtCore.QRect(-2, 288, 497, 1))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_soDienThoai = QtWidgets.QLabel(self.frame_4)
        self.label_soDienThoai.setGeometry(QtCore.QRect(8, 226, 195, 21))
        self.label_soDienThoai.setStyleSheet("border-width: 0px")
        self.label_soDienThoai.setObjectName("label_soDienThoai")
        self.label_email = QtWidgets.QLabel(self.frame_4)
        self.label_email.setGeometry(QtCore.QRect(10, 260, 195, 21))
        self.label_email.setStyleSheet("border-width: 0px")
        self.label_email.setObjectName("label_email")
        self.label_forShowName = QtWidgets.QLabel(self.frame_4)
        self.label_forShowName.setGeometry(QtCore.QRect(200, 8, 275, 21))
        self.label_forShowName.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowName.setText("")
        self.label_forShowName.setObjectName("label_forShowName")
        self.label_forShowDateOfBird = QtWidgets.QLabel(self.frame_4)
        self.label_forShowDateOfBird.setGeometry(QtCore.QRect(200, 44, 281, 21))
        self.label_forShowDateOfBird.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowDateOfBird.setText("")
        self.label_forShowDateOfBird.setObjectName("label_forShowDateOfBird")
        self.label_forShowIDcardNumber = QtWidgets.QLabel(self.frame_4)
        self.label_forShowIDcardNumber.setGeometry(QtCore.QRect(202, 82, 275, 21))
        self.label_forShowIDcardNumber.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowIDcardNumber.setText("")
        self.label_forShowIDcardNumber.setObjectName("label_forShowIDcardNumber")
        self.label_forShowDateOfIDcard = QtWidgets.QLabel(self.frame_4)
        self.label_forShowDateOfIDcard.setGeometry(QtCore.QRect(200, 116, 277, 21))
        self.label_forShowDateOfIDcard.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowDateOfIDcard.setText("")
        self.label_forShowDateOfIDcard.setObjectName("label_forShowDateOfIDcard")
        self.label_IDcardPlace = QtWidgets.QLabel(self.frame_4)
        self.label_IDcardPlace.setGeometry(QtCore.QRect(200, 150, 279, 21))
        self.label_IDcardPlace.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_IDcardPlace.setText("")
        self.label_IDcardPlace.setObjectName("label_IDcardPlace")
        self.label_forShowComeFrom = QtWidgets.QLabel(self.frame_4)
        self.label_forShowComeFrom.setGeometry(QtCore.QRect(202, 188, 283, 21))
        self.label_forShowComeFrom.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowComeFrom.setText("")
        self.label_forShowComeFrom.setObjectName("label_forShowComeFrom")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(200, 224, 285, 21))
        self.label.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_forShowEmail = QtWidgets.QLabel(self.frame_4)
        self.label_forShowEmail.setGeometry(QtCore.QRect(198, 260, 289, 21))
        self.label_forShowEmail.setStyleSheet("border-width: 0px;\n"
"font: 57 bold 12pt \"Ubuntu\";")
        self.label_forShowEmail.setText("")
        self.label_forShowEmail.setObjectName("label_forShowEmail")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_VuiLongKiemTraVV.setText(_translate("Frame", "VUI LÒNG KIỂM TRA CÁC THÔNG TIN CÁC NHÂN SAU"))
        self.label_hayBaoChoNhanVienVV.setText(_translate("Frame", "(Hãy thông báo cho nhân viên nếu phát hiện sai sót)"))
        self.label_hoVaTen.setText(_translate("Frame", "HỌ VÀ TÊN:"))
        self.label_ngaySinh.setText(_translate("Frame", "NGÀY SINH:"))
        self.label_soCMTND.setText(_translate("Frame", "SỐ CMTND:"))
        self.label_ngayCap.setText(_translate("Frame", "NGÀY CẤP:"))
        self.label_queQuan.setText(_translate("Frame", "QUÊ QUÁN:"))
        self.label_noiCap.setText(_translate("Frame", "NƠI CẤP:"))
        self.label_soDienThoai.setText(_translate("Frame", "SỐ ĐIỆN THOẠI LIÊN HỆ:"))
        self.label_email.setText(_translate("Frame", "EMAIL:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
