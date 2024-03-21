from string import punctuation
from turtle import color
import cv2
import numpy as np
import threading
from PyQt5.QtCore import *
import platform

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from cv_helper import CvHelper
from prpath_info import PrPathInfo
from udp_packet import UdpPacket
import sys
from logger import Logger
from static_info import StaticInfo
import time
import json

import tkinter
import tkinter.messagebox as messagebox

class Tab1:
    def __init__(self, ui, mainWnd):
        self.logger = Logger("tab1")
        self.isDebug = True
        self.ui = ui
        self.mainWnd = mainWnd
        self.msgBox = QMessageBox()
        # self.udpPacket = UdpPacket('', 0)
        StaticInfo.g_udp_packte = UdpPacket('', 0)
        self.ui.listWidget.clear()
        self.mb_signal = pyqtSignal(str)
        self.scanList = []
        self.scanPts = []
        self.inputImgPath = "/opt/qjs/gwcm/input.jpg"
        if (platform.system() == "Windows"):
            self.inputImgPath = "./input.jpg"
        self.outImgPath = "/opt/qjs/gwcm/out.jpg"
        if (platform.system() == "Windows"):
            self.outImgPath = "./out.jpg"
        self.scanMat = cv2.imread(self.inputImgPath)
        self.videoMat = cv2.resize(self.scanMat, (640, 480))
        self.polyMat = self.scanMat.copy()
        self.wHandler = ()
        self.cvHelper = CvHelper()
        self.prList = []
        self.isOpenIORealy = 0
        self.isOpenDO1 = 0
        self.isOpenDO2 = 0
        self.isOpenDO3 = 0
        self.isOpenDO4 = 0
        self.isOpenDO5 = 0
        self.isOpenDO6 = 0
        self.isOpenDO7 = 0
        self.isOpenDO8 = 0
        self.isOpenDO9 = 0
        self.isOpenDO10 = 0
        self.isOpenDO11 = 0
        self.isOpenDO12 = 0
        self.isOpenDO13 = 0
        self.isOpenDO14 = 0
        self.isOpenDO15 = 0
        self.isOpenDO16 = 0
        self.isOpenDO17 = 0
        self.isOpenDO18 = 0
        self.isOpenDO19 = 0
        self.isOpenDO20 = 0
        self.isOpenDO21 = 0
        self.isOpenDO22 = 0
        self.isOpenDO23 = 0
        self.isOpenDO24 = 0
        self.isOpenDO25 = 0
        self.isOpenDO26 = 0
        self.isOpenDO27 = 0
        self.isOpenDO28 = 0
        self.isOpenDO29 = 0
        self.isOpenDO30 = 0
        self.isOpenDO31 = 0
        self.isOpenDO32 = 0
        
        #按钮点击事件设置
        
        ui.pushButton_5.clicked.connect(self.pushButton_5_click)
        ui.pushButton_6.clicked.connect(self.pushButton_6_click)
        ui.pushButton_7.clicked.connect(self.pushButton_7_click)
        ui.pushButton_8.clicked.connect(self.pushButton_8_click)

        ui.pushButton_15.clicked.connect(self.pushButton_15_click)
        ui.pushButton_17.clicked.connect(self.pushButton_17_click)
        ui.pushButton_18.clicked.connect(self.pushButton_18_click)
        ui.pushButton_19.clicked.connect(self.pushButton_19_click)
        ui.pushButton_20.clicked.connect(self.pushButton_20_click)
        ui.pushButton_21.clicked.connect(self.pushButton_21_click)
        ui.pushButton_22.clicked.connect(self.pushButton_22_click)
        ui.pushButton_23.clicked.connect(self.pushButton_23_click)
        ui.pushButton_24.clicked.connect(self.pushButton_24_click)
        ui.pushButton_25.clicked.connect(self.pushButton_25_click)
        ui.pushButton_26.clicked.connect(self.pushButton_26_click)
        ui.pushButton_27.clicked.connect(self.pushButton_27_click)
        ui.pushButton_28.clicked.connect(self.pushButton_28_click)
        ui.pushButton_29.clicked.connect(self.pushButton_29_click)
        ui.pushButton_30.clicked.connect(self.pushButton_30_click)
        ui.pushButton_31.clicked.connect(self.pushButton_31_click)
        ui.pushButton_32.clicked.connect(self.pushButton_32_click)
        ui.pushButton_33.clicked.connect(self.pushButton_33_click)
        ui.pushButton_34.clicked.connect(self.pushButton_34_click)
        ui.pushButton_35.clicked.connect(self.pushButton_35_click)
        ui.pushButton_36.clicked.connect(self.pushButton_36_click)
        ui.pushButton_37.clicked.connect(self.pushButton_37_click)
        ui.pushButton_38.clicked.connect(self.pushButton_38_click)
        ui.pushButton_39.clicked.connect(self.pushButton_39_click)
        ui.pushButton_40.clicked.connect(self.pushButton_40_click)
        ui.pushButton_41.clicked.connect(self.pushButton_41_click)
        ui.pushButton_42.clicked.connect(self.pushButton_42_click)
        ui.pushButton_43.clicked.connect(self.pushButton_43_click)
        ui.pushButton_44.clicked.connect(self.pushButton_44_click)
        ui.pushButton_45.clicked.connect(self.pushButton_45_click)
        ui.pushButton_46.clicked.connect(self.pushButton_46_click)
        ui.pushButton_47.clicked.connect(self.pushButton_47_click)
        ui.pushButton_48.clicked.connect(self.pushButton_48_click)
        ui.pushButton_49.clicked.connect(self.pushButton_49_click)
        ui.pushButton_50.clicked.connect(self.pushButton_50_click)
        ui.pushButton_51.clicked.connect(self.pushButton_51_click)
        ui.pushButton_52.clicked.connect(self.pushButton_52_click)
        ui.pushButton_53.clicked.connect(self.pushButton_53_click)
        ui.pushButton_54.clicked.connect(self.pushButton_54_click)
        ui.pushButton_55.clicked.connect(self.pushButton_55_click)
        ui.pushButton_56.clicked.connect(self.pushButton_56_click)
        ui.pushButton_57.clicked.connect(self.pushButton_57_click)
        ui.pushButton_58.clicked.connect(self.pushButton_58_click)
        ui.pushButton_59.clicked.connect(self.pushButton_59_click)
        ui.pushButton_60.clicked.connect(self.pushButton_60_click)
        ui.pushButton_61.clicked.connect(self.pushButton_61_click)
        ui.pushButton_62.clicked.connect(self.pushButton_62_click)
        ui.pushButton_63.clicked.connect(self.pushButton_63_click)
        ui.pushButton_64.clicked.connect(self.pushButton_64_click)
        ui.pushButton_65.clicked.connect(self.pushButton_65_click)
        ui.pushButton_66.clicked.connect(self.pushButton_66_click)
        ui.pushButton_67.clicked.connect(self.pushButton_67_click)
        ui.pushButton_68.clicked.connect(self.pushButton_68_click)
        ui.pushButton_69.clicked.connect(self.pushButton_69_click)
        ui.pushButton_70.clicked.connect(self.pushButton_70_click)

        ui.pushButton_199.clicked.connect(self.pushButton_199_click)
        ui.pushButton_200.clicked.connect(self.pushButton_200_click)


        # 脉冲控制
        ui.pushButton_74.clicked.connect(self.pushButton_74_click)
        ui.pushButton_75.clicked.connect(self.pushButton_75_click)
        ui.pushButton_76.clicked.connect(self.pushButton_76_click)
        ui.pushButton_77.clicked.connect(self.pushButton_77_click)
        ui.pushButton_78.clicked.connect(self.pushButton_78_click)
        ui.pushButton_79.clicked.connect(self.pushButton_79_click)
        ui.pushButton_80.clicked.connect(self.pushButton_80_click)
        ui.pushButton_81.clicked.connect(self.pushButton_81_click)
        ui.pushButton_82.clicked.connect(self.pushButton_82_click)

        ui.pushButton_85.clicked.connect(self.pushButton_85_click)
        ui.pushButton_86.clicked.connect(self.pushButton_86_click)
        ui.pushButton_87.clicked.connect(self.pushButton_87_click)

        ui.pushButton_89.clicked.connect(self.pushButton_89_click)
        ui.pushButton_91.clicked.connect(self.pushButton_91_click)
        ui.pushButton_90.clicked.connect(self.pushButton_90_click)

        ui.pushButton_92.clicked.connect(self.pushButton_92_click)
        ui.pushButton_93.clicked.connect(self.pushButton_93_click)
        ui.pushButton_94.clicked.connect(self.pushButton_94_click)

        ui.pushButton_83.clicked.connect(self.pushButton_83_click)
        ui.pushButton_84.clicked.connect(self.pushButton_84_click)
        ui.pushButton_88.clicked.connect(self.pushButton_88_click)

        ui.pushButton_95.clicked.connect(self.pushButton_95_click)
        ui.pushButton_96.clicked.connect(self.pushButton_96_click)
        ui.pushButton_97.clicked.connect(self.pushButton_97_click)
        ui.pushButton_98.clicked.connect(self.pushButton_98_click)

        ui.pushButton_100.clicked.connect(self.pushButton_100_click)
        ui.pushButton_101.clicked.connect(self.pushButton_101_click)
        ui.pushButton_102.clicked.connect(self.pushButton_102_click)
        ui.pushButton_99.clicked.connect(self.pushButton_99_click)

        ui.pushButton_104.clicked.connect(self.pushButton_104_click)
        ui.pushButton_106.clicked.connect(self.pushButton_106_click)
        ui.pushButton_105.clicked.connect(self.pushButton_105_click)
        ui.pushButton_103.clicked.connect(self.pushButton_103_click)

        ui.pushButton_109.clicked.connect(self.pushButton_109_click)

        

        ui.pushButton_179.clicked.connect(self.pushButton_179_click)

        ui.pushButton_107.clicked.connect(self.pushButton_107_click)
        ui.pushButton_183.clicked.connect(self.pushButton_183_click)
        ui.pushButton_187.clicked.connect(self.pushButton_187_click)

        ui.pushButton_180.clicked.connect(self.pushButton_180_click)
        ui.pushButton_185.clicked.connect(self.pushButton_185_click)
        ui.pushButton_202.clicked.connect(self.pushButton_202_click)

        ui.pushButton_181.clicked.connect(self.pushButton_181_click)
        ui.pushButton_182.clicked.connect(self.pushButton_182_click)
        ui.pushButton_186.clicked.connect(self.pushButton_186_click)

        ui.pushButton_184.clicked.connect(self.pushButton_184_click)
        ui.pushButton_203.clicked.connect(self.pushButton_203_click)
        ui.pushButton_207.clicked.connect(self.pushButton_207_click)
        ui.pushButton_204.clicked.connect(self.pushButton_204_click)
        ui.pushButton_205.clicked.connect(self.pushButton_205_click)
        ui.pushButton_206.clicked.connect(self.pushButton_206_click)
        ui.pushButton_114.clicked.connect(self.pushButton_114_click)
        ui.pushButton_115.clicked.connect(self.pushButton_115_click)

        ui.pushButton_108.clicked.connect(self.pushButton_108_click)
        ui.pushButton_112.clicked.connect(self.pushButton_112_click)
        ui.pushButton_111.clicked.connect(self.pushButton_111_click)

        ui.pushButton_113.clicked.connect(self.pushButton_113_click)

        ui.pushButton_211.clicked.connect(self.pushButton_211_click)
        ui.pushButton_209.clicked.connect(self.pushButton_209_click)
        ui.pushButton_208.clicked.connect(self.pushButton_208_click)
        ui.pushButton_210.clicked.connect(self.pushButton_210_click)

        ui.pushButton_212.clicked.connect(self.pushButton_212_click)
        ui.pushButton_213.clicked.connect(self.pushButton_213_click)
        ui.pushButton_214.clicked.connect(self.pushButton_214_click)

        ui.pushButton_215.clicked.connect(self.pushButton_215_click)
        ui.pushButton_216.clicked.connect(self.pushButton_216_click)

        ui.pushButton_217.clicked.connect(self.pushButton_217_click)
        ui.pushButton_218.clicked.connect(self.pushButton_218_click)

        ui.pushButton_219.clicked.connect(self.pushButton_219_click)
        ui.pushButton_220.clicked.connect(self.pushButton_220_click)

        ui.pushButton_221.clicked.connect(self.pushButton_221_click)
        ui.pushButton_222.clicked.connect(self.pushButton_222_click)

        ui.pushButton_188.clicked.connect(self.pushButton_188_click)
        ui.pushButton_226.clicked.connect(self.pushButton_226_click)
        ui.pushButton_223.clicked.connect(self.pushButton_223_click)
        ui.pushButton_224.clicked.connect(self.pushButton_224_click)
        ui.pushButton_225.clicked.connect(self.pushButton_225_click)
        ui.pushButton_227.clicked.connect(self.pushButton_227_click)
        ui.pushButton_230.clicked.connect(self.pushButton_230_click)


        ui.listWidget.itemClicked.connect(self.listWidget_itemClicked)
        ui.listWidget_2.itemClicked.connect(self.listWidget_2_itemClickedNew)
        #ui.listWidget_3.itemClicked.connect(self.listWidget_3_itemClickedNew)
        # ui.label_13.doubleClicked.connect(self.label_13_doubleClicked)
        self.ui.tabWidget.setCurrentIndex(0)
        self.setSrvListNew()
        th1 = threading.Thread(target=self.tSetNowTimeer)
        th1.start()
        self.udpListen()
    
    def signal_handler(self):
        pass

    def udpListen(self):
        host = "192.168.10.101"
        if (platform.system() == "Windows"):
            host = "192.168.22.137"
        port = 10071
        _udpPacket = UdpPacket(host, port)
        th1 = threading.Thread(target=_udpPacket.OpenUdpListen)
        th1.start()
        th2 = threading.Thread(target=_udpPacket.UdpHandler)
        th2.start()
        
        self.logger.writelog("Udp Listen Thread Start")
        pass

    def pushButton_188_click(self):
        self.pushButton_184_click()
        pass

    def pushButton_226_click(self):
        self.pushButton_203_click()
        pass

    def pushButton_223_click(self):
        self.pushButton_207_click()
        pass

    def pushButton_224_click(self):
        self.pushButton_204_click()
        pass

    def pushButton_225_click(self):
        self.pushButton_205_click()
        pass

    def pushButton_227_click(self):
        self.pushButton_206_click()
        pass

    def pushButton_230_click(self):
        self.pushButton_214_click()
        pass

    def pushButton_221_click(self):
        print("pushButton_221_click" )
        reqJson = {"api": "OpenOut7"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_222_click(self):
        print("pushButton_222_click" )
        reqJson = {"api": "CloseOut7"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_219_click(self):
        print("pushButton_219_click" )
        reqJson = {"api": "CloseOut6"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_220_click(self):
        print("pushButton_220_click" )
        reqJson = {"api": "OpenOut6"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_217_click(self):
        print("pushButton_217_click" )
        reqJson = {"api": "OpenOut9"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_218_click(self):
        print("pushButton_218_click" )
        reqJson = {"api": "CloseOut9"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_215_click(self):
        ##print("pushButton_215_click" )
        reqJson = {"api": "OpenOut5"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_216_click(self):
        print("pushButton_216_click" )
        reqJson = {"api": "CloseOut5"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_214_click(self):
        #print("pushButton_214_click" )
        reqJson = {"api": "CarWashStep7"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_213_click(self):
        print("pushButton_213_click" )
        reqJson = {"api": "GetMoveWashArrData", "index": self.ui.lineEdit_56.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_212_click(self):
        print("pushButton_212_click" )
        reqJson = {"api": "GetMoveWashArrLen"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_211_click(self):
        # self.ui.lineEdit_54.setText("0")
        # self.ui.lineEdit_49.setText("0")
        # self.ui.lineEdit_50.setText("0")
        # self.ui.lineEdit_51.setText("0")
        # self.ui.lineEdit_52.setText("0")
        # self.ui.lineEdit_53.setText("0")
        print("pushButton_211_click" )
        reqJson = {"api": "EthFunc34"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_209_click(self):
        print("pushButton_209_click" )
        snNo = self.ui.lineEdit_54.text()
        speed = self.ui.lineEdit_49.text()
        st = self.ui.lineEdit_50.text()
        x_puu = self.ui.lineEdit_51.text()
        y_puu = self.ui.lineEdit_52.text()
        z_puu = self.ui.lineEdit_53.text()
        reqJson = {"api": "EthFunc35", "snNo": snNo, "speed": speed, 
                   "st": st, "x_puu": x_puu, "y_puu": y_puu, "z_puu": z_puu}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_208_click(self):
        print("pushButton_208_click" )
        reqJson = {"api": "EthFunc36"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_210_click(self):
        print("pushButton_210_click" )
        reqJson = {"api": "EthFunc37"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_113_click(self):
        print("pushButton_113_click" )
        self.scanList.clear()
        cv2.waitKey(30)
        self.scanMat = cv2.imread(self.inputImgPath)
        reqJson = {"api": "MoveWashCar"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_108_click(self):
        self.pushButton_92_click()
        pass

    def pushButton_112_click(self):
        self.pushButton_93_click()
        pass

    def pushButton_111_click(self):
        self.pushButton_94_click()
        pass

    def pushButton_184_click(self):
        #print("pushButton_184_click" )
        self.scanList.clear()
        cv2.waitKey(30)
        self.scanMat = cv2.imread(self.inputImgPath)
        reqJson = {"api": "CarWashStep1"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_203_click(self):
        #print("pushButton_203_click" )
        reqJson = {"api": "CarWashStep2"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_207_click(self):
        #print("pushButton_207_click" )
        reqJson = {"api": "CarWashStep3"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_204_click(self):
        #print("pushButton_204_click" )
        reqJson = {"api": "CarWashStep4"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_205_click(self):
        #print("pushButton_205_click" )
        reqJson = {"api": "CarWashStep5"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_206_click(self):
        #print("pushButton_206_click" )
        reqJson = {"api": "CarWashStep6"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_114_click(self):
        print("pushButton_114_click" )
        self.scanList.clear()
        cv2.waitKey(30)
        self.scanMat = cv2.imread(self.inputImgPath)
        reqJson = {"api": "MNCarWash"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_115_click(self):
        print("pushButton_115_click" )
        self.scanList.clear()
        cv2.waitKey(30)
        self.scanMat = cv2.imread(self.inputImgPath)
        reqJson = {"api": "GetMNScanFrame"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass


    
    
    
    

    def pushButton_69_click(self):
        print("pushButton_69_click" + self.ui.pushButton_69.text())
        reqJson = {"api": "ReadP1001","modbusId": self.ui.lineEdit_21.text(),"serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_70_click(self):
        print("pushButton_70_click" + self.ui.pushButton_70.text())
        reqJson = {"api": "SetP1001", "modbusId": self.ui.lineEdit_21.text(),"serialPort": self.ui.lineEdit_4.text(), "zval": self.ui.lineEdit_10.text() }
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_199_click(self):
        print("pushButton_199_click " + self.ui.pushButton_199.text())
        reqJson = {"api": "EnbleCom1Recv"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_200_click(self):
        print("pushButton_200_click " + self.ui.pushButton_200.text())
        reqJson = {"api": "CloseCom1Recv"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    


    
    

    

    
    
    

    def pushButton_5_click(self):
        print("pushButton_5_click " + self.ui.pushButton_5.text())
        reqJson = {"api": "ResetDev", "modbusId": self.ui.lineEdit.text(), "serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_6_click(self):
        print("pushButton_6_click")
        self.ui.tabWidget.setCurrentIndex(0)
        pass

    def pushButton_7_click(self):
        print("pushButton_7_click")
        self.ui.tabWidget.setCurrentIndex(1)
        pass

    def pushButton_8_click(self):
        print("pushButton_8_click")
        self.ui.tabWidget.setCurrentIndex(2)
        self.ui.listWidget.clear()
        for i in range(100):
            self.ui.listWidget.addItem("PR #" + str(i))
        # self.ui.listWidget.addItem("1111111111")
        # self.ui.listWidget.addItem("2222222222")
        # self.ui.listWidget.addItem("3333333333")
        pass

    def pushButton_15_click(self):
        print("pushButton_15_click " + self.ui.pushButton_15.text())
        pass
    
    def pushButton_16_click(self):
        print("pushButton_16_click " + self.ui.pushButton_16.text())
        pass

    def pushButton_17_click(self):
        print("pushButton_17_click " + self.ui.pushButton_17.text())
        
        pass

    def pushButton_18_click(self):
        print("pushButton_18_click " + self.ui.pushButton_18.text())
        pathNo = self.ui.lineEdit_2.text()
        puu = self.ui.lineEdit_3.text()
        #fx = self.ui.lineEdit_6.text()
        reqJson = {"api": "SetPRPath", "modbusId": self.ui.lineEdit.text(), "serialPort": self.ui.lineEdit_4.text(), "pathNo": pathNo, "puu": puu}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_19_click(self):
        print("pushButton_19_click " + self.ui.pushButton_19.text())
        self.ui.listWidget.clear()
        reqJson = {"api": "ReadAllPRPath", "serialPort": self.ui.lineEdit_4.text(), "modbusId": self.ui.lineEdit.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_20_click(self):
        print("pushButton_20_click " + self.ui.pushButton_20.text())
        reqJson = {"api": "OriginReset"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_21_click(self):
        print("pushButton_21_click " + self.ui.pushButton_21.text())
        
        reqJson = {"api": "ServoOn", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_22_click(self):
        print("pushButton_22_click" + self.ui.pushButton_22.text())
        reqJson = {"api": "ServoOff", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_23_click(self):
        print("pushButton_23_click" + self.ui.pushButton_23.text())
        jogSpeed = self.ui.lineEdit_5.text()
        reqJson = {"api": "JogCW", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text(), "jogSpeed": jogSpeed}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_24_click(self):
        print("pushButton_24_click" + self.ui.pushButton_24.text())
        jogSpeed = self.ui.lineEdit_5.text()
        reqJson = {"api": "JogCCW", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text(), "jogSpeed": jogSpeed}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_25_click(self):
        print("pushButton_25_click" + self.ui.pushButton_25.text())
        reqJson = {"api": "JogStopAll", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_26_click(self):
        print("pushButton_26_click" + self.ui.pushButton_26.text())
        reqJson = {"api": "KillUi"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_27_click(self):
        print("pushButton_27_click" + self.ui.pushButton_27.text())
        pathNo = self.ui.lineEdit_2.text()
        reqJson = {"api": "ExecPRPath", "serialPort": self.ui.lineEdit_4.text(), "modbusId": self.ui.lineEdit.text(), "pathNo": pathNo}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass


    

    def pushButton_28_click(self):
        print("pushButton_28_click" + self.ui.pushButton_28.text())
        self.scanList.clear()
        # self.scanMat = cv2.imread("/opt/qjs/gwcm/input.jpg")
        # self.videoMat = cv2.resize(self.scanMat, (640, 480))
        # cv2.imshow('Scan', self.videoMat)
        # pix = QPixmap("/opt/qjs/gwcm/input.jpg")
        # self.ui.label_13.setScaledContents(True)
        # self.ui.label_13.setPixmap(pix)
        # cv2.putText(self.videoMat, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '   Wait Scaning...', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0, 0), 1)
        # cv2.imshow('Scan', self.videoMat)
        reqJson = {"api": "ScanOutlineNew", "modbusId": self.ui.lineEdit.text(), "serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    

    def pushButton_29_click(self):
        print("pushButton_29_click" + self.ui.pushButton_29.text())
        reqJson = {"api": "GetJogSpeed", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_30_click(self):
        print("pushButton_30_click" + self.ui.pushButton_30.text())
        jogSpeed = self.ui.lineEdit_5.text()
        reqJson = {"api": "SetJogSpeed", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text(), "jogSpeed": jogSpeed}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_31_click(self):
        print("pushButton_31_click" + self.ui.pushButton_31.text())
        reqJson = {"api": "StopPRPath", "serialPort": self.ui.lineEdit_4.text(), "modbusId": self.ui.lineEdit.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_32_click(self):
        print("pushButton_32_click" + self.ui.pushButton_32.text())
        pathNo = self.ui.lineEdit_2.text()
        puu = self.ui.lineEdit_3.text()
        fx = self.ui.lineEdit_6.text()
        reqJson = {"api": "SetPRPathFx", "modbusId": self.ui.lineEdit.text(), "serialPort": self.ui.lineEdit_4.text(), "pathNo": pathNo, "puu": puu, "fx": fx}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_33_click(self):
        print("pushButton_33_click" + self.ui.pushButton_33.text())
        str = self.ui.lineEdit_2.text()
        if '-' in str:
            s = str.split('-')
            startPathNo = s[0]
            endPathNo = s[1]
            reqJson = {"api": "BatchDelPRPath", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text(), "startPathNo": startPathNo, "endPathNo": endPathNo}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        else:
            str2 = self.ui.lineEdit_2.text() + "-" + self.ui.lineEdit_2.text()
            s = str2.split('-')
            startPathNo = s[0]
            endPathNo = s[1]
            reqJson = {"api": "BatchDelPRPath", "modbusId": self.ui.lineEdit.text(),"serialPort": self.ui.lineEdit_4.text(), "startPathNo": startPathNo, "endPathNo": endPathNo}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_34_click(self):
        print("pushButton_34_click" + self.ui.pushButton_34.text())
        if self.isOpenIORealy == 0:
            reqJson = {"api": "IORelayOn", "serialPort": self.ui.lineEdit_7.text()}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        else:
            self.ui.label_34.setText("○")
            self.ui.label_34.setStyleSheet("color: rgb(0, 0, 0);")
            self.isOpenIORealy == 0
        time.sleep(2)
        reqJson = {"api": "ReadAllDoStatus", "serialPort": self.ui.lineEdit_7.text(), "channelCount" : 32}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        time.sleep(2)
        reqJson = {"api": "ReadAllDIStatus", "serialPort": self.ui.lineEdit_7.text(), "channelCount" : 32}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_35_click(self):
        print("pushButton_35_click " + self.ui.pushButton_35.text())
        if self.isOpenDO1 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 0}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO1 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 0}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO1 = 0
        pass

    def pushButton_36_click(self):
        print("pushButton_36_click" + self.ui.pushButton_36.text())
        if self.isOpenDO2 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 1}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO2 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 1}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO2 = 0
        pass

    def pushButton_37_click(self):
        if self.isOpenDO3 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 2}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO3 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 2}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO3 = 0
        pass
    
    def pushButton_38_click(self):
        if self.isOpenDO4 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 3}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO4 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 3}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO4 = 0
        pass
    
    def pushButton_39_click(self):
        if self.isOpenDO5 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 4}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO5 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 4}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO5 = 0
        pass

    def pushButton_40_click(self):
        if self.isOpenDO6 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 5}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO6 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 5}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO6 = 0
        pass

    def pushButton_41_click(self):
        if self.isOpenDO7 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 6}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO7 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 6}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO7 = 0
        pass

    def pushButton_42_click(self):
        if self.isOpenDO8 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 7}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO8 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 7}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO8 = 0
        pass
    def pushButton_43_click(self):
        if self.isOpenDO9 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 8}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO9 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 8}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO9 = 0
        pass

    def pushButton_44_click(self):
        if self.isOpenDO10 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 9}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO10 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 9}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO10 = 0
        pass

    def pushButton_45_click(self):
        if self.isOpenDO11 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 10}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO11 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 10}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO11 = 0
        pass

    def pushButton_46_click(self):
        if self.isOpenDO12 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 11}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO12 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 11}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO12 = 0
        pass

    def pushButton_47_click(self):
        if self.isOpenDO13 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 12}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO13 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 12}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO13 = 0
        pass

    def pushButton_48_click(self):
        if self.isOpenDO14 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 13}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO14 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 13}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO14 = 0
        pass

    def pushButton_49_click(self):
        if self.isOpenDO15 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 14}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO15 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 14}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO15 = 0
        pass

    def pushButton_50_click(self):
        if self.isOpenDO16 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 15}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO16 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 15}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO16 = 0
        pass

    def pushButton_51_click(self):
        if self.isOpenDO17 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 16}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO17 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 16}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO17 = 0
        pass

    def pushButton_52_click(self):
        if self.isOpenDO18 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 17}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO18 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 17}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO18 = 0
        pass

    def pushButton_53_click(self):
        if self.isOpenDO19 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 18}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO19 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 18}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO19 = 0
        pass

    def pushButton_54_click(self):
        if self.isOpenDO20 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 19}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO20 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 19}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO20 = 0
        pass

    def pushButton_55_click(self):
        if self.isOpenDO21 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 20}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO21 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 20}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO21 = 0
        pass

    def pushButton_56_click(self):
        if self.isOpenDO22 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 21}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO22 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 21}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO22 = 0
        pass

    def pushButton_57_click(self):
        if self.isOpenDO23 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 22}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO23 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 22}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO23 = 0
        pass

    def pushButton_58_click(self):
        if self.isOpenDO24 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 23}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO24 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 23}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO24 = 0
        pass

    def pushButton_59_click(self):
        if self.isOpenDO25 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 24}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO25 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 24}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO25 = 0
        pass

    def pushButton_60_click(self):
        if self.isOpenDO26 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 25}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO26 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 25}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO26 = 0
        pass

    def pushButton_61_click(self):
        if self.isOpenDO27 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 26}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO27 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 26}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO27 = 0
        pass

    def pushButton_62_click(self):
        if self.isOpenDO28 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 27}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO28 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 27}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO28 = 0
        pass

    def pushButton_63_click(self):
        if self.isOpenDO29 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 28}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO29 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 28}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO29 = 0
        
        pass

    def pushButton_64_click(self):
        if self.isOpenDO30 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 29}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO30 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 29}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO30 = 0
        
        pass

    def pushButton_65_click(self):
        if self.isOpenDO31 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 30}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO31 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 30}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO31 = 0
        
        pass

    def pushButton_66_click(self):
        if self.isOpenDO32 == 0:
            reqJson = {"api": "OpenDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 31}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO32 = 1
        else:
            reqJson = {"api": "CloseDo", "serialPort": self.ui.lineEdit_7.text(), "channelNo" : 31}
            jsonStr = json.dumps(reqJson)
            StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
            self.isOpenDO32 = 0
        
        pass

    def pushButton_67_click(self):
        reqJson = {"api": "ReadAllDoStatus", "serialPort": self.ui.lineEdit_7.text(), "channelCount" : 32}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_68_click(self):
        # 获取DI信号返回报文： 1 2 4 5 80 4 0 F8 6，即0x05 0x80 0x04 0x00为DI信号数据
        # 根据0x05 0x80 0x04 0x00解析为32路的DI信号（1字节=8bit）：1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ，即DI1  DI3  DI16 DI19 读出来是1
        # 注：解析单字节的顺序为右到左，即第一字节最右bit位为DI1，第二字节最右bit位为DI9，以此类推
        reqJson = {"api": "ReadAllDIStatus", "serialPort": self.ui.lineEdit_7.text(), "channelCount" : 32}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_74_click(self):
        reqJson = {"api": "EthFunc1", "speed": self.ui.lineEdit_13.text(), "lowSpeed" : self.ui.lineEdit_11.text(),"st": self.ui.lineEdit_14.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_75_click(self):
        reqJson = {"api": "EthFunc2", "speed": self.ui.lineEdit_15.text(), "lowSpeed" : self.ui.lineEdit_12.text(),"st": self.ui.lineEdit_16.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_76_click(self):
        reqJson = {"api": "EthFunc3", "speed": self.ui.lineEdit_22.text(), "lowSpeed" : self.ui.lineEdit_17.text(),"st": self.ui.lineEdit_18.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_77_click(self):
        reqJson = {"api": "EthFunc4"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_78_click(self):
        reqJson = {"api": "EthFunc5"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_79_click(self):
        reqJson = {"api": "EthFunc6"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_80_click(self):
        reqJson = {"api": "EthFunc7"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_81_click(self):
        reqJson = {"api": "EthFunc8"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_82_click(self):
        reqJson = {"api": "EthFunc9"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_85_click(self):
        reqJson = {"api": "EthFunc10"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_86_click(self):
        reqJson = {"api": "EthFunc11"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_87_click(self):
        reqJson = {"api": "EthFunc12"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_89_click(self):
        reqJson = {"api": "EthFunc13"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_91_click(self):
        reqJson = {"api": "EthFunc14"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_90_click(self):
        reqJson = {"api": "EthFunc15"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_92_click(self):
        reqJson = {"api": "EthFunc16"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_93_click(self):
        reqJson = {"api": "EthFunc17"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_94_click(self):
        reqJson = {"api": "EthFunc18"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_83_click(self):
        reqJson = {"api": "EthFunc19"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_84_click(self):
        reqJson = {"api": "EthFunc20"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_88_click(self):
        reqJson = {"api": "EthFunc21"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_95_click(self):
        reqJson = {"api": "EthFunc31","puu": self.ui.lineEdit_23.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_96_click(self):
        pass

    def pushButton_97_click(self):
        self.pushButton_82_click()
        pass

    def pushButton_98_click(self):
        self.pushButton_83_click()
        pass

    def pushButton_100_click(self):
        reqJson = {"api": "EthFunc32","puu": self.ui.lineEdit_24.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_101_click(self):
        
        pass

    def pushButton_102_click(self):
        self.pushButton_87_click()
        pass

    def pushButton_99_click(self):
        self.pushButton_84_click()
        pass

    def pushButton_104_click(self):
        reqJson = {"api": "EthFunc33","puu": self.ui.lineEdit_25.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_106_click(self):
        
        pass

    def pushButton_105_click(self):
        self.pushButton_90_click()
        pass

    def pushButton_103_click(self):
        self.pushButton_88_click()
        pass

    

    def pushButton_177_click(self):
        reqJson = {"api": "EthFunc30","ioNo": self.ui.lineEdit_38.text(), "ioStatus": 1}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_178_click(self):
        reqJson = {"api": "EthFunc30","ioNo": self.ui.lineEdit_38.text(), "ioStatus": 0}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_179_click(self):
        self.scanList.clear()
        cv2.waitKey(30)
        self.scanMat = cv2.imread(self.inputImgPath)
        reqJson = {"api": "EthFunc30"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_107_click(self):
        reqJson = {"api": "EthFunc22","puu": self.ui.lineEdit_26.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_183_click(self):
        reqJson = {"api": "EthFunc24","puu": self.ui.lineEdit_27.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_187_click(self):
        reqJson = {"api": "EthFunc26","puu": self.ui.lineEdit_28.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass
    
    def pushButton_109_click(self):
        reqJson = {"api": "EthFunc29"}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def pushButton_180_click(self):
        self.pushButton_82_click()
        pass

    def pushButton_185_click(self):
        self.pushButton_87_click()
        pass

    def pushButton_202_click(self):
        self.pushButton_90_click()
        pass

    def pushButton_181_click(self):
        self.pushButton_83_click()
        pass

    def pushButton_182_click(self):
        self.pushButton_84_click()
        pass

    def pushButton_186_click(self):
        self.pushButton_88_click()
        pass

    def listWidget_itemClicked(self, item):
        print("listWidget_itemClicked")
        pathNo = item.text().split("#")[1]
        reqJson = {"api": "ReadPRPathByPathNo", "modbusId": self.ui.lineEdit.text(), "serialPort": self.ui.lineEdit_4.text(), "pathNo": pathNo}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def listWidget_2_itemClicked(self, item):
        print("listWidget_2_itemClicked")
        if item.text() == "COM #1":
            self.ui.lineEdit_4.setText("1")
        elif item.text() == "COM #2":
            self.ui.lineEdit_4.setText("2")
        elif item.text() == "COM #3":
            self.ui.lineEdit_4.setText("3")
        elif item.text() == "COM #4":
            self.ui.lineEdit_4.setText("4")
        elif item.text() == "COM #5":
            self.ui.lineEdit_4.setText("5")
        elif item.text() == "COM #6":
            self.ui.lineEdit_4.setText("6")
        elif item.text() == "COM #7":
            self.ui.lineEdit_4.setText("7")
        elif item.text() == "COM #8":
            self.ui.lineEdit_4.setText("8")
        pass

    def listWidget_2_itemClickedNew(self, item):
        print("listWidget_2_itemClickedNew")
        if item.text() == "X轴伺服器":
            self.ui.lineEdit_4.setText("6")
        elif item.text() == "Y轴伺服器":
            self.ui.lineEdit_4.setText("7")
        elif item.text() == "Z轴伺服器":
            self.ui.lineEdit_4.setText("8")
        
        pass

    def listWidget_3_itemClickedNew(self, item):
        print("listWidget_3_itemClickedNew")
        if item.text() == "X轴伺服器":
            self.ui.lineEdit_19.setText("6")
        elif item.text() == "Y轴伺服器":
            self.ui.lineEdit_19.setText("7")
        elif item.text() == "Z轴伺服器":
            self.ui.lineEdit_19.setText("8")
        reqJson = {"api": "ServoOn", "modbusId": self.ui.lineEdit_21.text(),"serialPort": self.ui.lineEdit_19.text()}
        jsonStr = json.dumps(reqJson)
        StaticInfo.g_udp_packte.UdpNewConnSendTo(StaticInfo.g_src_addr,StaticInfo.g_dst_addr, jsonStr)
        pass

    def label_13_doubleClicked(self):
        print("label_13_doubleClicked")
        pass

    def tSetNowTimeer(self):
        while True:
            now_date = time.strftime("%Y-%m-%d", time.localtime())
            now_time = time.strftime('%H:%M:%S',time.localtime())
            self.ui.label.setText(now_date)
            self.ui.label_3.setText(now_time)
            time.sleep(1)
    
    # 伺服器列表数据
    def setSrvListNew(self):
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItem("X轴伺服器")
        self.ui.listWidget_2.addItem("")
        self.ui.listWidget_2.addItem("Y轴伺服器")
        self.ui.listWidget_2.addItem("")
        self.ui.listWidget_2.addItem("Z轴伺服器")
        #self.ui.listWidget_3 = self.ui.listWidget_2
        # self.ui.listWidget_3.clear()
        # self.ui.listWidget_3.addItem("X轴伺服器")
        # self.ui.listWidget_3.addItem("")
        # self.ui.listWidget_3.addItem("Y轴伺服器")
        # self.ui.listWidget_3.addItem("")
        # self.ui.listWidget_3.addItem("Z轴伺服器")

        
    
    def setSrvList(self):
        self.ui.listWidget_2.clear()
        for i in range(8):
            self.ui.listWidget_2.addItem("COM #" + str(i+1))
        pass

    
    
    def pressResp(self,data):
        # tk = tkinter.Tk()
        # tk.withdraw()
        j = json.loads(data)
        api = j.get('api')
        rt = int(j.get('rt'))
        err = int(j.get('err'))
        msg = j.get('msg')
        if api == "ServoOn":
            print("ServoOn")
        elif api == "ServoOff":
            print("ServoOff")
        elif api == "OriginReset":
            print("OriginReset")
        elif api == "ReadAllPRPath":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressReadAllPRPath(data)
            else:
                self.logger.writelog("ReadAllPRPath Error " + msg)
        elif api == "ReadPRPathByPathNo":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressReadPRPathByPathNo(data)
            else:
                self.logger.writelog("ReadPRPathByPathNo Error " + msg)
        elif api == "SetPRPath":
            if rt > 0 and err == 0:
                tk = tkinter.Tk()
                tk.withdraw()
                StaticInfo.g_tab1.pressSetPRPath(data)
                tk.destroy()
            else:
                self.logger.writelog("SetPRPath Error " + msg)
        elif api == "ScanOutline":
            if rt > 0 and err == 0:
                if rt == 1:
                    scanframe_no = int(j.get('scanframe_no'))
                    h_point_x = int(j.get('h_point_x'))
                    h_point_y = int(j.get('h_point_y'))
                    l_point_x = int(j.get('l_point_x'))
                    l_point_y = int(j.get('l_point_y'))
                    self.scanList.append((scanframe_no,h_point_x,h_point_y))
                    self.scanList.append((scanframe_no,l_point_x,l_point_y))
                if rt == 2:
                    if len(self.scanList) > 0:
                        scanframe_count = int(j.get('scanframe_count')) * 2
                        while True:
                            if scanframe_count == len(self.scanList):
                                self.scanPts = np.array([],np.int32)
                                break
                            cv2.waitKey(5)

                        self.pressScanOutline()
                        # while True:
                        #     if len(self.scanList) == 0:
                        #         break
                        #     th = threading.Thread(target=self.pressScanOutline)
                        #     th.start()
                        #     cv2.waitKey(5)
            else:
                tk = tkinter.Tk()
                tk.withdraw()
                self.logger.writelog("ScanOutline Error " + msg)
                messagebox.showwarning("提示","扫描失败 Error " + msg)
                self.scanList.clear()
                tk.destroy()
        
        elif api == "ScanOutlineNew":
            if rt > 0 and err == 0:
                if rt == 1:
                    scanframe_no = int(j.get('scanframe_no'))
                    h_point_x = int(j.get('h_point_x'))
                    h_point_y = int(j.get('h_point_y'))
                    l_point_x = int(j.get('l_point_x'))
                    l_point_y = int(j.get('l_point_y'))
                    self.scanList.append((scanframe_no,h_point_x,h_point_y))
                    self.scanList.append((scanframe_no,l_point_x,l_point_y))
                if rt == 2:
                    if len(self.scanList) > 0:
                        # scanframe_count = int(j.get('scanframe_count')) * 2
                        # print("Scan Outline End scanframe_count %d" % (scanframe_count))
                        # th = threading.Thread(target=StaticInfo.g_tab1.scanOut, args=[self.scanMat,self.scanList,self.ui.label_13])
                        # th.start()
                        self.scanOut(self.scanMat,self.scanList,1)
                        # while True:
                        #     if scanframe_count == len(self.scanList):
                        #         self.scanPts = np.array([],np.int32)
                        #         break
                        #     cv2.waitKey(5)
                        #self.pressScanOutline()
            else:
                tk = tkinter.Tk()
                tk.withdraw()
                self.logger.writelog("ScanOutline Error " + msg)
                messagebox.showwarning("提示","扫描失败 Error " + msg)
                self.scanList.clear()
                tk.destroy()

        elif api == "ScanOutlineNew2":
            if rt > 0 and err == 0:
                if rt == 1:
                    scanframe_no = int(j.get('scanframe_no'))
                    h_point_x = int(j.get('h_point_x'))
                    h_point_y = int(j.get('h_point_y'))
                    # l_point_x = int(j.get('l_point_x'))
                    # l_point_y = int(j.get('l_point_y'))
                    self.scanList.append((scanframe_no,h_point_x,h_point_y))
                    # self.scanList.append((scanframe_no,l_point_x,l_point_y))
                if rt == 2:
                    if len(self.scanList) > 0:
                        # scanframe_count = int(j.get('scanframe_count')) * 2
                        # print("Scan Outline End scanframe_count %d" % (scanframe_count))
                        # th = threading.Thread(target=StaticInfo.g_tab1.scanOut, args=[self.scanMat,self.scanList,self.ui.label_13])
                        # th.start()
                        self.scanOut(self.scanMat,self.scanList,2)
                        # while True:
                        #     if scanframe_count == len(self.scanList):
                        #         self.scanPts = np.array([],np.int32)
                        #         break
                        #     cv2.waitKey(5)
                        #self.pressScanOutline()
            else:
                tk = tkinter.Tk()
                tk.withdraw()
                self.logger.writelog("ScanOutline Error " + msg)
                messagebox.showwarning("提示","扫描失败 Error " + msg)
                self.scanList.clear()
                tk.destroy()

        elif api == "GetJogSpeed":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressGetJogSpeed(data)
            else:
                self.logger.writelog("GetJogSpeed Error " + msg)
        elif api == "SetJogSpeed":
            tk = tkinter.Tk()
            tk.withdraw()
            if rt > 0 and err == 0:
                messagebox.showwarning("提示",msg)
            else:
                self.logger.writelog("SetPRPath Error " + msg)
                messagebox.showwarning("提示",msg)
            tk.destroy()
        elif api == "ReadP1001":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressReadP1001(data)
            else:
                self.logger.writelog("ReadP1001 Error " + msg)
        elif api == "SetPROffset":
            tk = tkinter.Tk()
            tk.withdraw()
            if rt > 0 and err == 0:
                messagebox.showwarning("提示",msg)
            else:
                self.logger.writelog("SetPROffset Error " + msg)
                messagebox.showwarning("提示",msg)
            tk.destroy()
        elif api == "BatchSetPRPath":
            tk = tkinter.Tk()
            tk.withdraw()
            if rt > 0 and err == 0:
                messagebox.showwarning("提示",msg)
            else:
                self.logger.writelog("BatchSetPRPath Error " + msg)
                messagebox.showwarning("提示",msg)
            tk.destroy()
        elif api == "BatchDelPRPath":
            tk = tkinter.Tk()
            tk.withdraw()
            if rt > 0 and err == 0:
                messagebox.showwarning("提示",msg)
            else:
                self.logger.writelog("BatchDelPRPath Error " + msg)
                messagebox.showwarning("提示",msg)
            tk.destroy()
        elif api == "IORelayOn":
            tk = tkinter.Tk()
            tk.withdraw()
            if rt > 0 and err == 0:
                self.isOpenIORealy == 1
                self.ui.label_34.setText("●")
                self.ui.label_34.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.isOpenIORealy == 0
                self.ui.label_34.setText("○")
                self.ui.label_34.setStyleSheet("color: rgb(0, 0, 0);")
                #messagebox.showwarning("提示","操作失败")
            tk.destroy()
        elif api == "OpenDo":
            tk = tkinter.Tk()
            tk.withdraw()
            channelNo = int(j.get('channelNo'))
            if rt > 0 and err == 0:
                if channelNo == 0 :
                    self.isOpenDO1 = 1
                    self.ui.pushButton_35.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 1 :
                    self.isOpenDO2 = 1
                    self.ui.pushButton_36.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 2 :
                    self.isOpenDO3 = 1
                    self.ui.pushButton_37.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 3 :
                    self.isOpenDO4 = 1
                    self.ui.pushButton_38.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 4 :
                    self.isOpenDO5 = 1
                    self.ui.pushButton_39.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 5 :
                    self.isOpenDO6 = 1
                    self.ui.pushButton_40.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 6 :
                    self.isOpenDO7 = 1
                    self.ui.pushButton_41.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 7 :
                    self.isOpenDO8 = 1
                    self.ui.pushButton_42.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 8 :
                    self.isOpenDO9 = 1
                    self.ui.pushButton_43.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 9 :
                    self.isOpenDO10 = 1
                    self.ui.pushButton_44.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 10 :
                    self.isOpenDO11 = 1
                    self.ui.pushButton_45.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 11 :
                    self.isOpenDO12 = 1
                    self.ui.pushButton_46.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 12 :
                    self.isOpenDO13 = 1
                    self.ui.pushButton_47.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 13 :
                    self.isOpenDO14 = 1
                    self.ui.pushButton_48.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 14 :
                    self.isOpenDO15 = 1
                    self.ui.pushButton_49.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 15 :
                    self.isOpenDO16 = 1
                    self.ui.pushButton_50.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 16 :
                    self.isOpenDO17 = 1
                    self.ui.pushButton_51.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 17 :
                    self.isOpenDO18 = 1
                    self.ui.pushButton_52.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 18 :
                    self.isOpenDO19 = 1
                    self.ui.pushButton_53.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 19 :
                    self.isOpenDO20 = 1
                    self.ui.pushButton_54.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 20 :
                    self.isOpenDO21 = 1
                    self.ui.pushButton_56.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 21 :
                    self.isOpenDO22 = 1
                    self.ui.pushButton_57.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 22 :
                    self.isOpenDO23 = 1
                    self.ui.pushButton_58.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 23 :
                    self.isOpenDO24 = 1
                    self.ui.pushButton_59.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 24 :
                    self.isOpenDO25 = 1
                    self.ui.pushButton_60.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 25 :
                    self.isOpenDO26 = 1
                    self.ui.pushButton_61.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 26 :
                    self.isOpenDO27 = 1
                    self.ui.pushButton_62.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 27 :
                    self.isOpenDO28 = 1
                    self.ui.pushButton_63.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 28 :
                    self.isOpenDO29 = 1
                    self.ui.pushButton_64.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 29 :
                    self.isOpenDO30 = 1
                    self.ui.pushButton_65.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 30 :
                    self.isOpenDO31 = 1
                    self.ui.pushButton_66.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                if channelNo == 31 :
                    self.isOpenDO32 = 1
                    self.ui.pushButton_67.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
                
            else:
                messagebox.showwarning("提示","操作失败")
            tk.destroy()

        elif api == "CloseDo":
            tk = tkinter.Tk()
            tk.withdraw()
            channelNo = int(j.get('channelNo'))
            if rt > 0 and err == 0:
                if channelNo == 0 :
                    self.isOpenDO1 = 0
                    self.ui.pushButton_35.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 1 :
                    self.isOpenDO2 = 0
                    self.ui.pushButton_36.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 2 :
                    self.isOpenDO3 = 0
                    self.ui.pushButton_37.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 3 :
                    self.isOpenDO4 = 0
                    self.ui.pushButton_38.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 4 :
                    self.isOpenDO5 = 0
                    self.ui.pushButton_39.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 5 :
                    self.isOpenDO6 = 0
                    self.ui.pushButton_40.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 6 :
                    self.isOpenDO7 = 0
                    self.ui.pushButton_41.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 7 :
                    self.isOpenDO8 = 0
                    self.ui.pushButton_42.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 8 :
                    self.isOpenDO9 = 0
                    self.ui.pushButton_43.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 9 :
                    self.isOpenDO10 = 0
                    self.ui.pushButton_44.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 10 :
                    self.isOpenDO11 = 0
                    self.ui.pushButton_45.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 11 :
                    self.isOpenDO12 = 0
                    self.ui.pushButton_46.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 12 :
                    self.isOpenDO13 = 0
                    self.ui.pushButton_47.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 13 :
                    self.isOpenDO14 = 0
                    self.ui.pushButton_48.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 14 :
                    self.isOpenDO15 = 0
                    self.ui.pushButton_49.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 15 :
                    self.isOpenDO16 = 0
                    self.ui.pushButton_50.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 16 :
                    self.isOpenDO17 = 0
                    self.ui.pushButton_51.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 17 :
                    self.isOpenDO18 = 0
                    self.ui.pushButton_52.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 18 :
                    self.isOpenDO19 = 0
                    self.ui.pushButton_53.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 19 :
                    self.isOpenDO20 = 0
                    self.ui.pushButton_54.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 20 :
                    self.isOpenDO21 = 0
                    self.ui.pushButton_56.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 21 :
                    self.isOpenDO22 = 0
                    self.ui.pushButton_57.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 22 :
                    self.isOpenDO23 = 0
                    self.ui.pushButton_58.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 23 :
                    self.isOpenDO24 = 0
                    self.ui.pushButton_59.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 24 :
                    self.isOpenDO25 = 0
                    self.ui.pushButton_60.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 25 :
                    self.isOpenDO26 = 0
                    self.ui.pushButton_61.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 26 :
                    self.isOpenDO27 = 0
                    self.ui.pushButton_62.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 27 :
                    self.isOpenDO28 = 0
                    self.ui.pushButton_63.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 28 :
                    self.isOpenDO29 = 0
                    self.ui.pushButton_64.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 29 :
                    self.isOpenDO30 = 0
                    self.ui.pushButton_65.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 30 :
                    self.isOpenDO31 = 0
                    self.ui.pushButton_66.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                if channelNo == 31 :
                    self.isOpenDO32 = 0
                    self.ui.pushButton_67.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
                
                
            else:
                messagebox.showwarning("提示","操作失败")
            tk.destroy()

        elif api == "ReadAllDoStatus":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressReadAllDoStatus(data)
            else:
                self.logger.writelog("ReadAllDoStatus Error " + msg)
        elif api == "ReadAllDIStatus":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressReadAllDIStatus(data)
            else:
                self.logger.writelog("ReadAllDIStatus Error " + msg)
        elif api == "EthFunc4":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressEthFunc4(data)
            else:
                self.logger.writelog("pressEthFunc4 Error " + msg)
        elif api == "EthFunc5":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressEthFunc5(data)
            else:
                self.logger.writelog("pressEthFunc5 Error " + msg)
        elif api == "EthFunc6":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressEthFunc6(data)
            else:
                self.logger.writelog("pressEthFunc6 Error " + msg)
        elif api == "EthFunc29":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressEthFunc29(data)
            else:
                self.logger.writelog("pressEthFunc6 Error " + msg)
        elif api == "PdoStatusUpload":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressPdoStatusUpload(data)
            else:
                self.logger.writelog("pressPdoStatusUpload Error " + msg)
        elif api == "GetMoveWashArrLen":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressGetMoveWashArrLen(data)
            else:
                self.logger.writelog("pressGetMoveWashArrLen Error " + msg)
        elif api == "GetMoveWashArrData":
            if rt > 0 and err == 0:
                StaticInfo.g_tab1.pressGetMoveWashArrData(data)
            else:
                self.logger.writelog("pressGetMoveWashArrData Error " + msg)
        pass
        
        # tk.destroy()

    def pressGetMoveWashArrData(self, data):
        j = json.loads(data)
        x_puu = j.get('x_puu')
        y_puu = j.get('y_puu')
        z_puu = j.get('z_puu')
        snNo = self.ui.lineEdit_56.text()
        self.ui.lineEdit_54.setText(snNo)
        self.ui.lineEdit_49.setText("1000")
        self.ui.lineEdit_50.setText("1000")
        self.ui.lineEdit_51.setText(str(x_puu))
        self.ui.lineEdit_52.setText(str(y_puu))
        self.ui.lineEdit_53.setText(str(z_puu))
        pass

    def pressGetMoveWashArrLen(self, data):
        j = json.loads(data)
        arr_len = j.get('arr_len')
        self.ui.lineEdit_55.setText(str(arr_len))
        pass

    def pressPdoStatusUpload(self, data):
        j = json.loads(data)
        x_org = j.get('x_org')
        x_front = j.get('x_front')
        x_back = j.get('x_back')
        y_org = j.get('y_org')
        y_up = j.get('y_up')
        y_down = j.get('y_down')
        z_org = j.get('z_org')
        z_left = j.get('z_left')
        z_right = j.get('z_right')
        x_puu = j.get('x_puu')
        y_puu = j.get('y_puu')
        z_puu = j.get('z_puu')
        unmove = j.get('unmove')
        self.ui.lineEdit_48.setText(str(x_back))
        self.ui.lineEdit_42.setText(str(x_front))
        self.ui.lineEdit_43.setText(str(y_up))
        self.ui.lineEdit_44.setText(str(y_down))
        self.ui.lineEdit_45.setText(str(z_left))
        self.ui.lineEdit_46.setText(str(z_right))

        self.ui.lineEdit_38.setText(str(x_puu))
        self.ui.lineEdit_40.setText(str(y_puu))
        self.ui.lineEdit_39.setText(str(z_puu))

        self.ui.lineEdit_47.setText(str(unmove))
        pass

    def pressEthFunc4(self, data):
        j = json.loads(data)
        x_lowSpeed = j.get('x_lowSpeed')
        x_speed = j.get('x_speed')
        x_st = j.get('x_st')
        self.ui.lineEdit_11.setText(str(x_lowSpeed))
        self.ui.lineEdit_13.setText(str(x_speed))
        self.ui.lineEdit_14.setText(str(x_st))
        pass

    def pressEthFunc5(self, data):
        j = json.loads(data)
        y_lowSpeed = j.get('y_lowSpeed')
        y_speed = j.get('y_speed')
        y_st = j.get('y_st')
        self.ui.lineEdit_12.setText(str(y_lowSpeed))
        self.ui.lineEdit_15.setText(str(y_speed))
        self.ui.lineEdit_16.setText(str(y_st))
        pass

    def pressEthFunc6(self, data):
        j = json.loads(data)
        z_lowSpeed = j.get('z_lowSpeed')
        z_speed = j.get('z_speed')
        z_st = j.get('z_st')
        self.ui.lineEdit_17.setText(str(z_lowSpeed))
        self.ui.lineEdit_22.setText(str(z_speed))
        self.ui.lineEdit_18.setText(str(z_st))
        pass

    def pressEthFunc29(self, data):
        j = json.loads(data)
        x_location = j.get('x_location')
        y_location = j.get('y_location')
        z_location = j.get('z_location')
        self.ui.lineEdit_36.setText(str(x_location))
        self.ui.lineEdit_37.setText(str(y_location))
        self.ui.lineEdit_35.setText(str(z_location))
        pass

    def pressReadP1001(self, data):
        j = json.loads(data)
        zval = j.get('zval')
        self.ui.lineEdit_10.setText(str(zval))
        pass

    def pressGetJogSpeed(self, data):
        j = json.loads(data)
        jogSpeed = j.get('jogSpeed')
        self.ui.lineEdit_5.setText(str(jogSpeed))
        pass

    def pressReadAllPRPath(self,data):
        j = json.loads(data)
        #prs = j.get('prs')
        item = PrPathInfo()
        #for i in prs:
        item.pathNo = j.get('pathNo')
        item.puu = j.get('puu')
        StaticInfo.g_prpath_list.append(item)
        self.ui.listWidget.addItem("PR #" + str(item.pathNo))

    def pressReadPRPathByPathNo(self,data):
        j = json.loads(data)
        pathNo = j.get('pathNo')
        puu = j.get('puu')
        # prOffset = j.get('prOffset')
        self.ui.lineEdit_2.setText(str(pathNo))
        self.ui.lineEdit_3.setText(str(puu))
        if pathNo == 1:
            self.ui.lineEdit_6.setText(str(0))
        else:
            self.ui.lineEdit_6.setText(str(1))
    
    def pressSetPRPath(self,data):
        j = json.loads(data)
        rt = j.get('rt')
        msg = j.get('msg')
        messagebox.showwarning("提示",msg)
        pass

    def pressScanOutline(self):
        while True:
            if len(self.scanList) == 0:
                # self.scanPts.reshape((-1,1,2))
                # cv2.fillConvexPoly(self.polyMat,self.scanPts,(0,255,0))
                # cv2.polylines()
                cv2.imwrite("/opt/qjs/gwcm/out.jpg", self.scanMat)
                cv2.imwrite("/opt/qjs/gwcm/show.jpg", self.videoMat)
                pix = QPixmap("/opt/qjs/gwcm/show.jpg")
                self.ui.label_13.setScaledContents(True)
                self.ui.label_13.setPixmap(pix)
                break
            p = self.scanList[0]
            x = p[1]
            # 原点从左上角开始
            y = self.scanMat.shape[0] - p[2]
            vx = int(x / 10)
            vy = int(y / 10)
            print("No %d,X %d,Y %d" % (p[0],x,y))
            # dp = (x,y)
            # vp = (vx,vy)
            # self.cvHelper.DrawCircleAsync(self.scanMat, dp,5)
            # self.cvHelper.DrawCircleAsync(self.videoMat, vp,3)
            # self.scanPts.append([x,y])
            # np.append(self.scanPts, np.array([x,y]), axis=0)
            cv2.circle(img=self.videoMat, center=(vx,vy),radius= 5, color=(0, 255, 0, 0), thickness=-1)
            cv2.circle(img=self.scanMat, center=(x,y),radius= 3, color=(0, 255, 0, 0), thickness=-1)
            cv2.imshow("Scan",self.videoMat)
            if len(self.scanList) > 0:
                self.scanList.pop(0)
            cv2.waitKey(5)
        
    def pressScanOutline_b(self,data):
        j = json.loads(data)
        rt = int(j.get('rt'))
        scanframe_count = j.get('scanframe_count')
        scanframe_no = j.get('scanframe_no')
        h_point_x = j.get('h_point_x')
        h_point_y = j.get('h_point_y')
        l_point_x = j.get('l_point_x')
        l_point_y = j.get('l_point_y')
        
        if rt == 1:
            self.scanList.append((scanframe_no,h_point_x,h_point_y))
            self.scanList.append((scanframe_no,l_point_x,l_point_y))
            # self.scanPts.append((h_point_x,h_point_y))
            # self.scanPts.append((l_point_x,l_point_y))
            print("No %d,X %d,Y %d" % (scanframe_no,h_point_x,h_point_y))
            # cv2.circle(img=self.scanMat, center=(h_point_x, h_point_y),radius= 3, color=(0, 255, 0, 0), thickness=-1)
            # cv2.circle(img=self.scanMat, center=(l_point_x,l_point_y),radius= 3, color=(0, 255, 0, 0), thickness=-1)
            hx = int(h_point_x / 10)
            hy = int(h_point_y / 10)
            lx = int(l_point_x / 10)
            ly = int(l_point_y / 10)
            # 原点从左上角开始
            hy = self.scanMat.shape[0] - hy
            ly = self.scanMat.shape[0] - ly
            # cv2.circle(img=self.videoMat, center=(hx,hy),radius= 3, color=(0, 255, 0, 0), thickness=-1)
            # cv2.circle(img=self.videoMat, center=(lx,ly),radius= 3, color=(0, 255, 0, 0), thickness=-1)
            # cv2.imwrite("./show.jpg", self.videoMat)

            self.cvHelper.DrawCircleAsync(self.videoMat, (hx,hy),3)
            self.cvHelper.DrawCircleAsync(self.videoMat, (lx,ly),3)
            self.cvHelper.ImWriteAsync(self.videoMat, "/opt/qjs/gwcm/show.jpg")
            #cv2.imshow("Scan",self.videoMat)
        elif rt == 2:
            print("Scan Outline End")
            th = threading.Thread(target=StaticInfo.g_tab1.scanOut, args=[self.scanMat,self.scanList,self.ui.label_13])
            th.start()
        else:
            messagebox.showwarning("提示","扫描失败")
            self.scanList.clear()
        pass
    
    def scanOut(self,mat,list,color):
        cv2.waitKey(1000)
        # pix = QPixmap("/opt/qjs/gwcm/show.jpg")
        # qpix.setScaledContents(True)
        # qpix.setPixmap(pix)
        for p in list:
            x = p[1]
            # 原点从左上角开始
            y = mat.shape[0] - p[2]
            #print("No %d,X %d,Y %d" % (p[0],p[1],p[2]))
            if color == 1:
                self.cvHelper.DrawCircle(mat, (x,y),5)
            else :
                self.cvHelper.DrawCircle2(mat, (x,y),5)
            #cv2.circle(img=mat, center=(x,y),radius= 5, color=(0, 255, 0, 0), thickness=-1)
            #cv2.imshow('Scan', mat)
        
        self.cvHelper.ImWrite(mat, self.outImgPath)
        self.scanList.clear()
        # cv2.imshow('scan', mat)
        pass

    def pressReadAllDoStatus(self,data):
        j = json.loads(data)
        rdataHex = j.get('rdataHex')
        self.ui.lineEdit_8.setText(str(rdataHex))
        DO1 = j.get('DO1')
        if DO1 == 1:
            self.isOpenDO1 = 1
            self.ui.pushButton_35.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO1 = 0
            self.ui.pushButton_35.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DO2 = j.get('DO2')
        if DO2 == 1:
            self.isOpenDO2 = 1
            self.ui.pushButton_36.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO2 = 0
            self.ui.pushButton_36.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO3 = j.get('DO3')
        if DO3 == 1:
            self.isOpenDO3 = 1
            self.ui.pushButton_37.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO3 = 0
            self.ui.pushButton_37.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DO4 = j.get('DO4')
        if DO4 == 1:
            self.isOpenDO4 = 1
            self.ui.pushButton_38.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO4 = 0
            self.ui.pushButton_38.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DO5 = j.get('DO5')
        if DO5 == 1:
            self.isOpenDO5 = 1
            self.ui.pushButton_39.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO5 = 0
            self.ui.pushButton_39.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO6 = j.get('DO6')
        if DO6 == 1:
            self.isOpenDO6 = 1
            self.ui.pushButton_40.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO6 = 0
            self.ui.pushButton_40.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO7 = j.get('DO7')
        if DO7 == 1:
            self.isOpenDO7 = 1
            self.ui.pushButton_41.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO7 = 0
            self.ui.pushButton_41.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO8 = j.get('DO8')
        if DO8 == 1:
            self.isOpenDO8 = 1
            self.ui.pushButton_42.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO8 = 0
            self.ui.pushButton_42.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO9 = j.get('DO9')
        if DO9 == 1:
            self.isOpenDO9 = 1
            self.ui.pushButton_43.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO9 = 0
            self.ui.pushButton_43.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO10 = j.get('DO10')
        if DO10 == 1:
            self.isOpenDO10 = 1
            self.ui.pushButton_44.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO10 = 0
            self.ui.pushButton_44.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO11 = j.get('DO11')
        if DO11 == 1:
            self.isOpenDO11 = 1
            self.ui.pushButton_45.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO11 = 0
            self.ui.pushButton_45.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO12 = j.get('DO12')
        if DO12 == 1:
            self.isOpenDO12 = 1
            self.ui.pushButton_46.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO12 = 0
            self.ui.pushButton_46.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO13 = j.get('DO13')
        if DO13 == 1:
            self.isOpenDO13 = 1
            self.ui.pushButton_47.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO13 = 0
            self.ui.pushButton_47.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        
        DO14 = j.get('DO14')
        if DO14 == 1:
            self.isOpenDO14 = 1
            self.ui.pushButton_48.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO14 = 0
            self.ui.pushButton_48.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO15 = j.get('DO15')
        if DO15 == 1:
            self.isOpenDO15 = 1
            self.ui.pushButton_49.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO15 = 0
            self.ui.pushButton_49.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO16 = j.get('DO16')
        if DO16 == 1:
            self.isOpenDO16 = 1
            self.ui.pushButton_50.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO16 = 0
            self.ui.pushButton_50.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO17 = j.get('DO17')
        if DO17 == 1:
            self.isOpenDO17 = 1
            self.ui.pushButton_51.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO17 = 0
            self.ui.pushButton_51.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO18 = j.get('DO18')
        if DO18 == 1:
            self.isOpenDO18 = 1
            self.ui.pushButton_52.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO18 = 0
            self.ui.pushButton_52.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO19 = j.get('DO19')
        if DO19 == 1:
            self.isOpenDO19 = 1
            self.ui.pushButton_53.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO19 = 0
            self.ui.pushButton_53.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO20 = j.get('DO20')
        if DO20 == 1:
            self.isOpenDO20 = 1
            self.ui.pushButton_54.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO20 = 0
            self.ui.pushButton_54.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO21 = j.get('DO21')
        if DO21 == 1:
            self.isOpenDO21 = 1
            self.ui.pushButton_55.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO21 = 0
            self.ui.pushButton_55.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO22 = j.get('DO22')
        if DO22 == 1:
            self.isOpenDO22 = 1
            self.ui.pushButton_56.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO22 = 0
            self.ui.pushButton_56.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO23 = j.get('DO23')
        if DO23 == 1:
            self.isOpenDO23 = 1
            self.ui.pushButton_57.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO23 = 0
            self.ui.pushButton_57.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO24 = j.get('DO24')
        if DO24 == 1:
            self.isOpenDO24 = 1
            self.ui.pushButton_58.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO24 = 0
            self.ui.pushButton_58.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO25 = j.get('DO25')
        if DO25 == 1:
            self.isOpenDO25 = 1
            self.ui.pushButton_59.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO25 = 0
            self.ui.pushButton_59.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO26 = j.get('DO26')
        if DO26 == 1:
            self.isOpenDO26 = 1
            self.ui.pushButton_60.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO26 = 0
            self.ui.pushButton_60.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO27 = j.get('DO27')
        if DO27 == 1:
            self.isOpenDO27 = 1
            self.ui.pushButton_61.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO27 = 0
            self.ui.pushButton_61.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO28 = j.get('DO28')
        if DO28 == 1:
            self.isOpenDO28 = 1
            self.ui.pushButton_62.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO28 = 0
            self.ui.pushButton_62.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO29 = j.get('DO29')
        if DO29 == 1:
            self.isOpenDO29 = 1
            self.ui.pushButton_63.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO29 = 0
            self.ui.pushButton_63.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO30 = j.get('DO30')
        if DO30 == 1:
            self.isOpenDO30 = 1
            self.ui.pushButton_64.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO30 = 0
            self.ui.pushButton_64.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO31 = j.get('DO31')
        if DO31 == 1:
            self.isOpenDO31 = 1
            self.ui.pushButton_65.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO31 = 0
            self.ui.pushButton_65.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DO32 = j.get('DO32')
        if DO32 == 1:
            self.isOpenDO32 = 1
            self.ui.pushButton_66.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.isOpenDO32 = 0
            self.ui.pushButton_66.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        
        
        

    def pressReadAllDIStatus(self,data):
        j = json.loads(data)
        rdataHex = j.get('rdataHex')
        self.ui.lineEdit_9.setText(str(rdataHex))
        DI1 = j.get('DI1')
        if DI1 == 1:
            
            self.ui.pushButton_124.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_124.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DI2 = j.get('DI2')
        if DI2 == 1:
            
            self.ui.pushButton_125.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_125.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI3 = j.get('DI3')
        if DI3 == 1:
            
            self.ui.pushButton_126.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_126.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DI4 = j.get('DI4')
        if DI4 == 1:
            
            self.ui.pushButton_127.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_127.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

        DI5 = j.get('DI5')
        if DI5 == 1:
            
            self.ui.pushButton_128.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_128.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI6 = j.get('DI6')
        if DI6 == 1:
            
            self.ui.pushButton_129.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_129.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI7 = j.get('DI7')
        if DI7 == 1:
            
            self.ui.pushButton_130.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_130.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI8 = j.get('DI8')
        if DI8 == 1:
            
            self.ui.pushButton_131.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_131.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI9 = j.get('DI9')
        if DI9 == 1:
            
            self.ui.pushButton_132.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_132.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI10 = j.get('DI10')
        if DI10 == 1:
            
            self.ui.pushButton_133.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_133.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI11 = j.get('DI11')
        if DI11 == 1:
            
            self.ui.pushButton_134.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_134.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI12 = j.get('DI12')
        if DI12 == 1:
            
            self.ui.pushButton_135.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_135.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI13 = j.get('DI13')
        if DI13 == 1:
            
            self.ui.pushButton_136.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            
            self.ui.pushButton_136.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        
        DI14 = j.get('DI14')
        if DI14 == 1:
            
            self.ui.pushButton_137.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_137.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI15 = j.get('DI15')
        if DI15 == 1:
            self.ui.pushButton_138.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_138.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI16 = j.get('DI16')
        if DI16 == 1:
            self.ui.pushButton_139.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_139.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI17 = j.get('DI17')
        if DI17 == 1:
            self.ui.pushButton_140.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_140.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI18 = j.get('DI18')
        if DI18 == 1:
            self.ui.pushButton_141.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_141.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI19 = j.get('DI19')
        if DI19 == 1:
            self.ui.pushButton_142.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_142.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI20 = j.get('DI20')
        if DI20 == 1:
            self.ui.pushButton_143.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_143.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI21 = j.get('DI21')
        if DI21 == 1:
            self.ui.pushButton_144.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_144.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI22 = j.get('DI22')
        if DI22 == 1:
            self.ui.pushButton_145.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_145.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI23 = j.get('DI23')
        if DI23 == 1:
            self.ui.pushButton_146.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_146.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI24 = j.get('DI24')
        if DI24 == 1:
            self.ui.pushButton_147.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_147.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI25 = j.get('DI25')
        if DI25 == 1:
            self.ui.pushButton_148.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_148.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI26 = j.get('DI26')
        if DI26 == 1:
            self.ui.pushButton_149.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_149.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI27 = j.get('DI27')
        if DI27 == 1:
            self.ui.pushButton_150.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_150.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI28 = j.get('DI28')
        if DI28 == 1:
            self.ui.pushButton_151.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_151.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI29 = j.get('DI29')
        if DI29 == 1:
            self.ui.pushButton_152.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_152.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI30 = j.get('DI30')
        if DI30 == 1:
            self.ui.pushButton_153.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_153.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI31 = j.get('DI31')
        if DI31 == 1:
            self.ui.pushButton_154.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_154.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")
        
        DI32 = j.get('DI32')
        if DI32 == 1:
            self.ui.pushButton_155.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 255, 0);")
        else :
            self.ui.pushButton_155.setStyleSheet("background-color: rgb(191, 191, 191);color: rgb(0, 0, 0);")

