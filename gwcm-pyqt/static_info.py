#coding = 'utf-8'
import sys
import platform

class StaticInfo:
    g_dst_addr = ()
    g_src_addr = ()
    g_prpath_list = []
    g_tab1 = ()
    g_udp_packte = ()
    g_app = ()
    def __init__():
        pass
    
    def InitVal():
        StaticInfo.g_dst_addr = ('192.168.10.101', 10080)
        if (platform.system() == "Windows"):
            StaticInfo.g_dst_addr = ('192.168.22.68', 10080)
        StaticInfo.g_src_addr = ('192.168.10.101', 10070)
        if (platform.system() == "Windows"):
            StaticInfo.g_src_addr = ('192.168.22.137', 10070)
        pass