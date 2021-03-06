# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stuinfo_add_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_Window_stuinfo_add(object):
    def setupUi(self, Window_stuinfo_add):
        Window_stuinfo_add.setObjectName("Window_stuinfo_add")
        Window_stuinfo_add.resize(1280, 720)
        Window_stuinfo_add.setMinimumSize(QtCore.QSize(1280, 720))
        Window_stuinfo_add.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_title = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title.setGeometry(QtCore.QRect(490, 20, 300, 60))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_title2 = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title2.setGeometry(QtCore.QRect(440, 140, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title2.setFont(font)
        self.label_title2.setObjectName("label_title2")
        self.label_title3 = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title3.setGeometry(QtCore.QRect(440, 220, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title3.setFont(font)
        self.label_title3.setObjectName("label_title3")
        self.label_title4 = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title4.setGeometry(QtCore.QRect(440, 300, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title4.setFont(font)
        self.label_title4.setObjectName("label_title4")
        self.label_title5 = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title5.setGeometry(QtCore.QRect(440, 380, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title5.setFont(font)
        self.label_title5.setObjectName("label_title5")
        self.label_title6 = QtWidgets.QLabel(Window_stuinfo_add)
        self.label_title6.setGeometry(QtCore.QRect(440, 460, 100, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title6.setFont(font)
        self.label_title6.setObjectName("label_title6")
        self.lineEdit_stuno = QtWidgets.QLineEdit(Window_stuinfo_add)
        self.lineEdit_stuno.setGeometry(QtCore.QRect(530, 140, 300, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_stuno.setFont(font)
        self.lineEdit_stuno.setObjectName("lineEdit_stuno")
        self.lineEdit_stuage = QtWidgets.QLineEdit(Window_stuinfo_add)
        self.lineEdit_stuage.setGeometry(QtCore.QRect(530, 220, 300, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_stuage.setFont(font)
        self.lineEdit_stuage.setObjectName("lineEdit_stuage")
        self.lineEdit_stuname = QtWidgets.QLineEdit(Window_stuinfo_add)
        self.lineEdit_stuname.setGeometry(QtCore.QRect(530, 300, 300, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_stuname.setFont(font)
        self.lineEdit_stuname.setObjectName("lineEdit_stuname")
        self.lineEdit_stuclass = QtWidgets.QLineEdit(Window_stuinfo_add)
        self.lineEdit_stuclass.setGeometry(QtCore.QRect(530, 380, 300, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_stuclass.setFont(font)
        self.lineEdit_stuclass.setObjectName("lineEdit_stuclass")
        self.lineEdit_stusex = QtWidgets.QLineEdit(Window_stuinfo_add)
        self.lineEdit_stusex.setGeometry(QtCore.QRect(530, 460, 300, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.lineEdit_stusex.setFont(font)
        self.lineEdit_stusex.setObjectName("lineEdit_stusex")
        self.pushButton_add = QtWidgets.QPushButton(Window_stuinfo_add)
        self.pushButton_add.setGeometry(QtCore.QRect(440, 540, 390, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(Window_stuinfo_add)
        QtCore.QMetaObject.connectSlotsByName(Window_stuinfo_add)

        self.pushButton_add.clicked.connect(lambda: self.add())

    def retranslateUi(self, Window_stuinfo_add):
        _translate = QtCore.QCoreApplication.translate
        Window_stuinfo_add.setWindowTitle(_translate("Window_stuinfo_add", "Form"))
        self.label_title.setText(_translate("Window_stuinfo_add", "添加学生信息"))
        self.label_title2.setText(_translate("Window_stuinfo_add", "学号："))
        self.label_title3.setText(_translate("Window_stuinfo_add", "年龄："))
        self.label_title4.setText(_translate("Window_stuinfo_add", "姓名："))
        self.label_title5.setText(_translate("Window_stuinfo_add", "班级："))
        self.label_title6.setText(_translate("Window_stuinfo_add", "性别："))
        self.pushButton_add.setText(_translate("Window_stuinfo_add", "添加"))

    def add(self):
        sno = self.lineEdit_stuno.text()
        sname = self.lineEdit_stuname.text()
        sage = self.lineEdit_stuage.text()
        sclass = self.lineEdit_stuclass.text()
        sex = self.lineEdit_stusex.text()
        conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};'
                              r'SERVER=Beta;'
                              r'DATABASE=Curriculum_design;'
                              r'UID=Pdocw;'
                              r'PWD=123456'
                              )
        cur = conn.cursor()
        if sno != '' and sname != '' and sage != '' and sclass != '' and sex != '':
            cur.execute('SELECT * FROM xsxx WHERE Sno =' + sno)
        elif sno == '':
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "错误", "学号不能为空", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
            return
        elif not sno.isdigit() or not sage.isdigit() or sclass.isdigit():
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "错误", "请输入数字！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
            return
        else:
            return
        row = cur.fetchone()
        if not row:
            cur.execute("insert into xsxx values('" + sno + "','" + sname + "','" + sex + "','" + sclass + "','" + sage + "')")
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.about(QtWidgets.QWidget(), "提示", "用户添加成功！")
        else:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "提示", "该学号已存在！请重新输入！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
