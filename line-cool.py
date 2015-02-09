# coding=utf-8

import sublime
import sublime_plugin
import re


class LineCoolCommand(sublime_plugin.TextCommand):

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
            [pic for pic in chunk.split('\n')]
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
        self.create_new_file(datas)
        # for items in datas:
        #     print self.line_split.join(items)

    def create_new_file(self, contents):
        window = sublime.active_window()  # 得到当前活动window
        view = window.new_file()  # 创建文件view
        edit = view.begin_edit()  # 开始编辑view
        _contents = '\n'.join(
            [
                ''.join(['{0:<10s}'.format(item) for item in items])
                for items in contents
            ]
        )  # 转换为文本
        view.insert(edit, 0, _contents)
        view.end_edit()


if __name__ == '__main__':
    sublime.view.run_command('linecool')
