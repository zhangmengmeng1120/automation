#coding:utf-8
from util.opera_excel import OperaExcel

class GetData:
    def __init__(self,*args):
        self.opera_xecel = OperaExcel(file_path=args[0],i=args[1])
    def get_case_line(self):
        '''
        获取case的行数
        :return:
        '''
        lines = self.opera_xecel.get_lines()
        return lines

    def get_case_no(self,row):
        '''
        获取用例编号
        :param row:行
        :return:
        '''
        case_no = self.opera_xecel.get_cell(row,0)
        if case_no == '':
            return None
        return  case_no.encode('utf-8')

    def get_file_path(self,row):
        '''
        获取元素路径
        :param row:行
        :return:
        '''
        file_path = self.opera_xecel.get_cell(row,1)
        if file_path == '':
            return None
        return  file_path.encode('utf-8')

    def get_section(self,row):
        '''
        获取模块名称
        :param row:行
        :return:
        '''
        section = self.opera_xecel.get_cell(row,2)
        if section == '':
            return None
        return  section.encode('utf-8')

    def get_handle_step(self,row):
        '''
        获取操作步骤里面的操作方法名字
        :param row:行
        :return:
        '''
        method_name = self.opera_xecel.get_cell(row,4)
        return method_name.encode('utf-8')
    def get_element_key(self,row):
        '''
        获取操作元素的key
        :param row:行
        :return:
        '''
        element_key = self.opera_xecel.get_cell(row,5)
        if element_key == '':
            return None
        return element_key.encode('utf-8')
    def get_hadle_value(self,row):
        '''
        获取操作值
        :param row:行
        :return:
        '''
        handle_value = self.opera_xecel.get_cell(row,6)
        if handle_value == '':
            return None
        return handle_value.encode('utf-8')
    def get_expect_file_path(self,row):
        '''
        获取预期元素路径
        :param row:行
        :return:
        '''
        expect_file_path = self.opera_xecel.get_cell(row,7)
        if expect_file_path == '':
            return None
        return  expect_file_path.encode('utf-8')
    def get_expect_section(self,row):
        '''
        获取预期元素模块名称
        :param row:行
        :return:
        '''
        expect_section = self.opera_xecel.get_cell(row,8)
        if expect_section == '':
            return None
        return  expect_section.encode('utf-8')
    def get_expect_element_key(self,row):
        '''
        获取预期元素
        :param row:行
        :return:
        '''
        expect_element_key = self.opera_xecel.get_cell(row,9)
        if expect_element_key == '':
            return None
        return  expect_element_key.encode('utf-8')

    def get_expect_handle_step(self,row):
        '''
        获取预期步骤
        :param row:行
        :return:
        '''
        expect_handle_step = self.opera_xecel.get_cell(row,10)
        if expect_handle_step == '':
            return None
        return  expect_handle_step.encode('utf-8')

    def get_expect_handle_value(self,row):
        '''
        获取预期操作值
        :param row:行
        :return:
        '''
        expect_handle_value = self.opera_xecel.get_cell(row,11)
        if expect_handle_value == '':
            return None
        return  expect_handle_value.encode('utf-8')



