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
        :param Index: 1  231  2  233
        :return: ssh
        '''
        if Index == 1:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.3.231',22,self.username, self.password)
            except Exception:
                print (Exception)
            return ssh
        elif Index == 2:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('172.31.3.233',22,self.username, self.password)
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

            sftp = paramiko.SFTPClient.from_transport(trans)
            sftp.put(localpath,remotepath)
            time.sleep(2)
            trans.close()

        elif Index == 2 :
            try:
                trans = paramiko.Transport(('172.31.3.233',22))
                trans.connect(username=self.username,password=self.password)
            except Exception as e:
                print (e)

            sftp = paramiko.SFTPClient.from_transport(trans)
            sftp.put(localpath,remotepath)
            time.sleep(2)
            trans.close()
            QApplication.processEvents()

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
        if self.printtomcat() == 1:
            print('部署环境为：'+ self.ui.environment.currentText())

            # 部署单个文件
            if self.filenumber() == 1:
                self.onefile(1,self.filetype())

            #部署web.zip
            elif self.filenumber() == 2:
                #连接231 部署web.zip
                self.zip(1)
                # print('222')

            #判断是否需要重启
            if self.needrestart() == 1:
                ssh = self.connect(1)
                stdin, stdout, stderr = ssh.exec_command('service  tomcat_iorder_appsvr  restart',get_pty=False)
                for line in stdout:
                    print (line.strip('\n'))
                time.sleep(5)
                ssh.close()
            elif self.needrestart() == 2:
                time.sleep(2)
            QApplication.processEvents()
        elif self.printtomcat() == 2:
            print('部署环境为：'+ self.ui.environment.currentText())

            # 部署单个文件
            if self.filenumber() == 1:
                self.onefile(2,self.filetype())

            # 部署web.zip
            elif self.filenumber()== 2:
                #连接231 部署web.zip
                # print('222 222')
                self.zip(2)

            # 判断是否需要重启
            if self.needrestart() == 1:
                ssh = self.connect(2)
                stdin, stdout, stderr = ssh.exec_command('service  tomcat_iorder_appsvr  restart',get_pty=False)
                for line in stdout:
                    print (line.strip('\n'))
                time.sleep(2)
                ssh.close()
                self.ui.log.setPlainText('部署完成,服务器重启中，请稍候')
            elif self.needrestart() == 2:
                time.sleep(2)
                self.ui.log.setPlainText('部署完成')
            QApplication.processEvents()

if __name__=="__main__":
	app = QApplication(sys.argv)
	win = Main()
	win.show()
	sys.exit(app.exec_())
