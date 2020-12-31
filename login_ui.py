# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import ui_rc
import pyodbc

from PyQt5 import QtCore, QtGui, QtWidgets
from generaluser_ui import Ui_Window_generaluser
from admin_ui import Ui_Window_admin
from score_inquiry_ui import Ui_Window_score_inquiry


class Ui_Window_login(object):
    def setupUi(self, Window_login):
        Window_login.setObjectName("Window_login")
        Window_login.resize(1280, 720)
        Window_login.setMinimumSize(QtCore.QSize(1280, 720))
        Window_login.setMaximumSize(QtCore.QSize(1280, 720))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/icon/res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_background = QtWidgets.QLabel(Window_login)
        self.label_background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap(":/background/res/bell_tower.png"))
        self.label_background.setObjectName("label_background")
        self.lineEdit_username = QtWidgets.QLineEdit(Window_login)
        self.lineEdit_username.setGeometry(QtCore.QRect(600, 200, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setTabletTracking(False)
        self.lineEdit_username.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_username.setAutoFillBackground(False)
        self.lineEdit_username.setFrame(True)
        self.lineEdit_username.setDragEnabled(False)
        self.lineEdit_username.setClearButtonEnabled(False)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_username = QtWidgets.QLabel(Window_login)
        self.label_username.setGeometry(QtCore.QRect(480, 200, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Window_login)
        self.label_password.setGeometry(QtCore.QRect(480, 270, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(Window_login)
        self.lineEdit_password.setGeometry(QtCore.QRect(600, 270, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(Window_login)
        self.pushButton_login.setGeometry(QtCore.QRect(480, 350, 160, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_exit = QtWidgets.QPushButton(Window_login)
        self.pushButton_exit.setGeometry(QtCore.QRect(690, 350, 160, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_tip = QtWidgets.QLabel(Window_login)
        self.label_tip.setGeometry(QtCore.QRect(530, 140, 291, 40))
        self.label_tip.setStyleSheet('color:rgb(255, 0, 0)')
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_tip.setFont(font)
        self.label_tip.setText("")
        self.label_tip.setObjectName("label_tip")

        self.retranslateUi(Window_login)
        # 登录
        self.pushButton_login.clicked.connect(lambda: self.login())
        # 关闭页面
        self.pushButton_exit.clicked.connect(Window_login.close)
        QtCore.QMetaObject.connectSlotsByName(Window_login)

    def retranslateUi(self, Window_login):
        _translate = QtCore.QCoreApplication.translate
        Window_login.setWindowTitle(_translate("Window_login", "浙江理工大学学生管理系统"))
        Window_login.setWindowIcon(self.icon)
        self.label_username.setText(_translate("Window_login", "用户名："))
        self.label_password.setText(_translate("Window_login", "密    码："))
        self.pushButton_login.setText(_translate("Window_login", "登录"))
        self.pushButton_exit.setText(_translate("Window_login", "退出"))

    def login(self):
        # 获取用户名和密码
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        with open("username.txt", "w") as f:
            f.write(username)
        if username == '' and password == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "用户名或密码不可为空，请重新输入！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        elif username == 'admin' and password == 'admin':
            self.lineEdit_username.setText("")
            self.lineEdit_password.setText("")
            admin_window = Ui_Window_admin()
            window = QtWidgets.QMainWindow()
            admin_window.setupUi(window)
            window.show()
        elif self.isUser(username) and password == username:
            self.lineEdit_username.setText("")
            self.lineEdit_password.setText("")
            generaluser_window = Ui_Window_generaluser()
            window = QtWidgets.QMainWindow()
            generaluser_window.setupUi(window)
            window.show()
        else:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "用户名或密码错误，请重新输入！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)

    def isUser(self, name):
        """name用户是否在学生信息表中，若在则证明该用户可以使用该数据库，返回Ture，反之返回False"""
        conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};'
                              r'SERVER=Beta;'
                              r'DATABASE=Curriculum_design;'
                              r'UID=Pdocw;'
                              r'PWD=123456')
        cur = conn.cursor()
        cur.execute("SELECT * FROM xsxx WHERE Sno='" + name + "'")
        row = cur.fetchone()
        conn.close()
        if row:
            return True
        else:
            return False