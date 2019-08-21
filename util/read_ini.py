# encoding:utf-8
import ConfigParser


class ReadIni:

    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = '../config/base_element.ini'
        else:
            self.file_path=file_path
        self.read_ini = self.read_ini()
    def read_ini(self):
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self,key,section=None):
        if section == None:
            section = 'login_element'
        else:
            section = section
        data = self.read_ini.get(section,key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni('../config/login.ini')
    print read_ini.get_value('edit_business','login_element')
