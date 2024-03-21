
#coding = 'utf-8'
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_untitled
import time
import cv2
from logger import Logger
from static_info import StaticInfo
from tab1 import Tab1


if __name__ == '__main__':
    StaticInfo.InitVal()
    StaticInfo.g_app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    StaticInfo.g_tab1 = Tab1(ui, MainWindow)
    MainWindow.show()
    sys.exit(StaticInfo.g_app.exec_())
    pass


