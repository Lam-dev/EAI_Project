from MainScreen.MainScreenUI     import Ui_Frame_containMainWindow
from AddFace.AddFaceAction       import AddFaceScreen
from ShowInfomation.ShowInfomationAction   import ShowInfoScreen
from AddFGP.AddFGPaction         import AddFGPscreen         
from SocketConnect.SocketClient  import SocketClient
from PyQt5          import QtCore, QtGui
from PyQt5.QtCore   import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty, QSize
from PyQt5          import QtWidgets
import json
from    KeyBoard.KeyBoard                       import KeyBoard
from Outdoor.OutDoor   import OutDoor
from SettingScreen.SettingScreen    import SettingScreen
from    CheckVersionScreen.CheckVersion         import CheckUpdate
from    GetSettingFromJSON    import GetSetting 

try:
    NAME_SETTING_DICT = GetSetting.GetPersionalSetting()
    NAME_CENTER = NAME_SETTING_DICT["scName"]
    NAME_DEVICE = NAME_SETTING_DICT["cenName"]
except:
    NAME_CENTER = ""
    NAME_DEVICE = ""

class MainScreen(QObject, Ui_Frame_containMainWindow):
    SignalCloseApp = pyqtSignal()
    SignalShutdown = pyqtSignal()
    SignalGoToSetting = pyqtSignal()
    SignalSettingScreenHiden = pyqtSignal()
    SignalUpdateVersion = pyqtSignal()
    SignalCloseELT = pyqtSignal()
    

    def __init__(self, frameContainMainScreen):
        QObject.__init__(self)
        Ui_Frame_containMainWindow.__init__(self)

        self.setupUi(frameContainMainScreen)
        self.frameContain = frameContainMainScreen
        self.label_logo.setPixmap(QtGui.QPixmap("icon/iconEcotek.png"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/settingIcon40.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_settingButton.setIcon(icon)
        self.pushButton_settingButton.setIconSize(QtCore.QSize(40, 40))

        self.pushButton_settingButton.clicked.connect(self.ShowSettingScreen)

        self.frameContainShowInfo = QtWidgets.QFrame(self.frame)
        self.frameContainShowInfo.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.showInfoScreenObj = ShowInfoScreen(self.frameContainShowInfo)

        self.frameContainAddFace = QtWidgets.QFrame(self.frame)
        self.frameContainAddFace.setGeometry(QtCore.QRect(self.frame.width(), 0, 0, 0))
        self.addFaceScreenObj = AddFaceScreen(self.frameContainAddFace)

        self.frameContainAddFGP = QtWidgets.QFrame(self.frame)
        self.frameContainAddFGP.setGeometry(QtCore.QRect(self.frame.width(), 0, 0, 0))
        self.addFGPscreenObj = AddFGPscreen(self.frameContainAddFGP)

        self.label_logo.mouseDoubleClickEvent = lambda event: self.__OpenOutdoor()

        self.currentStep = 1

        self.socketObj = SocketClient()
        self.socketObj.processReciptDataObj.SignalGoToAddFGP.connect(self.GoToAddFGPscreen)
        self.socketObj.processReciptDataObj.SignalGoToAddFace.connect(self.GoToAddFaceScreen)
        self.socketObj.processReciptDataObj.SignalShowInformation.connect(self.GoToShowInfomation)

        self.addFGPscreenObj.SignalSendImageToServer.connect(self.socketObj.SendFingerImage)
        self.addFGPscreenObj.SignalSendFGPGetToServer.connect(self.socketObj.SendFingerFeature)

        self.addFaceScreenObj.SignalPictureTaked.connect(self.socketObj.SendTakedImage)

        self.label_centerName.setText(NAME_CENTER)
        self.label_deviceName.setText(self.__ConvertStringToUTF8String(NAME_DEVICE))

        self.__keyBoardOpened = False

    def __ShowKeyBoard(self, widgetTakeInput):
        if(not self.__keyBoardOpened):
            self.frameContainKeyBoard = QtWidgets.QFrame(self.frameContain)
            self.frameContainKeyBoard.setGeometry(0, 0, 480, 220)
            self.keyBoardObject = KeyBoard(widgetTakeInput, self.frameContainKeyBoard)
            self.keyBoardObject.CloseKeyBoardSignal.connect(self.__CloseKeyBoard)
            self.__keyBoardOpened = True

    def __CloseKeyBoard(self):
        self.frameContainKeyBoard.deleteLater()
        self.keyBoardObject.deleteLater()
        self.__keyBoardOpened = False

    def __ConvertStringToUTF8String(self, string):
        x = []
        for elem in string:
            x.append(ord(elem))
        return(bytes(x).decode("utf8", "ignore"))

    def SaveAndChangeSetting(self, settingDict):
        self.label_cty.setText(self.__ConvertStringToUTF8String(settingDict["scName"]))
        self.label_cty_2.setText(self.__ConvertStringToUTF8String(settingDict["cenName"]))

    def ShowSettingScreen(self):
        self.settingScreenShadow = QtWidgets.QFrame(self.frameContain)
        self.settingScreenShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.settingScreenShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.settingScreenShadow.mousePressEvent = lambda event: self.__HideSettingScreen()
        self.frameContainUpdateScreen = QtWidgets.QFrame(self.settingScreenShadow)
        self.frameContainUpdateScreen.mousePressEvent = lambda event: self.__EventDontUse()
        self.settingScreenObj = SettingScreen(self.frameContainUpdateScreen)
        # self.settingScreenObj.SignalModifyFaceMark.connect(self.__ModifyFaceMark)
        # self.settingScreenObj.SignalModifyFRthreshold.connect(self.__ModifyFRthreadhold)
        # self.settingScreenObj.SignalModifyImageQuality.connect(self.__SignalModifyImageQuality)
        self.settingScreenObj.RequestOpenKeyBoard.connect(self.__ShowKeyBoard)
        self.settingScreenObj.SignalConnectNewFTPserver.connect(self.socketObj.ConnectNewFTP)
        self.settingScreenObj.SignalConnectNewServer.connect(self.socketObj.SocketConnectNewServer)
        # self.settingScreenObj.RequestOpenDatabaseScreen.connect(self.OpenDatabaseManagerScreen)
        # self.settingScreenObj.SignalOpenHideSettingScreen.connect(self.OpenHideSettingScreen)
        # self.settingScreenObj.SignalCleanFGPsensor.connect(self.SignalCleanFGPsensor.emit)
        self.settingScreenObj.SignalCheckVersion.connect(self.ShowVersionCheckScreen)
        self.settingScreenObj.SignalShutdown.connect(self.SignalShutdown.emit)
        # self.settingScreenObj.SignalDeleteAllData.connect(self.SignalDeleteAllData.emit)
        
        self.settingScreenShadow.show()
        self.settingScreenShadow.raise_()
    
    def __EventDontUse(self):
        pass

    def __HideSettingScreen(self):
        self.settingScreenObj.SaveSetting()
        self.settingScreenShadow.hide()
        self.settingScreenShadow.deleteLater()
        self.settingScreenObj.deleteLater()
        self.SignalSettingScreenHiden.emit()

    def __SetIP(self):
        # self.outdoorScreenShadow = QtWidgets.QFrame(self.frameContain)
        # self.outdoorScreenShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        # self.outdoorScreenShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        # self.frameContainOutdoor = QtWidgets.QFrame(self.outdoorScreenShadow)
        # self.outdoorObj = OutDoor(self.frameContainOutdoor)
        # self.outdoorScreenShadow.raise_()
        # self.outdoorScreenShadow.show()
        # self.outdoorObj.SignalHideExitScreen.connect(self.__HideOutdoorScreen)
        # self.outdoorObj.SignalGoToDesktop.connect(self.__GoToDesktop)
        pass

    def __HideOutdoorScreen(self):
        self.outdoorScreenShadow.hide()
        self.outdoorScreenShadow.deleteLater()


    def __OpenOutdoor(self):
        self.SignalCloseApp.emit()

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
    
    def ShowVersionCheckScreen(self):
        
        self.checkVersionShadow = QtWidgets.QFrame(self.frameContain)
        self.checkVersionShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.checkVersionShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frameContainCheckVersionScreen = QtWidgets.QFrame(self.checkVersionShadow)
        self.checkVersionScreenObj = CheckUpdate(self.frameContainCheckVersionScreen)
        self.checkVersionScreenObj.SignalUpdateVersion.connect(self.SignalCloseELT.emit)
        self.checkVersionScreenObj.SignalRequestCloseScreen.connect(self.CloseCheckVersionScreen)
        self.checkVersionScreenObj.SignalServerSettingForDevice.connect(self.SaveAndChangeSetting)
        self.checkVersionShadow.raise_()
        self.checkVersionShadow.show()

    def CloseCheckVersionScreen(self):
        self.checkVersionShadow.hide()
        self.checkVersionShadow.deleteLater()

    def SaveAndChangeSetting(self):
        pass
    