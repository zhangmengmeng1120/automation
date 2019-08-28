# encoding:utf-8
from util.get_by_local import GetByLocal
from key_word.get_data import GetData


class OperaCaseToJson:
    def __init__(self,*args):
        self.type = args[0]
        self.get_by_local = GetByLocal()
        # args[2]表示读哪个sheet，int类型
        # args[1]表示测试Excel名称，类似../config/name.xls
        self.data = GetData(args[1],args[2])
    # 将Excel中的数据转换成json
    def opera_case(self):
        lines = self.data.get_case_line()
        line_infos = {}
        for i in range(1, lines):
            section = self.data.get_section(i)
            if section != 'h5_page_element' and section != None:
                section += '_' + self.type
            file_path = self.data.get_file_path(i)
            if file_path != None:
                file_path = '../config/' + self.data.get_file_path(i)
            handle_step = self.data.get_handle_step(i)
            handle_value = self.data.get_hadle_value(i)
            element_key = self.data.get_element_key(i)
            if line_infos.has_key(self.data.get_case_no(i)):
                line_infos[self.data.get_case_no(i)].append({
                    'file_path': file_path,  # 元素路径
                    'section': section,  # 模块名称
                    'handle_step': handle_step,  # 操作步骤
                    'handle_value': handle_value,  # 操作值
                    'element_key': element_key # 操作值
                })
            else:
                line_infos[self.data.get_case_no(i)] = []
                line_infos[self.data.get_case_no(i)].append({
                    'file_path': file_path,  # 元素路径
                    'section': section,  # 模块名称
                    'handle_step': handle_step,  # 操作步骤
                    'handle_value': handle_value,  # 操作值
                    'element_key': element_key  # 操作值
                })
        return line_infos

if __name__ == '__main__':
    import json
    opera = OperaCaseToJson('android','../config/case.xls',9)
    line_infos = opera.opera_case()
