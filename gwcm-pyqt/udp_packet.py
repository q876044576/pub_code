from socket import *
from time import ctime
import queue
import time
from static_info import StaticInfo

#from tab1 import Tab1


class UdpPacket:
    def __init__(self, host, port):
        self.Host = host
        self.Port = port
        self.Addr = (host, port)
        self.Udp_conn = ()
        self.CAddr = ('', 0)
        self.Udp_list = []
        pass

    def OpenUdpListen(self):
        self.OpenUdpServer()
    
    def UdpHandler(self):
        while True:
            if len(self.Udp_list) > 0:
                data = self.Udp_list[0]
                StaticInfo.g_tab1.pressResp(data)
                
                #Tab1.PressResp(StaticInfo.g_tab1,data)
                self.Udp_list.pop(0)
                #print('222222222222 %d' % (len(self.Udp_list)))
            else:
                time.sleep(0.1)
        pass
        

    def OpenUdpServer(self):
        
        self.Udp_conn = socket(AF_INET, SOCK_DGRAM)
        self.Udp_conn.bind(self.Addr)
        BUFSIZE = 1024
        while True:
            data,caddr = self.Udp_conn.recvfrom(BUFSIZE)
            # if data is None:
            #     break
            jf = data.decode('utf-8')
            print("Recv[%s]: %s" % (caddr.__str__(),jf))
            self.Udp_list.append(jf)
            # sData = "{'code':'0','msg':'ok'}"
            # sData = []
            # sData.append(0x48)
            # sData.append(0x54)
            # sData.append(0x00)
            # sData.append(0x01)
            # sData.append(0x16)
            
            # if data is not None:
            #     self.Udp_conn.sendto(sData.encode(encoding='utf-8'), caddr)
        # self.Udp_conn.close()
        pass
    
    def UdpSendTo(self, conn, addr, data):
        conn.sendto(data, addr)
        pass

    def UdpNewConnSendTo(self,bindAddr,sendAddr, sData):
        # print(bindAddr.__str__())
        conn = socket(AF_INET, SOCK_DGRAM)
        conn.bind(bindAddr)
        conn.sendto(sData.encode(encoding='utf-8'), sendAddr)
        pass

    



