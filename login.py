# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow, QLineEdit
import hashlib
from dbutil import DBUtil
from register import RegisterUI
import time
from threading import Thread
# from mainwindow import Ui_MainWindow
from window import Ui_MainWindow
import threading

class LoginUI(object):

    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 80, 481, 315))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setMaximumSize(QtCore.QSize(95, 16777215))
        self.loginBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_3.addWidget(self.loginBtn)
        self.registerBtn = QtWidgets.QPushButton(self.widget)
        self.registerBtn.setMaximumSize(QtCore.QSize(95, 16777215))
        self.registerBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.registerBtn.setObjectName("registerBtn")
        self.horizontalLayout_3.addWidget(self.registerBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMaximumSize(QtCore.QSize(80, 45))
        self.label_4.setStyleSheet("font: 14pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setMaximumSize(QtCore.QSize(200, 45))
        self.password.setObjectName("password")
        self.password.setEchoMode(QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.password)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(80, 45))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMaximumSize(QtCore.QSize(200, 45))
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.time = QtWidgets.QLabel(self.widget)
        self.time.setStyleSheet("font: 14pt \"楷体\";")
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font: 28pt \"黑体\";\n"
                                   "text-decoration: underline;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.bindEvent(MainWindow)
        self.timeFlag = True
        self.threadTime = Thread(target=self.timeLabel)
        self.threadTime.daemon=True
        self.threadTime.start()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "王鑫悦的作业"))
        self.loginBtn.setText(_translate("MainWindow", "登录"))
        self.registerBtn.setText(_translate("MainWindow", "注册"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.time.setText(_translate("MainWindow", "时间"))
        self.label_3.setText(_translate("MainWindow", "登录"))
        self.menu.setTitle(_translate("MainWindow", "王鑫悦的作业"))

    def bindEvent(self,MainWindow):
        self.loginBtn.clicked.connect(lambda:self.loginBtnEvent(MainWindow))
        self.registerBtn.clicked.connect(lambda:self.registerEvent(MainWindow))

    def loginBtnEvent(self,MainWindow):
        username=self.username.text()
        password=self.password.text()
        if username.strip()=='' or password.strip()=='':
            self.messageDialog("用户名或密码不能为空")
            return
        password=hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        sql="select * from user where username=%s and password=%s"
        db=DBUtil()
        if db.query(sql,(username,password)):
            db.close()
            self.messageDialog("登陆成功")
            self.timeFlag=False
            mainWindow=Ui_MainWindow()
            mainWindow.setupUi(MainWindow)

        else:
            self.messageDialog("用户名或密码错误")



    def messageDialog(self,msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()


    def registerEvent(self,MainWindow):
        self.mainWindow=QMainWindow()
        registerUI = RegisterUI()
        registerUI.setupUi(self.mainWindow)
        self.mainWindow.show()

    def timeLabel(self):
        while self.timeFlag:
            self.time.setText(time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)








