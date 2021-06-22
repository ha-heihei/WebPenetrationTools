import sys
from PyQt5.QtWidgets import *
from login import LoginUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()  # 防止进程卡死
    MainWindow = QMainWindow()
    ui = LoginUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())