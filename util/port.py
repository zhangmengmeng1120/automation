# encoding:utf-8
from dos_cmd import DosCmd
from server import Server

class Port:
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



if __name__ == '__main__':
    server = Server()
    port = Port()
    print port.create_port(4700,[1,2,3])