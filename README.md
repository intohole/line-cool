sublime 编写历程
=============


+ 实现功能点
    * 主要是经常会遇到两个段落（字段），进行对比 ， 但是采用excel表格比较笨重，所以趁此机会学习sublime plugin编写




注意点
=============

+ sublime 控件一般放在 ## C:\Users\用户名\AppData\Roaming\Sublime Text 2\Packages##
+ sublime 第一个空间代码:
    * Tools->New Plugin
    
:::code    
    
    import sublime
    import sublime_plugin
    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")

##保存在Packages/下任一目录##
+ 运行方式 CTRL + ` 运行consle ，命令view.run_command('example')
+ eg. ExampleCommand -> LineCoolCommand : view.run_command('line_cool') #去掉command 后缀，命名的驼峰变为下划线
+ 




引用
---------------------
+  <a href="http://mux.alimama.com/posts/541">插件开发</a>