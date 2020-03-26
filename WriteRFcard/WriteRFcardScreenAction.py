from WriteRFcard.WriteRFcardScreenUi   import Ui_Frame_containWriteIDcardScreen
from PyQt5          import QtCore, QtGui
from PyQt5.QtCore   import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty, QSize
from PyQt5          import QtWidgets
import json
from WriteRFcard.ControlRFIDmodule    import ControlRFIDmudule

class WriteRFcardAction(QObject, Ui_Frame_containWriteIDcardScreen):
    SignalWriteToRFcardSuccessfully = pyqtSignal()

    def __init__(self, frameContain):
        QObject.__init__(self)
        Ui_Frame_containWriteIDcardScreen.__init__(self)
        self.frameContainCurrentStep = frameContain
        self.frameContainCurrentStep.show()
        self.setupUi(frameContain)
        self.controlRFmoduleObj = ControlRFIDmudule()
        self.controlRFmoduleObj.SignalWriteToCardSuccessfully.connect(self.WriteCardSuccessFully)
        self.label.setPixmap(QtGui.QPixmap("icon/putRFcardIcon400.png"))

    def StopWriteToCard(self):
        self.controlRFmoduleObj.StopWriteIDcardNumberToRFcard()

    def WriteIDcardNumberToRFcard(self, number):
        self.label_showNotify.setStyleSheet("font: 57 bold 28pt 'Ubuntu';color: rgb(193, 0, 0);")
        self.label_showNotify.setText("Vui đặt thẻ lên thiết bị")
        if(type(number) is str):
            numberDict = json.loads(number)
            self.controlRFmoduleObj.SetIDcarNumberToWriteToRFcard(numberDict["number"])
        self.controlRFmoduleObj.StartWriteIDcardNumberToRFcard()

    def WriteCardSuccessFully(self):
        self.label_showNotify.setStyleSheet("font: 57 bold 28pt 'Ubuntu';color: rgb(0, 193, 0);")
        self.label_showNotify.setText("Ghi thành công")
        self.SignalWriteToRFcardSuccessfully.emit()

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
    
    
