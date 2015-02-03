import sublime
import sublime_plugin


class LineCoolCommand(sublime_plugin.TextCommand):


    
    def run(self, edit):
        sublime.view.sel()
        
        for sel in self.view.sel():
            if not sel.empty():
                print self.view.word( self.view.full_line(sel) ) 
            else:
                print 'empty'


if __name__ == '__main__':
    sublime.view.run_command('linecool')
        
