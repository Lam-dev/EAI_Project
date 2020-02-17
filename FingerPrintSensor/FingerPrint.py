from    FingerPrintSensor.FingerprintLib    import PyFingerprint
from    PyQt5.QtCore       import QRect, QPropertyAnimation, QTimer, pyqtSignal, pyqtSlot, QObject
import  time
from    PIL import Image
import  _thread
import  threading
import  os
from    datetime import datetime


class Fingerprint(QObject):
    SignalNewFGPadded = pyqtSignal(int, list)
    SignalRecognizedFGP = pyqtSignal(int)
    SignalFGPnotFind = pyqtSignal()
    SignalHandPushed = pyqtSignal()
    SignalDowloadedImage = pyqtSignal(str)
    SignalFGPget = pyqtSignal(str)
    SignalFGPputOnIsTheSame = pyqtSignal()

    def __init__(self, port = '/dev/ttyACM0', baudRate = 57600, address = 0xFFFFFFFF, password = 0xFFFFFFFF):
        super().__init__()
        self.port = port
        self.baudRate = baudRate
        self.address = address
        self.password = password
        try:
            self.fingerprintObj = PyFingerprint(port, baudRate, address, password)
            # self.fingerprintObj.verifyPassword()
        except:
            self.fingerprintObj = False
        
        self.timerDownloadFGPimage = QTimer()
        self.timerDownloadFGPimage.timeout.connect(self.ThreadDownloadFGPimage)

        self.timerGetFGPfeature = QTimer()
        self.timerGetFGPfeature.timeout.connect(self.ThreadGetFGPfeature)

        self.lstIDvaVanTay = []
        self.viTriDaChonChuaLuu = []
        self.FlagFGPfree = True
        self.__FlagLockFGPsensor = False

    def ThreadGetFGPfeature(self):
        thread = threading.Thread(target = self.GetFGPfeature)
        thread.start()
    
    def StartGetFGP(self):
        self.timerGetFGPfeature.start(1000)
    
    def StopGetFGP(self):
        self.timerGetFGPfeature.stop()

    # def StartDownloadImage(self):
    #     self.timerDownloadFGPimage.start(1000)
    
    # def StopDownloadImage(self):
    #     self.timerDownloadFGPimage.stop()

    def ThreadDownloadFGPimage(self):
        if(self.FlagFGPfree):
            self.FlagFGPfree = False
            thread = threading.Thread(target = self.GetFGPfeature, args=(), daemon= True)
            thread.start()

    def DownloadFGPimage(self):
        try:
            if(type(self.fingerprintObj) is not bool):
                if(self.fingerprintObj.readImage()):
                    imageName = datetime.now().strftime("%H_%M_%S")+".bmp"
                    imageDir = os.getcwd() + "/" + imageName
                    self.fingerprintObj.downloadImage(imageDir)
                    self.SignalDowloadedImage.emit(imageName)
            else:
                self.fingerprintObj = PyFingerprint(self.port, self.baudRate, self.address, self.password)
                self.fingerprintObj.verifyPassword()
        except:
            self.fingerprintObj = False
        self.FlagFGPfree = True        

    def ClearFGPfeatureSaveOnSensor(self):
        self.fingerprintObj.clearDatabase()

    def GetFGPfeature(self):
        if(self.__FlagLockFGPsensor):
            return
        self.__FlagLockFGPsensor = True
        try:
            if(type(self.fingerprintObj) is not bool):
                if(self.fingerprintObj.readImage()):
                    self.SignalHandPushed.emit()
                    self.fingerprintObj.convertImage(0x01)
                    theSame = self.fingerprintObj.searchTemplate()
                    if(theSame[0] == -1):
                        lstFGPfeature = self.fingerprintObj.downloadCharacteristics(0x01)
                        self.fingerprintObj.storeTemplate()
                        lstFGPfeatureStrElem = [str(elem) for elem in lstFGPfeature]
                        FGPfeatureString = ",".join(lstFGPfeatureStrElem)
                        self.SignalFGPget.emit(FGPfeatureString)
                        
                    else:
                        self.SignalFGPputOnIsTheSame.emit()
                            

            else:
                self.fingerprintObj = PyFingerprint(self.port, self.baudRate, self.address, self.password)
                self.fingerprintObj.verifyPassword()

        except:
            self.__FlagLockFGPsensor = False
            self.fingerprintObj = False
        self.__FlagLockFGPsensor = False
    

