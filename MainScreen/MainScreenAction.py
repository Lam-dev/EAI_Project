from MainScreen.MainScreenUI     import Ui_Frame_containMainWindow
from AddFace.AddFaceAction       import AddFaceScreen
from ShowInfomation.ShowInfomationAction   import ShowInfoScreen
from AddFGP.AddFGPaction         import AddFGPscreen         
from SocketConnect.SocketClient  import SocketClient
from PyQt5          import QtCore, QtGui
from PyQt5.QtCore   import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty, QSize
from PyQt5          import QtWidgets
import json

class MainScreen(QObject, Ui_Frame_containMainWindow):
    def __init__(self, frameContainMainScreen):
        QObject.__init__(self)
        Ui_Frame_containMainWindow.__init__(self)

        self.setupUi(frameContainMainScreen)
        self.label_logo.setPixmap(QtGui.QPixmap("icon/iconEcotek.png"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_shutdown.setIcon(icon)
        self.pushButton_shutdown.setIconSize(QtCore.QSize(40, 40))
        self.frameContainShowInfo = QtWidgets.QFrame(self.frame)
        self.frameContainShowInfo.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.showInfoScreenObj = ShowInfoScreen(self.frameContainShowInfo)

        self.frameContainAddFace = QtWidgets.QFrame(self.frame)
        self.frameContainAddFace.setGeometry(QtCore.QRect(self.frame.width(), 0, 0, 0))
        self.addFaceScreenObj = AddFaceScreen(self.frameContainAddFace)

        self.frameContainAddFGP = QtWidgets.QFrame(self.frame)
        self.frameContainAddFGP.setGeometry(QtCore.QRect(self.frame.width(), 0, 0, 0))
        self.addFGPscreenObj = AddFGPscreen(self.frameContainAddFGP)


        self.currentStep = 1

        self.socketObj = SocketClient()
        self.socketObj.processReciptDataObj.SignalGoToAddFGP.connect(self.GoToAddFGPscreen)
        self.socketObj.processReciptDataObj.SignalGoToAddFace.connect(self.GoToAddFaceScreen)
        self.socketObj.processReciptDataObj.SignalShowInformation.connect(self.GoToShowInfomation)

        self.addFGPscreenObj.SignalSendImageToServer.connect(self.socketObj.SendFingerImage)
        self.addFGPscreenObj.SignalSendFGPGetToServer.connect(self.socketObj.SendFingerFeature)

        self.addFaceScreenObj.SignalPictureTaked.connect(self.socketObj.SendTakedImage)

    def GoToAddFGPscreen(self, strMessage):
        if(self.currentStep == 1):
            self.addFGPscreenObj.ShowStepStudentInformationAnim(self.frameContainShowInfo)
            self.currentStep = 2
            self.addFGPscreenObj.ListFingerNeedAdd(strMessage)
            self.addFGPscreenObj.GetFGP()

        elif(self.currentStep == 3):
            self.addFGPscreenObj.ShowStepStudentInformationAnim(self.frameContainAddFace)
            self.currentStep = 2
            #self.addFaceScreenObj.cameraObj.StopReadImage()
            self.addFaceScreenObj.StopTakePicture()
            self.addFGPscreenObj.ListFingerNeedAdd(strMessage)
            self.addFGPscreenObj.GetFGP()
        elif(self.currentStep == 2):
            self.addFGPscreenObj.ListFingerNeedAdd(strMessage)
            self.addFGPscreenObj.GetFGP()
        
    def GoToAddFaceScreen(self):
        if(self.currentStep == 2):
            self.addFaceScreenObj.ShowStepStudentInformationAnim(self.frameContainAddFGP)
            self.addFGPscreenObj.StopAll()
            self.currentStep = 3
        
        if(self.currentStep == 1):
            self.addFaceScreenObj.ShowStepStudentInformationAnim(self.frameContainShowInfo)
            self.currentStep = 3 
        
        if(self.currentStep == 3):
            self.addFaceScreenObj.RetakePicture()

    def GoToShowInfomation(self, inforString):
        self.showInfoScreenObj.ShowInformation(inforString)
        if(self.currentStep == 2):
            self.showInfoScreenObj.ShowStepStudentInformationAnim(self.frameContainAddFGP)
            self.addFGPscreenObj.StopAll()
            self.currentStep = 1

        if(self.currentStep == 3):
            self.showInfoScreenObj.ShowStepStudentInformationAnim(self.frameContainAddFace)
            self.addFaceScreenObj.StopTakePicture()
            self.currentStep = 1
            