# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 415)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../22.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.filename = QtWidgets.QLineEdit(Form)
        self.filename.setGeometry(QtCore.QRect(100, 80, 521, 31))
        self.filename.setObjectName("filename")
        self.filenumber = QtWidgets.QComboBox(Form)
        self.filenumber.setGeometry(QtCore.QRect(403, 31, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filenumber.setFont(font)
        self.filenumber.setStyleSheet("background-color: rgb(255, 212, 253);\n"
"selection-background-color: rgb(90, 112, 255);")
        self.filenumber.setObjectName("filenumber")
        self.filenumber.addItem("")
        self.filenumber.addItem("")
        self.filenumber.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(313, 35, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 48, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.restart = QtWidgets.QComboBox(Form)
        self.restart.setGeometry(QtCore.QRect(100, 248, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.restart.setFont(font)
        self.restart.setStyleSheet("background-color: rgb(255, 212, 253);\n"
"selection-background-color: rgb(90, 112, 255);")
        self.restart.setObjectName("restart")
        self.restart.addItem("")
        self.restart.addItem("")
        self.restart.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 35, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.filetype = QtWidgets.QComboBox(Form)
        self.filetype.setGeometry(QtCore.QRect(528, 31, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filetype.setFont(font)
        self.filetype.setStyleSheet("background-color: rgb(255, 212, 253);\n"
"selection-background-color: rgb(90, 112, 255);")
        self.filetype.setObjectName("filetype")
        self.filetype.addItem("")
        self.filetype.addItem("")
        self.filetype.addItem("")
        self.environment = QtWidgets.QComboBox(Form)
        self.environment.setGeometry(QtCore.QRect(100, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.environment.setFont(font)
        self.environment.setAcceptDrops(False)
        self.environment.setStyleSheet("background-color: rgb(255, 212, 253);\n"
"selection-background-color: rgb(90, 112, 255);\n"
"\n"
"")
        self.environment.setFrame(True)
        self.environment.setObjectName("environment")
        self.environment.addItem("")
        self.environment.addItem("")
        self.environment.addItem("")
        self.filepath = QtWidgets.QTextEdit(Form)
        self.filepath.setGeometry(QtCore.QRect(100, 130, 521, 101))
        self.filepath.setObjectName("filepath")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 64, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(530, 248, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.log = QtWidgets.QTextEdit(Form)
        self.log.setGeometry(QtCore.QRect(100, 310, 521, 71))
        self.log.setObjectName("log")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(23, 340, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "重启服务"))
        self.filenumber.setItemText(0, _translate("Form", "选择文件"))
        self.filenumber.setItemText(1, _translate("Form", "单个文件"))
        self.filenumber.setItemText(2, _translate("Form", "web.zip"))
        self.label_2.setText(_translate("Form", "文件类型"))
        self.label_3.setText(_translate("Form", "文件名"))
        self.restart.setItemText(0, _translate("Form", "重启？？"))
        self.restart.setItemText(1, _translate("Form", "是"))
        self.restart.setItemText(2, _translate("Form", "否"))
        self.label.setText(_translate("Form", "替换环境"))
        self.filetype.setItemText(0, _translate("Form", "选择类型"))
        self.filetype.setItemText(1, _translate("Form", "应用文件"))
        self.filetype.setItemText(2, _translate("Form", "平台文件"))
        self.environment.setStatusTip(_translate("Form", "环境地址"))
        self.environment.setItemText(0, _translate("Form", "选择环境"))
        self.environment.setItemText(1, _translate("Form", "172.31.3.231"))
        self.environment.setItemText(2, _translate("Form", "172.31.3.233"))
        self.label_4.setText(_translate("Form", "文件路径"))
        self.start.setText(_translate("Form", "开始部署"))
        self.pushButton.setText(_translate("Form", "关闭"))
        self.label_6.setText(_translate("Form", "操作日志"))

