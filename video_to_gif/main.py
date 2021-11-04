# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import os
import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
import time

from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
# 导入designer工具生成的login模块
from ui import Ui_MainWindow
from video_to_gif import video_to_gif


# class EmittingStr(QObject):
#     textWritten = pyqtSignal(str)  # 定义一个发送str的信号
#
#     def write(self, text):
#         self.textWritten.emit(str(text))


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.file_browser.clicked.connect(self.browse_file)
        self.set_ouput_path.clicked.connect(self.save_file)
        self.start.clicked.connect(self.start_convert)
        self.quite_app.clicked.connect(self.close)

        self.video_path = None
        self.video_extension = 'MP4(*.mp4);;WMV(*.wmv);;RM(*.rm);;' \
                               'AVI(*.avi);;FLV(*.flv);;WEBM(*.webm);;' \
                               'WAV(*.wav);;RMVB(*.rmvb)'

        self.gif_path = None

        # sys.stdout = EmittingStr(textWritten=self.on_update_text)
        # sys.stderr = EmittingStr(textWritten=self.on_update_text)

    # def on_update_text(self, text):
    #     """Write console output to console_browser."""
    #
    #     cursor = self.console_browser.textCursor()
    #     cursor.movePosition(QTextCursor.End)
    #     cursor.insertText(text)
    #     self.console_browser.setTextCursor(cursor)
    #     self.console_browser.ensureCursorVisible()

    def browse_file(self):
        self.video_path, _ = \
            QFileDialog.getOpenFileName(self, '请选择文件路径', './',
                                        self.video_extension)
        self.file_path_edit.setText(self.video_path)

        dir_path_name, extension = os.path.splitext(self.video_path)
        if self.video_path:
            self.gif_path = os.path.join(dir_path_name + '.gif')
        self.file_path_edit_2.setText(self.gif_path)

    def save_file(self):
        gif_path, _ = \
            QFileDialog.getSaveFileName(self, '请选择路径', './',
                                        'GIF (*.gif)')
        if gif_path:
            self.gif_path = gif_path
        self.file_path_edit_2.setText(self.gif_path)

    def start_convert(self):
        self.start.setEnabled(False)
        self.q_thread = Thread1(video_to_gif, video_path=self.video_path,
                                gif_path=self.gif_path,
                                console_browser=self.console_browser)
        self.q_thread._signal.connect(self.run_app)
        self.q_thread.start()

    def run_app(self):
        self.start.setEnabled(True)


class Thread1(QThread):
    _signal = pyqtSignal()

    def __init__(self, func, **args):
        super().__init__()
        self.func = func
        self.video_path = args.get('video_path')
        self.gif_path = args.get('gif_path')
        self.console_browser = args.get('console_browser')

    def run(self):
        try:
            self.console_browser.append('开始转换，请稍后...')
            self.func(self.video_path, self.gif_path)
            self.console_browser.append('转换完成！')
        except Exception as e:
            self.console_browser.append(e)
        self._signal.emit()
        self.console_browser.append('——————————————')


if __name__ == "__main__":
    try:
        # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
        app = QApplication(sys.argv)
        # 初始化
        myWin = MyMainForm()
        # 将窗口控件显示在屏幕上
        myWin.show()
        # 程序运行，sys.exit方法确保程序完整退出。
        sys.exit(app.exec_())
    except Exception:
        import traceback

        traceback.print_exc()
