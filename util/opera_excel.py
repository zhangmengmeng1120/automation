# encoding:utf-8
import xlrd

class OperaExcel:

    def __init__(self,file_path=None,i=None):
        if file_path == None or i == None:
            self.file_path = '../config/case.xls'
            i = 0
        else:
            self.file_path = file_path
            i = i
        self.excel = self.get_excel()
        self.data = self.get_sheet(i)

    def get_excel(self):
        '''
        获取Excel
        :return:
        '''
        excel = xlrd.open_workbook(self.file_path)
        return excel
    def get_sheet(self,i):
        '''
        获取sheet行
        :param i:
        :return:
        '''
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取行数
        :return:
        '''
        lines = self.data.nrows
        return lines

    def get_cell(self,row,cel):
        '''
        获取数据
        :param row:
        :param cel:
        :return:
        '''
        data = self.data.cell(row,cel).value
        return data

if __name__ == '__main__':
    opera = OperaExcel()
    print opera.get_lines()
    print opera.get_cell(3,4)