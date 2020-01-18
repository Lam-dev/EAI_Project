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

        self.lstIDvaVanTay = []
        self.viTriDaChonChuaLuu = []
        self.FlagFGPfree = True
    
    def StartDownloadImage(self):
        self.timerDownloadFGPimage.start(1000)
    
    def StopDownloadImage(self):
        self.timerDownloadFGPimage.stop()

    def ThreadDownloadFGPimage(self):
        if(self.FlagFGPfree):
            self.FlagFGPfree = False
            thread = threading.Thread(target = self.DownloadFGPimage, args=(), daemon= True)
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
    def ThreadLayVanTayDangNhap(self):
        if(self.FlagFGPfree):
            self.FlagFGPfree = False
            thread = threading.Thread(target = self.LayVanTayDangNhap, args=(), daemon= True)
            thread.start()
    
    def LayVanTayDangNhap(self):
        
        try:
            if(self.fingerprintObj.readImage()):
                self.fingerprintObj.convertImage(0x01)
                ketqua = self.fingerprintObj.searchTemplate()
                if(len(ketqua) == 2):
                    for idVaVanTay in self.lstIDvaVanTay:
                        if(idVaVanTay.Vi_Tri_Van_Tay == ketqua[0]):
                            self.SignalRecognizedFGP.emit(idVaVanTay.ID_Thi_Sinh)
                            return
                self.SignalFGPnotFind.emit()

        except NameError:
            pass
        self.FlagFGPfree = True

