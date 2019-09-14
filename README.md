# pycahrm自动添加引号

1. 把`replacess.py`放在python的模块搜索路径里面，推荐`..\Lib\site-packages`目录

1. 在 `pycharm`→`File`→`Settings`→`Tools`→`External Tools`添加一个External Tools（外部工具）

1. Program ：`$JDKPath$`(固定写法)

     Arguments : `-m replacess -v -c -p "$SelectedText$"` (-v -c -p 是三个可选参数，其它参数是固定写法不要改，
  
    -v复制到剪辑版，
  
    -c打印到控制台，
  
    -p自动粘贴到pycahrm)
  
     Working directory ：`$FileDir$`(固定写法)
  
 1. 大功告成！鼠标右键单击 找到External Tools 点击你的工具就可以了。（推荐添加一个快捷键）
