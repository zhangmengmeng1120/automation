#!/usr/bin/python
# encoding:utf-8
from dos_cmd import DosCmd
import threading

class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.appium_port_list = self.create_port(4700,self.device_list)
        self.bootstrap_port_list = self.create_port(5700,self.device_list)

    def get_devices(self):
        '''
        获取设备信息
        :return:
        '''
        devices_list = []
        result_list = self.dos.excute_cmd('/Users/zhangmengmeng/software/platform-tools/adb devices')
        if len(result_list)>2:
            for i in result_list:
                if 'List' in i or 'device' not in i:
                    continue
                devices_info = i.split('\t')
                if 'device' in devices_info[1]:
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def port_is_used(self,port):
        self.dos = DosCmd()
        result = self.dos.excute_cmd('netstat -an | grep %s'%port)
        if len(result)>0:
            flag = True
        else:
            flag = False
        return flag

    def create_port(self,start_port=4700,device_list=None):
        port_list = []
        if len(device_list) > 0:
            while len(device_list) != len(port_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                    start_port +=1
            return port_list
        else:
            return '不存在可用的设备信息，无法生成appium端口'


    def create_command(self):
        '''
        android 启动appium服务
        appium -p 4700 -bp 4701 -u 168.98.34.12:1234
        :return:
        '''
        command_list = []
        for i in range(len(self.appium_port_list)):
            command_list.append('appium -p %s -bp %s -U %s'%(self.appium_port_list[i],self.bootstrap_port_list[i],self.device_list[i]))
        return command_list


    def start_server(self,i):
        command_list = self.create_command()
        self.dos.excute_cmd(command_list[i])

    def start1(self):
        for i in range(len(self.create_command())):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()
