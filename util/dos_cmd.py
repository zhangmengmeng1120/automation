#!/usr/bin/python
# encoding:utf-8
import os


class DosCmd:
    def excute_cmd(self,command):
        '''
        执行终端命令
        :param command:
        :return:
        '''
        result = os.popen(command).readlines()

        return result
