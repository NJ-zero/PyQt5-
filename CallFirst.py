#coding=utf-8
#author='Shichao-Dong'

import sys
from PyQt5.QtWidgets import *
from FirstMainWin import Ui_Form

'''
用于打开FirstMainWin 展现窗口
'''

class Main(QMainWindow,Ui_Form):

    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__=="__main__":
	app = QApplication(sys.argv)
	win = Main()
	win.show()
	sys.exit(app.exec_())
