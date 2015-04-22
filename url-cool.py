#coding=utf-8


import sublime
import sublime_plugin
import webbrowser
import re 


class UrlCoolCommand(sublime_plugin.TextCommand):

	regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.IGNORECASE)

	def run(self , edit):
		content = self.view.substr(sublime.Region(0, self.view.size()))
		urls = self.regex.findall(content)
		for url in urls:
			webbrowser.open(url)




