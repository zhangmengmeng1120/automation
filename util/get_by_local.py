# encoding:utf-8
from read_ini import ReadIni
class GetByLocal:
    def get_element(self,key,package_name='com.nexttao.shopforce.enterprise',file_path='../config/login.ini',section=None):
        read_ini = ReadIni(file_path)
        local = read_ini.get_value(key,section)
        if '%s' in local:
            local=local%package_name
        return local

