from        UARTconnection.UARTconnection   import UART
from        PyQt5.QtCore                    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
import      math

CODE_DATA_IN_CARD = 0
CODE_NOT_CARD = 1
CODE_RESQUEST_WRITE_DATA_TO_CARD = 2
CODE_WRITE_SUCCESSFUL = 3
CODE_WRITE_FAIL = 4


class ControlRFIDmudule(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        self.uartObject = UART()
        self.uartObject.SignalReciptedData.connect(self.ProcessReciptData)
        self.chuaXuLy = b''

    """
    Tach xu ly du lieu nhan
    """
    def ProcessReciptData(self, data):
        lstFrame = self.__TachCacKhungTruyen(data)
        for frame in lstFrame:
            self.SwitchRequest(frame)

    def SwitchRequest(self, frame):
        try:
            data, code = self.__CatLayPhanDataTrongFrame(khungNhan)
            reciptObj = self.json2obj(data)

            if(code == CODE_DATA_IN_CARD):
                pass
            elif(code == CODE_NOT_CARD):
                pass
            elif(code == CODE_RESQUEST_WRITE_DATA_TO_CARD):
                pass
            elif(code == CODE_WRITE_SUCCESSFUL):
                pass
            elif(code == CODE_WRITE_FAIL):
                pass
    except:
            pass
    
    def SendRequestWriteToRFcard(self, data):
        self.uartObject.SendDataToUART(self.__BuildFrameToSend(data, CODE_RESQUEST_WRITE_DATA_TO_CARD)[0])


    def __CatLayPhanDataTrongFrame(self, frameNhan):

        code = frameNhan[3]
        chieuDaiDl = frameNhan[4] + frameNhan[5] * math.pow(2, 8)
        return frameNhan[6, 6+chieuDaiDl], code
    
    

        """
    khung truyen uart yeu cau module 3g gui file
    tham so
        tenFile: ten cua file can gui
    tra ve
        khungTruyen: khong truyen de gui cho ETM module
        tong : checksum cua khung truyen 
    """
    def __BuildFrameToSend(self, byteArray, code):

        highChieuDaiTen = int(len(byteArray) / 256)
        lowChieuDaiTen = int(len(byteArray) % 256)
        khungTruyen = [0x45, 0x54, 0x4D, code, lowChieuDaiTen, highChieuDaiTen]
        tong = code + highChieuDaiTen + lowChieuDaiTen
        j = 0
        for byte in byteArray:
            tong += byte
        
        khungTruyen.append(byteArray)    
        tong = -(~tong) % 256
        khungTruyen.append(0x00)
        khungTruyen[len(khungTruyen)-1] = tong
        return bytes(khungTruyen), tong
    

    def __TachCacKhungTruyen(self, duLieu):
        if(duLieu == b''):
            return []
        self.chuaXuLy = self.chuaXuLy + duLieu
        lstKhungDL = []
        for i in range(0, len(self.chuaXuLy)):
            if( self.chuaXuLy[i:i+3].__str__().__contains__("ETM")):
                try:
                    chieuDaiDl = self.chuaXuLy[i+4] + self.chuaXuLy[i+5] * math.pow(2, 7)
                    chieuDaiKhung = i + int(chieuDaiDl) + 7
                    if(chieuDaiKhung + i <= len(self.chuaXuLy)):
                        lstKhungDL.append(self.chuaXuLy[i:chieuDaiKhung])
                        #self.chuaXuLy = self.chuaXuLy[chieuDaiKhung: len(self.chuaXuLy)]
                        i = i + chieuDaiKhung
                    else:
                        self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                        break
                except:
                    self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                    break
        return lstKhungDL


    """
    check sum mot frame
    """
    def __CheckSum(self, frame):
        # return True ## test
        try:
            sumValue = 0
            for i in range (3, len(frame) - 1):
                sumValue = sumValue + frame[i]
            sumValue = -(~sumValue) % 256
            # print("sum = ", tong) #test
            if(sumValue == frame[len(framframeeNhan)-1]):
                # print("checksum dung")
                return True
            else:
                # print("checksum sai")
                return False
        except:
            return False

