# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
import requests
import threading
import time
import os

from websearch import getAllUrl
import re
comp = re.compile("((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(230, 10, 48, 23))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.webUrl = QtWidgets.QLineEdit(self.widget)
        self.webUrl.setGeometry(QtCore.QRect(290, 10, 171, 21))
        self.webUrl.setMaximumSize(QtCore.QSize(16777215, 45))
        self.webUrl.setObjectName("webUrl")
        self.submit = QtWidgets.QPushButton(self.widget)
        self.submit.setGeometry(QtCore.QRect(480, 10, 93, 32))
        self.submit.setStyleSheet("font: 14pt \"楷体\";")
        self.submit.setObjectName("submit")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.widget)
        self.webView.setGeometry(QtCore.QRect(280, 60, 511, 501))
        self.webView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
        self.webView.setZoomFactor(0.6)
        self.webView.setObjectName("webView")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(10, 60, 251, 481))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 48, 23))
        self.label_3.setStyleSheet("font: 14pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.webUrlAttack = QtWidgets.QLineEdit(self.tab_2)
        self.webUrlAttack.setGeometry(QtCore.QRect(150, 20, 171, 21))
        self.webUrlAttack.setMaximumSize(QtCore.QSize(16777215, 45))
        self.webUrlAttack.setObjectName("webUrlAttack")
        self.submitAttack = QtWidgets.QPushButton(self.tab_2)
        self.submitAttack.setGeometry(QtCore.QRect(590, 20, 93, 32))
        self.submitAttack.setStyleSheet("font: 14pt \"楷体\";")
        self.submitAttack.setObjectName("submitAttack")
        self.webUrlAttackThreadNum = QtWidgets.QLineEdit(self.tab_2)
        self.webUrlAttackThreadNum.setGeometry(QtCore.QRect(450, 20, 101, 21))
        self.webUrlAttackThreadNum.setMaximumSize(QtCore.QSize(16777215, 45))
        self.webUrlAttackThreadNum.setObjectName("webUrlAttackThreadNum")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(360, 20, 71, 23))
        self.label_4.setStyleSheet("font: 14pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextBrowser(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 791, 461))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.submit.clicked.connect(lambda: self.submitEvent())
        self.submitAttack.clicked.connect(lambda : self.webAttackEvent())

        sys.stdout = EmittingStr(textWritten=self.outputWritten)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def outputWritten(self,text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "网址"))
        self.submit.setText(_translate("MainWindow", "分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "网址分析"))
        self.label_3.setText(_translate("MainWindow", "网址"))
        self.submitAttack.setText(_translate("MainWindow", "开始"))
        self.label_4.setText(_translate("MainWindow", "线程数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "网站攻击"))

    def submitEvent(self):
        url=self.webUrl.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        urls=getAllUrl(url)
        if len(urls)==0:
            self.messageDialog("解析链接为空")
            return
        self.tableShow([(item["url"],item["type"]) for item in urls])

    def tableShow(self,urls):
        self.model = QStandardItemModel(len(urls), 2)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['url', '来源'])  # 设置每列标题
        for row in range(len(urls)):
            for column in range(2):
                item = QStandardItem(urls[row][column])  # 创建模板内容
                self.model.setItem(row, column, item)  # 向模板里添加 item
        self.tableView.setModel(self.model)  # 表格设置模板
        self.tableView.clicked.connect(self.tableClickEvent)


    def tableClickEvent(self,index):
        text = self.model.item(index.row(), 0).text()
        self.webView.setUrl(QUrl(text))

    def messageDialog(self, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()


    #################################网站攻击####################################
    def webAttackEvent(self):
        url=self.webUrlAttack.text()
        threadNum=self.webUrlAttackThreadNum.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        try:
            threadNum=int(threadNum)
            if threadNum<1 or threadNum>64:
                self.messageDialog("线程数在1到64之间")
                return
        except:
            self.messageDialog("请输入正确的线程数")
            return

        filename=time.strftime("%Y_%m_%d_%H_%M_%S")
        open("data/"+filename+".txt",'w').close()
        self.textEdit.append(f"日志文件保存在data/{filename}.txt文件中\n\n")
        for i in range(threadNum):
            threading.Thread(target=self.threadAttack,args=(url,filename)).start()




    def threadAttack(self,url,filename):
        for i in range(10):
            res=requests.get(url)
            data=f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{threading.currentThread().getName()}的第{i+1}次请求攻击\t{res.status_code}\t{url}"
            self.saveLog(filename, data)


    def saveLog(self, filename, data):
        lock=threading.Lock()
        lock.acquire()
        # self.textEdit.append(f"\n\n{data}")
        print(data)
        with open("data/"+filename+".txt","a",encoding="utf-8") as f:
            f.write(data+"\n")
        lock.release()


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


from PyQt5 import QtWebEngineWidgets
