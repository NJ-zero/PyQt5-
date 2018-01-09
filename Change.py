#coding=utf-8
#author='Shichao-Dong'

import sys
from PyQt5.QtWidgets import *
from FirstMainWin import Ui_Form
import time
import paramiko


class Main(QMainWindow,Ui_Form):

    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Waiqin365-DATT-V1.0.0')
        self.password = 'ZKwaiqin123'
        self.username='root'

        self.ui.environment.activated.connect(self.printtomcat)
        self.ui.filename.editingFinished.connect(self.filename)
        self.ui.filenumber.activated.connect(self.filenumber)
        self.ui.filetype.activated.connect(self.filetype)
        self.ui.restart.activated.connect(self.needrestart)
        self.ui.start.clicked.connect(self.start)


    def printtomcat(self):
        '''
        根据选择的环境返回Index值，供下面connect使用
        1   231
        2   233
        '''
        print(self.ui.environment.currentText())
        tomcat = self.ui.environment.currentIndex()
        self.ui.log.setPlainText('部署的环境为：'+self.ui.environment.currentText())
        return tomcat


    def filenumber(self):
        '''
        根据选择的文件数量：单个文件还是web.zip,返回Index供下面onefile和zip使用
        1  单个文件
        2  web.zip
        '''
        print(self.ui.filenumber.currentIndex())
        filenumber = self.ui.filenumber.currentIndex()
        self.ui.log.setPlainText('文件类型为：'+self.ui.filenumber.currentText())
        return filenumber


    def filetype(self):
        '''
        根据选择的文件类型：平台文件还是应用文件，自动加上前缀 /home/...web/WEB-INFO/class  还是 /home/...web/
        1  应用文件
        2  平台文件
        '''
        print(self.ui.filetype.currentIndex())
        filetype = self.ui.filetype.currentIndex()
        self.ui.log.setPlainText('文件为：'+self.ui.filetype.currentText())
        return filetype


    def filename(self):
        '''
        返回填写的filename
        '''
        print(self.ui.filename.text())
        filename = self.ui.filename.text()
        self.ui.log.setPlainText('文件名为：'+self.ui.filename.text())
        return filename

    def localfile(self):
        '''
        返回local,即文件所在路径
        :return:
        '''
        print(self.ui.filename.text())
        filename = self.ui.filename.text()
        localfile = 'D:/file/'+ filename
        print(localfile)
        return localfile

    def path(self):
        '''
        返回填写的filepath 文件路径
        '''
        print(self.ui.filepath.toPlainText())
        filepath = self.ui.filepath.toPlainText()

        return filepath

    def needrestart(self):
        '''
        根据所选，返回Index，供下面使用是否需要重启
        1 需要
        2 不需要
        '''
        need = self.ui.restart.currentIndex()
        print(need)
        return need

    def connect(self,Index):
        '''
        根据传入的Index连接服务器
        :param Index: 1  3.231  2  3.233   3  4.231  4 4.233
        :return: ssh
        '''
        if Index == 1:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.3.231',22,self.username, self.password)
                QApplication.processEvents()
            except Exception:
                print (Exception)
            return ssh
        elif Index == 2:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.3.233',22,self.username, self.password)
                QApplication.processEvents()
            except Exception:
                print (Exception)
            return ssh
        elif Index == 3:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.4.231',22,self.username, self.password)
                QApplication.processEvents()
            except Exception:
                print (Exception)
            return ssh
        elif Index == 4:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.4.233',22,self.username, self.password)
                QApplication.processEvents()
            except Exception:
                print (Exception)
            return ssh


    def trans(self,Index,localpath,remotepath):
        '''
        根据传入的Index连接服务器并上传文件
        :param Index:
        :return:
        '''
        if Index == 1:
            try:
                trans = paramiko.Transport(('172.31.3.231',22))
                trans.connect(username=self.username,password=self.password)
            except Exception as e:
                print (e)
        elif Index == 2 :
            try:
                trans = paramiko.Transport(('172.31.3.233',22))
                trans.connect(username=self.username,password=self.password)
            except Exception as e:
                print (e)
        elif Index == 3 :
            try:
                trans = paramiko.Transport(('172.31.4.231',22))
                trans.connect(username=self.username,password=self.password)
            except Exception as e:
                print (e)
        elif Index == 4 :
            try:
                trans = paramiko.Transport(('172.31.4.233',22))
                trans.connect(username=self.username,password=self.password)
            except Exception as e:
                print (e)

        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.put(localpath,remotepath)
        QApplication.processEvents()
        time.sleep(2)
        trans.close()

    def onefile(self,Index,type):
        '''
        一个文件，根据传入的type判断平台文件还是应用文件，拼接完整的路径
        :param type: 1 应用文件  2  平台文件
        :param type: Index  1  连接231  2  连接233
        :return:
        '''
        if type == 1:
            remotepath = '/home/iorder_appsvr/iorder_appsvr/web/WEB-INF/classes' + str(self.path())
            self.ui.log.setPlainText('文件路径为：'+ remotepath)
            filename = self.filename()
            self.localfile()
            bak = filename + time.strftime("%y%m%d") + 'bak'
            cmd = 'cd  {0};mv {1}  {2}'.format(remotepath,self.filename(),bak)
            #备份并上传替换文件
            print(cmd)
            self.ui.log.setPlainText('备份替换文件')
            QApplication.processEvents()

            # 根据Index 连接对应的环境
            ssh = self.connect(Index)
            stdin, stdout, stderr = ssh.exec_command(cmd,get_pty=True)
            for line in stdout:
                print (line.strip('\n'))
            ssh.close()
            QApplication.processEvents()
            remotefile = '/home/iorder_appsvr/iorder_appsvr/web/WEB-INF/classes' + str(self.path())+str(self.filename())
            self.trans(Index,self.localfile(),remotefile)
            self.ui.log.setPlainText('文件上传成功')
            return cmd,filename,remotepath

        elif type == 2:
            remotepath = '/home/iorder_appsvr/iorder_appsvr/web' + str(self.path())
            self.ui.log.setPlainText('文件路径为：'+ remotepath)
            filename = self.filename()
            bak = filename + time.strftime("%y%m%d") + 'bak'
            cmd = 'cd  {0} ;mv {1}  {2}'.format(remotepath,self.filename(),bak)
            print(cmd)
            self.ui.log.setPlainText('备份替换文件')
            QApplication.processEvents()

            ssh = self.connect(Index)
            stdin, stdout, stderr = ssh.exec_command(cmd,get_pty=True)

            for line in stdout:
                print (line.strip('\n'))
            ssh.close()
            QApplication.processEvents()
            remotefile = '/home/iorder_appsvr/iorder_appsvr/web' + str(self.path())+str(self.filename())
            self.trans(Index,self.localfile(),remotefile)
            self.ui.log.setPlainText('文件上传成功')
            return cmd,filename,remotepath


    def zip(self,Index):
        '''
        web.zip包直接复制到opt后解压后复制
        Index  用来判断231 还是 233
        :return:
        '''
        cmd = 'cd /opt;rm -rf web;mkdir web;ls'
        # cd 到opt下创建新的web目录
        ssh = self.connect(Index)
        stdin, stdout, stderr = ssh.exec_command(cmd,get_pty=True)
        for line in stdout:
                print (line.strip('\n'))
        ssh.close()
        QApplication.processEvents()

        #上传文件至opt/web 并解压
        remotepath = '/opt/web/{}'.format(self.filename())
        localpath = r'D:/file/{}'.format(self.filename())
        print(remotepath,localpath)
        self.trans(Index,localpath,remotepath)
        self.ui.log.setPlainText('压缩包文件上传成功')

        QApplication.processEvents()
        cmd1 = 'cd /opt/web;ls;unzip {};rm -rf  {}'.format(self.filename(),self.filename())
        ssh = self.connect(Index)
        stdin, stdout, stderr = ssh.exec_command(cmd1,get_pty=True)
        for line in stdout:
                print (line.strip('\n'))
        time.sleep(2)
        #复制解压后的文件
        cmd2 = '\cp -Rf /opt/web/*    /home/iorder_appsvr/iorder_appsvr/'
        stdin, stdout, stderr = ssh.exec_command(cmd2,get_pty=True)
        for line in stdout:
                print (line.strip('\n'))
        ssh.close()
        QApplication.processEvents()

        self.ui.log.setPlainText('复制zip替换文件成功')


    def start(self):
        '''
        开始部署  1  部署231   2  部署233
        :return:
        '''
        if self.printtomcat() != 0:
            print('部署环境为：'+ self.ui.environment.currentText())

            # 部署单个文件
            if self.filenumber() == 1:
                if self.filetype()==0:
                    self.ui.log.setPlainText('请选择文件类型')
                else:
                    self.onefile(self.printtomcat(),self.filetype())
            #部署web.zip
            elif self.filenumber() == 2:
                #连接231 部署web.zip
                self.zip(self.printtomcat())
            elif self.filenumber() ==0:
                self.ui.log.setPlainText('请选择文件类型')

            #判断是否需要重启
            if self.needrestart() == 1:
                ssh = self.connect(self.printtomcat())
                stdin, stdout, stderr = ssh.exec_command('service  tomcat_iorder_appsvr  restart',get_pty=False)
                for line in stdout:
                    print (line.strip('\n'))
                time.sleep(5)
                ssh.close()
                self.ui.log.setPlainText('部署完成,服务器重启中，请稍候')
            elif self.needrestart() == 2:
                self.ui.log.setPlainText('部署完成,不需要重启服务器')
                time.sleep(2)
            elif self.needrestart() == 0:
                self.ui.log.setPlainText('未选择是否重启,默认不重启服务器')
                time.sleep(2)
            QApplication.processEvents()

        else:
            self.ui.log.setPlainText('请选择需要部署的环境')

if __name__=="__main__":
	app = QApplication(sys.argv)
	win = Main()
	win.show()
	sys.exit(app.exec_())
