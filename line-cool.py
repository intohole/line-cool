#coding=utf-8

import sublime
import sublime_plugin
import re


class LineCoolCommand(sublime_plugin.TextCommand):

    #暂时定义\n三个以上为块分隔符

    __split = re.compile('\n{3,}').split
    placeholder = "    "
    line_split = '\t\t'
    def get_cur_content(self):
        return self.view.substr(sublime.Region(0, self.view.size()))

    def run(self, edit):
        contents = []
        content = self.get_cur_content()
        data_container = self.__split(content)
        #得到每个块内部pieces
        contents = [
            [pic for pic in chunk.split('\n')]
            for chunk in data_container
        ]
        #获得最大块含有行数
        max_len = max(len(chunk) for chunk in contents)
        #块数
        chunk_size = len(contents)

        datas = []

        for  i in range(max_len):
            items = []
            for j in range(chunk_size):
                item = self.placeholder
                if len(contents[j]) > i:
                    item = contents[j][i]
                items.append(item)
            datas.append(items)
        for items in datas:
            print self.line_split.join(items)


if __name__ == '__main__':
    sublime.view.run_command('linecool')
