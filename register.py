# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit
import hashlib
from dbutil import DBUtil


class RegisterUI(object):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 50, 501, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("\n"
                                   "font: 24pt \"黑体\";\n"
                                   "text-decoration: underline;\n"
                                   "")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(50, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setMaximumSize(QtCore.QSize(200, 45))
        self.username.setObjectName("username")
        self.horizontalLayout_4.addWidget(self.username)
        spacerItem1 = QtWidgets.QSpacerItem(50, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(50, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setMaximumSize(QtCore.QSize(200, 45))
        self.password.setObjectName("password")
        self.password.setEchoMode(QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.password)
        spacerItem3 = QtWidgets.QSpacerItem(50, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registerBtn = QtWidgets.QPushButton(self.widget)
        self.registerBtn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.registerBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.registerBtn.setStyleSheet("font: 14pt \"楷体\";")
        self.registerBtn.setObjectName("registerBtn")
        self.horizontalLayout.addWidget(self.registerBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bindEvent()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.registerBtn.setText(_translate("MainWindow", "注册"))

    def bindEvent(self,):
        self.registerBtn.clicked.connect(lambda:self.registerEvent())

    def registerEvent(self):
        username = self.username.text()
        password = self.password.text()
        if username.strip() == '' or password.strip() == '':
            self.messageDialog("用户名或密码不能为空")
            return
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        sql = "insert into user(username,password) values(%s,%s)"
        db = DBUtil()
        if db.update(sql, values=(username, password)):
            self.messageDialog("注册成功")
            db.close()
        else:
            self.messageDialog("注册失败")

    def messageDialog(self, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
        msg_box.exec_()

