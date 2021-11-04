# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_browser = QtWidgets.QToolButton(self.centralwidget)
        self.file_browser.setGeometry(QtCore.QRect(330, 70, 61, 21))
        self.file_browser.setObjectName("file_browser")
        self.file_path_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path_edit.setGeometry(QtCore.QRect(110, 70, 201, 20))
        self.file_path_edit.setObjectName("file_path_edit")
        self.file_path_label = QtWidgets.QLabel(self.centralwidget)
        self.file_path_label.setGeometry(QtCore.QRect(33, 70, 71, 21))
        self.file_path_label.setObjectName("file_path_label")
        self.set_ouput_path = QtWidgets.QPushButton(self.centralwidget)
        self.set_ouput_path.setGeometry(QtCore.QRect(330, 110, 81, 23))
        self.set_ouput_path.setObjectName("set_ouput_path")
        self.file_path_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path_edit_2.setGeometry(QtCore.QRect(110, 110, 201, 20))
        self.file_path_edit_2.setObjectName("file_path_edit_2")
        self.file_path_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.file_path_label_2.setGeometry(QtCore.QRect(30, 110, 71, 21))
        self.file_path_label_2.setObjectName("file_path_label_2")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(130, 160, 81, 23))
        self.start.setObjectName("start")
        self.console_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.console_browser.setGeometry(QtCore.QRect(20, 200, 401, 171))
        self.console_browser.setObjectName("console_browser")
        self.quite_app = QtWidgets.QPushButton(self.centralwidget)
        self.quite_app.setGeometry(QtCore.QRect(230, 160, 81, 23))
        self.quite_app.setObjectName("quite_app")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频转动图"))
        self.file_browser.setText(_translate("MainWindow", "浏览文件"))
        self.file_path_label.setText(_translate("MainWindow", "文件输入路径"))
        self.set_ouput_path.setText(_translate("MainWindow", "设置输出路径"))
        self.file_path_label_2.setText(_translate("MainWindow", "文件输出路径"))
        self.start.setText(_translate("MainWindow", "开始转换"))
        self.quite_app.setText(_translate("MainWindow", "退出"))
