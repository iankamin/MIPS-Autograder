# This Python file uses the following encoding: utf-8
import sys,os
from PyQt5 import QtWidgets
from Frontend.mainwindow import MainWindow

def folderGenerate(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

if __name__ == '__main__':
    folderGenerate("Frontend")

    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('macintosh')
    #app.setStyle('windows')
    #app.setStyle('windowsvista')
    app.setStyle('Fusion')

    font=app.font()
    font.setPointSize(12)
    app.setFont(font)
    main = MainWindow()
    print(main.geometry())
    main.showMaximized()
    sys.exit(app.exec_())
