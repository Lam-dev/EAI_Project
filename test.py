import socket
from   datetime     import datetime
import json
SERVER_IP                                           = "192.168.1.2"
SERVER_PORT                                         = 2019
import getmac
def __DungKhungGiaoTiep(noiDung, malenh):
        
        if(type(noiDung) is not str): 
            return False, False
        highChieuDaiTen = int(len(noiDung) / 256)
        lowChieuDaiTen = int(len(noiDung) % 256)                                                                                                                                                                                                                                                                                    
        khungTruyen = [0x45, 0x53, 0x4D, malenh,lowChieuDaiTen, highChieuDaiTen]
        tong = malenh + lowChieuDaiTen + highChieuDaiTen
        j = 0
        for i in range (len(khungTruyen), len(khungTruyen) + len(noiDung)):
            khungTruyen.append('')
            khungTruyen[i] = ord(noiDung[j])
            tong = tong + ord(noiDung[j])
            j = j+ 1
            
        tong = -(~tong) % 256
        khungTruyen.append(0x00)
        khungTruyen[len(khungTruyen)-1] = tong
        return bytes(khungTruyen), tong

gotoGetFGP = {
    "troTrai":1,
    "utTrai":1,
    "troPhai":1

}
khungGui, sumc = __DungKhungGiaoTiep(json.dumps(gotoGetFGP), 2)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
client.send(khungGui)
