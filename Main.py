from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QObject, Qt, QTimer, pyqtSignal, pyqtSlot
from MainScreen.MainScreenAction   import MainScreen


class MainWindowContent(QObject):  
    def __init__(self, MainWindow):
        super(self.__class__, self).__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralFrame = QtWidgets.QFrame(self.centralwidget)
        self.centralFrame.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.centralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.centralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centralFrame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mainScreenObj = MainScreen(self.centralFrame)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    MainWindow.setWindowModality(QtCore.Qt.WindowModal)
    MainWindow.setFixedSize(QtCore.QSize(800, 480))
    ui = MainWindowContent(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
