from ShowInfomation.ShowInfomationUI   import Ui_Frame
from PyQt5          import QtCore, QtGui
from PyQt5.QtCore   import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty, QSize
from PyQt5          import QtWidgets
import json
from SocketConnect.FTPclient   import FTPclient

class ShowInfoScreen(QObject, Ui_Frame):
    def __init__(self, frameContain):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        self.frameContainCurrentStep = frameContain
        self.frameContainCurrentStep.show()
        self.setupUi(frameContain)
        self.label_forShowImage.setPixmap(QtGui.QPixmap("icon/iconImageRepresent.png"))
        self.ftpObj = FTPclient()

    def ShowInformation(self, infoObj):
        inforDict = json.loads(infoObj)
        self.label_forShowName.setText(inforDict["ten"])
        self.label_forShowDateOfBird.setText(inforDict["ngaySinh"])
        self.label_forShowIDcardNumber.setText(inforDict["cmt"])
        self.label_forShowComeFrom.setText(inforDict["que"])
        self.label_forShowIDcardNumber.setText(inforDict["sdt"])
        self.label_forShowEmail.setText(inforDict["email"])
        # self.ftpObj.GetFileFromFTPserver("IDimage.jpg")


    def ShowStepStudentInformationAnim(self, frameOfPreStep):

        self.preStepGoToLeftAnim = QPropertyAnimation(frameOfPreStep, b"geometry")
        self.preStepGoToLeftAnim.setDuration(300)
        self.preStepGoToLeftAnim.setStartValue(QtCore.QRect(0 , frameOfPreStep.y() , frameOfPreStep.width(), frameOfPreStep.height()))
        self.preStepGoToLeftAnim.setEndValue(QtCore.QRect(0-frameOfPreStep.width() , frameOfPreStep.y(), frameOfPreStep.width(), frameOfPreStep.height()))
        
        self.currentStepToLeftAnim = QPropertyAnimation(self.frameContainCurrentStep, b"geometry")
        self.currentStepToLeftAnim.setDuration(300)
        self.currentStepToLeftAnim.setStartValue(QtCore.QRect(frameOfPreStep.width() , self.frameContainCurrentStep.y() , self.frameContainCurrentStep.width(), self.frameContainCurrentStep.height()))
        self.currentStepToLeftAnim.setEndValue(QtCore.QRect(0 , self.frameContainCurrentStep.y(), self.frameContainCurrentStep.width(), self.frameContainCurrentStep.height()))
        
        self.preStepGoToLeftAnim.start()
        self.currentStepToLeftAnim.start()
    
    