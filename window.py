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
import encryption_util as enUtil

from websearch import getAllUrl
import re

comp = re.compile(
    "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?")


class Ui_MainWindow(object):

    def __init__(self):
        pass


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
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 791, 461))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.symCombBox = QtWidgets.QComboBox(self.tab)
        self.symCombBox.setGeometry(QtCore.QRect(300, 20, 111, 31))
        self.symCombBox.setObjectName("symCombBox")
        self.symCombBox.addItem("")
        self.symCombBox.addItem("")
        self.symCombBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.symKey = QtWidgets.QTextEdit(self.tab)
        self.symKey.setGeometry(QtCore.QRect(410, 110, 371, 91))
        self.symKey.setObjectName("symKey")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(410, 70, 101, 31))
        self.label_6.setStyleSheet("font: 14pt \"楷体\";")
        self.label_6.setObjectName("label_6")
        self.symResult = QtWidgets.QTextEdit(self.tab)
        self.symResult.setGeometry(QtCore.QRect(410, 260, 371, 271))
        self.symResult.setObjectName("symResult")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(410, 220, 101, 31))
        self.label_7.setStyleSheet("font: 14pt \"楷体\";")
        self.label_7.setObjectName("label_7")
        self.symContent = QtWidgets.QTextEdit(self.tab)
        self.symContent.setGeometry(QtCore.QRect(20, 110, 341, 421))
        self.symContent.setObjectName("symContent")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.label_8.setStyleSheet("font: 14pt \"楷体\";")
        self.label_8.setObjectName("label_8")
        self.symEncryptionBtn = QtWidgets.QPushButton(self.tab)
        self.symEncryptionBtn.setGeometry(QtCore.QRect(450, 20, 71, 41))
        self.symEncryptionBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.symEncryptionBtn.setObjectName("symEncryptionBtn")
        self.symDecipherBtn = QtWidgets.QPushButton(self.tab)
        self.symDecipherBtn.setGeometry(QtCore.QRect(540, 20, 71, 41))
        self.symDecipherBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.symDecipherBtn.setObjectName("symDecipherBtn")
        self.symResult.setReadOnly(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 101, 31))
        self.label_9.setStyleSheet("font: 14pt \"楷体\";")
        self.label_9.setObjectName("label_9")
        self.asymResult = QtWidgets.QTextEdit(self.tab_3)
        self.asymResult.setGeometry(QtCore.QRect(410, 260, 371, 271))
        self.asymResult.setObjectName("asymResult")
        self.asymPrivateKey = QtWidgets.QTextEdit(self.tab_3)
        self.asymPrivateKey.setGeometry(QtCore.QRect(410, 110, 371, 91))
        self.asymPrivateKey.setObjectName("asymPrivateKey")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(410, 70, 101, 31))
        self.label_10.setStyleSheet("font: 14pt \"楷体\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(410, 220, 101, 31))
        self.label_11.setStyleSheet("font: 14pt \"楷体\";")
        self.label_11.setObjectName("label_11")
        self.asymCombBox = QtWidgets.QComboBox(self.tab_3)
        self.asymCombBox.setGeometry(QtCore.QRect(310, 20, 111, 31))
        self.asymCombBox.setObjectName("asymCombBox")
        self.asymCombBox.addItem("")
        self.asymCombBox.addItem("")
        self.asymCombBox.addItem("")
        self.asymContent = QtWidgets.QTextEdit(self.tab_3)
        self.asymContent.setGeometry(QtCore.QRect(20, 260, 371, 271))
        self.asymContent.setObjectName("asymContent")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(200, 20, 101, 31))
        self.label_5.setStyleSheet("font: 14pt \"楷体\";")
        self.label_5.setObjectName("label_5")
        self.asymPublicKey = QtWidgets.QTextEdit(self.tab_3)
        self.asymPublicKey.setGeometry(QtCore.QRect(20, 110, 371, 91))
        self.asymPublicKey.setObjectName("asymPublicKey")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.label_12.setStyleSheet("font: 14pt \"楷体\";")
        self.label_12.setObjectName("label_12")
        self.asymDecipherBtn = QtWidgets.QPushButton(self.tab_3)
        self.asymDecipherBtn.setGeometry(QtCore.QRect(540, 20, 120, 41))
        self.asymDecipherBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.asymDecipherBtn.setObjectName("asymDecipherBtn")
        self.asymEncryptionBtn = QtWidgets.QPushButton(self.tab_3)
        self.asymEncryptionBtn.setGeometry(QtCore.QRect(450, 20, 71, 41))
        self.asymEncryptionBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.asymEncryptionBtn.setObjectName("asymEncryptionBtn")
        self.asymPublicKey.setReadOnly(True)
        self.asymPrivateKey.setReadOnly(True)
        self.asymResult.setReadOnly(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(230, 20, 101, 31))
        self.label_13.setStyleSheet("font: 14pt \"楷体\";")
        self.label_13.setObjectName("label_13")
        self.otherEncryptionBtn = QtWidgets.QPushButton(self.tab_4)
        self.otherEncryptionBtn.setGeometry(QtCore.QRect(480, 20, 71, 41))
        self.otherEncryptionBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.otherEncryptionBtn.setObjectName("otherEncryptionBtn")
        self.otherCombBox = QtWidgets.QComboBox(self.tab_4)
        self.otherCombBox.setGeometry(QtCore.QRect(340, 20, 111, 31))
        self.otherCombBox.setObjectName("otherCombBox")
        self.otherCombBox.addItem("")
        self.otherCombBox.addItem("")
        self.otherCombBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(30, 70, 101, 31))
        self.label_14.setStyleSheet("font: 14pt \"楷体\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(420, 70, 101, 31))
        self.label_15.setStyleSheet("font: 14pt \"楷体\";")
        self.label_15.setObjectName("label_15")
        self.otherContent = QtWidgets.QTextEdit(self.tab_4)
        self.otherContent.setGeometry(QtCore.QRect(30, 110, 371, 421))
        self.otherContent.setObjectName("otherContent")
        self.otherResult = QtWidgets.QTextEdit(self.tab_4)
        self.otherResult.setGeometry(QtCore.QRect(420, 110, 371, 421))
        self.otherResult.setObjectName("otherResult")
        self.otherResult.setReadOnly(True)
        self.tabWidget.addTab(self.tab_4, "")
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
        self.submitAttack.clicked.connect(lambda: self.webAttackEvent())
        self.otherEncryptionBtn.clicked.connect(lambda : self.otherEncrytEvent())       #其他加密
        self.symEncryptionBtn.clicked.connect(lambda : self.symEncrytEvent())       #对称加密
        self.symDecipherBtn.clicked.connect(lambda : self.symDecipherEvent())
        self.asymEncryptionBtn.clicked.connect(lambda : self.asymEncrytEvent())        #非对称加密
        self.asymDecipherBtn.clicked.connect(lambda : self.asymGetKey())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.symCombBox.setItemText(0, _translate("MainWindow", "DES"))
        self.symCombBox.setItemText(1, _translate("MainWindow", "AES"))
        self.symCombBox.setItemText(2, _translate("MainWindow", "3DES"))
        self.label_2.setText(_translate("MainWindow", "加密算法"))
        self.label_6.setText(_translate("MainWindow", "密钥"))
        self.label_7.setText(_translate("MainWindow", "转换结果"))
        self.label_8.setText(_translate("MainWindow", "转换内容"))
        self.symEncryptionBtn.setText(_translate("MainWindow", "加密"))
        self.symDecipherBtn.setText(_translate("MainWindow", "解密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "对称加密"))
        self.label_9.setText(_translate("MainWindow", "转换内容"))
        self.label_10.setText(_translate("MainWindow", "私钥"))
        self.label_11.setText(_translate("MainWindow", "转换结果"))
        self.asymCombBox.setItemText(0, _translate("MainWindow", "RSA"))
        self.asymCombBox.setItemText(1, _translate("MainWindow", "DSA"))
        self.asymCombBox.setItemText(2, _translate("MainWindow", "ECC"))
        self.label_5.setText(_translate("MainWindow", "加密算法"))
        self.label_12.setText(_translate("MainWindow", "公钥"))
        self.asymDecipherBtn.setText(_translate("MainWindow", "生成密钥"))
        self.asymEncryptionBtn.setText(_translate("MainWindow", "加密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "非对称加密"))
        self.label_13.setText(_translate("MainWindow", "加密算法"))
        self.otherEncryptionBtn.setText(_translate("MainWindow", "加密"))
        self.otherCombBox.setItemText(0, _translate("MainWindow", "MD5"))
        self.otherCombBox.setItemText(1, _translate("MainWindow", "SHA1"))
        self.otherCombBox.setItemText(2, _translate("MainWindow", "Base64"))
        self.label_14.setText(_translate("MainWindow", "加密内容"))
        self.label_15.setText(_translate("MainWindow", "加密结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "其他加密"))


    def symDecipherEvent(self):
        key = self.symKey.toPlainText()
        text = self.symContent.toPlainText()
        type = self.symCombBox.currentText()
        if text.strip() == '':
            self.messageDialog("转换内容不能为空")
            return
        if key.strip() == '':
            self.messageDialog("密钥不能为空")
            return

        if type == "DES" and len(key.strip()) != 8:
            self.messageDialog("DES算法密钥长度必须为8位")
            return

        if type == "3DES" and (len(key.strip()) != 16 and len(key.strip()) != 24):
            self.messageDialog("3DES算法密钥长度必须为16位或24位")
            return
        rs = ''
        if type == 'DES':
            rs = enUtil.DESDecryption(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        elif type == 'AES':
            rs = enUtil.AES_decrypt(text, key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            des3 = enUtil.DES3Encryt(key)
            rs = des3.decrypt(text)
            if rs is None:
                self.messageDialog("转换失败")
                return
        self.symResult.setPlainText(rs)



    def asymGetKey(self):
        privateKey, publicKey = enUtil.get_rsa_key()
        self.asymPrivateKey.setPlainText(str(privateKey.decode()))
        self.asymPublicKey.setPlainText(str(publicKey.decode()))


    def asymEncrytEvent(self):
        text=self.asymContent.toPlainText()
        if text.strip()=='':
            self.messageDialog("转换内容不能为空")
            return
        type=self.asymCombBox.currentText()
        rs=''
        publicKey=self.asymPublicKey.toPlainText()
        if publicKey.strip()=='':
            self.messageDialog("公钥不能为空，请先生成公钥")
            return
        if type=='RSA':
            rs=enUtil.RSAEncryt(text,publicKey)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            self.messageDialog(f"{type}算法暂未开放")
            return
        self.asymResult.setPlainText(rs)


    def symEncrytEvent(self):
        key=self.symKey.toPlainText()
        text=self.symContent.toPlainText()
        type = self.symCombBox.currentText()
        if text.strip()=='':
            self.messageDialog("转换内容不能为空")
            return
        if key.strip()=='':
            self.messageDialog("密钥不能为空")
            return

        if type=="DES" and len(key.strip())!=8:
            self.messageDialog("DES算法密钥长度必须为8位")
            return

        if type=="3DES" and (len(key.strip())!=16 and len(key.strip())!=24):
            self.messageDialog("3DES算法密钥长度必须为16位或24位")
            return
        rs=''
        if type=='DES':
            rs=enUtil.DESEncrytion(text,key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        elif type=='AES':
            rs=enUtil.AES_encrypt(text,key)
            if rs is None:
                self.messageDialog("转换失败")
                return
        else:
            des3=enUtil.DES3Encryt(key)
            rs=des3.encrypt(text)
            if rs is None:
                self.messageDialog("转换失败")
                return
        self.symResult.setPlainText(rs)


    def otherEncrytEvent(self):
        text=self.otherContent.toPlainText()
        if text.strip()=='':
            self.messageDialog("加密内容不能为空")
            return
        type=self.otherCombBox.currentText()
        rs=''
        if type=='MD5':
            rs=enUtil.MD5Encrytion(text)
        elif type=='SHA1':
            rs=enUtil.SHA1Encrytion(text)
        else:
            rs=enUtil.Base64Encrythion(text)
        self.otherResult.setPlainText(rs)


    def outputWritten(self,text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def submitEvent(self):
        url = self.webUrl.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        urls = getAllUrl(url)
        if len(urls) == 0:
            self.messageDialog("解析链接为空")
            return
        self.tableShow([(item["url"], item["type"]) for item in urls])

    def tableShow(self, urls):
        self.model = QStandardItemModel(len(urls), 2)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['url', '来源'])  # 设置每列标题
        for row in range(len(urls)):
            for column in range(2):
                item = QStandardItem(urls[row][column])  # 创建模板内容
                self.model.setItem(row, column, item)  # 向模板里添加 item
        self.tableView.setModel(self.model)  # 表格设置模板
        self.tableView.clicked.connect(self.tableClickEvent)

    def tableClickEvent(self, index):
        text = self.model.item(index.row(), 0).text()
        self.webView.setUrl(QUrl(text))

    def messageDialog(self, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()

    #################################网站攻击####################################
    def webAttackEvent(self):
        url = self.webUrlAttack.text()
        threadNum = self.webUrlAttackThreadNum.text()
        if not comp.search(url):
            self.messageDialog("请输入正确的url")
            return
        try:
            threadNum = int(threadNum)
            if threadNum < 1 or threadNum > 64:
                self.messageDialog("线程数在1到64之间")
                return
        except:
            self.messageDialog("请输入正确的线程数")
            return

        filename = time.strftime("%Y_%m_%d_%H_%M_%S")
        open("data/" + filename + ".txt", 'w').close()
        sys.stdout = EmittingStr(textWritten=self.outputWritten)        # 开启GUI输出
        self.textEdit.append(f"日志文件保存在data/{filename}.txt文件中\n\n")
        for i in range(threadNum):
            threading.Thread(target=self.threadAttack, args=(url, filename)).start()

    def threadAttack(self, url, filename):
        for i in range(10):
            res = requests.get(url)
            data = f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{threading.currentThread().getName()}的第{i + 1}次请求攻击\t{res.status_code}\t{url}"
            self.saveLog(filename, data)

    def saveLog(self, filename, data):
        lock = threading.Lock()
        lock.acquire()
        # self.textEdit.append(f"\n\n{data}")
        print(data)
        with open("data/" + filename + ".txt", "a", encoding="utf-8") as f:
            f.write(data + "\n")
        lock.release()


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


from PyQt5 import QtWebEngineWidgets
