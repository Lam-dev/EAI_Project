import ftplib
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
import  os
import shutil
from   GetSettingFromJSON       import GetSetting
# ftp = ftplib.FTP("192.168.1.46")
# ftp.login("etm", "1")
# file = []


# def getFile(ftp, filename):
#     try:
#         x = ftp.retrbinary("RETR " + filename ,open(""+filename, 'wb').write)
#         print(x)
#     except:
#         print ("Error")

# data = []
# ftp.cwd('/files/raspi_3g/')         # change directory to /pub/
# # getFile(ftp, "TTDD_29A-999999_2019-11-05_16-47-05.json")
# files = ftp.nlst()
# for f in files:
#     print(f)

# files = ftp.nlst()
# for f in files:
#     print(f)

SETTING_DICT = GetSetting.LoadSettingFromFile()
FTP_IP       =  SETTING_DICT["ftpIP"]
FTP_PORT     =  SETTING_DICT["ftpPort"]
FTP_ACCOUNT  =  SETTING_DICT["ftpAccount"]
FTP_PASSWORD =  SETTING_DICT["ftpPassword"]

LOCAL_PATH_CONTAIN_DATA_UPDATE = "DataUpdate/"
LOCAL_PATH_CONTAIN_ID_IMAGE = "IDimage/"
FTP_SERVER_DOWLOAD_IMAGE_FILE_PATH = "syncimage/"

class FTPclient(QObject):
    SignalFTPnotConnect = pyqtSignal()
    SignalFolderNotExist = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.__CreateConnect()


    def __CreateConnect(self):
        try:
            self.ftpObj = ftplib.FTP(FTP_IP)
            self.ftpObj.login(FTP_ACCOUNT, FTP_PASSWORD)
            return True

        except:
            return False

    def ConnectNewFTPserver(self, inforDict):
        global FTP_IP, FTP_PORT, FTP_ACCOUNT, FTP_PASSWORD
        FTP_IP = inforDict["ftpIP"]
        FTP_PORT = int(inforDict["ftpPort"])
        FTP_ACCOUNT = inforDict["ftpAccount"]
        FTP_PASSWORD  = inforDict["ftpPassword"]
        return self.__CreateConnect()


    def GetListStudentImage(self, fileDir):
        for i in range(0, 3):
            try:
                self.ftpObj.cwd(fileDir)
                lstFile = self.ftpObj.nlst()
                lstImage = []
                for f in lstFile:
                    
                    if(f.__contains__("jpg")):
                        lstImage.append(f)
                self.GetListFileFromServer(lstImage)
                return lstImage
            except:
                print(e)
                self.__CreateConnect()
        
    def SendImageToFTPserver(self, localfile, remotefile):
        fp = open(localfile, 'rb')
        try:
            self.__CreateConnect()
            self.ftpObj.storbinary('STOR %s' % remotefile, fp, 1024)
        except:
            print("remotefile not exist error caught" + remotefile)
            path,filename = os.path.split(remotefile)
            print("creating directory: " + remotefile)
            self.ftpObj.mkd(path)
            self.ftpObj.storbinary('STOR %s' % remotefile, fp, 1024)
            fp.close()
            return
        fp.close()
                
    def GetFileFromFTPserver(self, fileName, ftpFilePath = FTP_SERVER_DOWLOAD_IMAGE_FILE_PATH):
        self.ftpObj.cwd(ftpFilePath)
        try:
            self.ftpObj.retrbinary("RETR " + fileName ,open(LOCAL_PATH_CONTAIN_DATA_UPDATE + "image.jpg", 'wb').write)
        except:
            print(e.args)
            pass
# x = FTPclient()
# x.GetListStudentImage("/files/")
# x.SendImageToFTPserver("/home/lam/AppLoadXml/aaa.jpg", "files/aaa.jpg")

# x = FTPclient()
# x.GetListFileFromServer(['1.jpg', '2.jpg'])
