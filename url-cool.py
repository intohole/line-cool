#coding=utf-8


import sublime
import sublime_plugin
import webbrowser
import re 
import sys


class UrlCoolCommand(sublime_plugin.TextCommand):

    regex = re.compile(
        r"^[\w\d]+(\.[\w\d]+){0,}\.[\w\d]+$" 
        , re.IGNORECASE
    )

    def run(self , edit):
        content = self.view.substr(sublime.Region(0, self.view.size()))
        urls = self.regex.findall(content)
        for url in urls:
            sys.stderr.write(url)
            sys.stderr.flush()
            # webbrowser.open(url)