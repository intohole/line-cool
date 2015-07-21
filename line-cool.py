# coding=utf-8

import sublime
import sublime_plugin
import re


class _LineCoolCommand(sublime_plugin.TextCommand):

    # 暂时定义\n三个以上为块分隔符

    __split = re.compile('\n{3,}').split
    placeholder = ""
    line_split = '\t\t'

    def get_cur_content(self):
        '''
        得到当前编辑view中的所有文本
        '''
        return self.view.substr(sublime.Region(0, self.view.size()))

    def run(self, edit):
        contents = []
        content = self.get_cur_content()
        data_container = self.__split(content)
        # 得到每个块内部pieces
        contents = [
            [pic for pic in chunk.split(self._split_item)]
            for chunk in data_container
        ]
        # 获得最大块含有行数
        max_len = max(len(chunk) for chunk in contents)
        # 块数
        chunk_size = len(contents)
        datas = []
        for i in range(max_len):
            items = []
            for j in range(chunk_size):
                item = self.placeholder
                if len(contents[j]) > i:
                    item = contents[j][i]
                items.append(item)
            datas.append(items)
        self.create_new_file(edit, datas)

    def get_datas_gather(self, *argv):
        gathers = []
        sorted_list = sort_list_by_len(*argv)
        for i in range(sorted_list[0][1]):
            _tmp = []
            for ll in sorted_list:
                if ll[1] > i:
                    try:
                        _tmp.index(ll[0][i])
                    except Exception:
                        _tmp.append(ll[0][i])
            gathers.extend(_tmp)
        return gathers

    def sort_list_by_len(self, *argv):
        return sorted([(ll, len(ll)) for ll in argv if ll and hasattr(ll, '__len__')], key=lambda x: x[1], reverse=True)

    def excute_data(self,  contents):
        '''
        data format :
            datas [[line11 content , line12 content  , ....  line1n content] , [line2 content  , line22  , ... line2n] ]
        '''

    def create_new_file(self, edit, contents):
        window = sublime.active_window()  # 得到当前活动window
        view = window.new_file()  # 创建文件view
        view.set_name('new_file')
        # 开始编辑view
        _contents = '\n'.join(
            [
                ''.join(['{0:<30s}'.format(item) for item in items])
                for items in contents
            ]
        )  # 转换为文本
        view.insert(edit, 0, _contents)


class LineCoolCommand(_LineCoolCommand):

    _split_item = '\n'


class BaseCoolCommand(_LineCoolCommand):
    _split_item = None


if __name__ == '__main__':
    sublime.view.run_command('linecool')
