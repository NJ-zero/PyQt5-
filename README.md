# PyQt5+Python3

### 自动部署替换文件工具
1.Windows环境电脑一台（本人是WIN7，WIN10没有测试过，应该也没问题）
2.Python 3.4.3，这是基本啦，关于python的安装这边就不说啦
3.PyQt5安装 ,可以去官网下载安装，也可以pip install 安装
4.paramiko安装，直接pip install paramiko（看到很多人装这个库遇到很多问题，可能我是幸运的，一下子就装好了）
5.配置pycharm，备注（这个主要用于将Qt Designer设计出来的ui文件转换为py文件，主要参考了 CSDN 上一位小伙伴的文章），
配置完了可以直接将设计好的ui文件，转换为py文件，非常方便

#### 主界面如下
![image](https://github.com/NJ-zero/PyQt5-/edit/master/jiemian.png)
打包生成EXE文件只需要两个步骤

#### 1.安装PyInstaller

pip install PyInstaller

#### 2.打包
pyinstaller -F -w  change.py

完成后会在同目录的dist文件夹中生成一个同名的.exe文件，双击这个exe文件，运行效果和直接使用编辑器运行脚本效果一样

在其他电脑上使用时，直接将dist目录拷贝过去即可，我这边加了platforms是因为在其他电脑运行报错，paltforms文件夹来自于

C:\Python34\Lib\site-packages\PyQt5\plugins\platforms
