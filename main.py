import generaluser_ui
from admin_ui import Ui_Window_admin
import course_inquiry_ui
from login_ui import Ui_Window_login
import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    login_window = Ui_Window_login()
    # admin_window = Ui_Window_admin()

    MainWindow_login_window = QtWidgets.QMainWindow()
    # MainWindow_admin_window = QtWidgets.QMainWindow()

    login_window.setupUi(MainWindow_login_window)
    # admin_window.setupUi(MainWindow_admin_window)

    MainWindow_login_window.show()
    # login_window.pushButton_login.clicked.connect(MainWindow_admin_window.show)

    app.exec_()
