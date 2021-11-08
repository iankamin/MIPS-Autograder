# This Python file uses the following encoding: utf-8
import sys,os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from Frontend.mainwindow import MainWindow
from Frontend.resources.filepaths import resource_path

def folderGenerate(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

if __name__ == '__main__':
    #print(sys.platform)
    #folderGenerate("Frontend")
    #os.system("ls")
    app = QtWidgets.QApplication(sys.argv)
    iconpath=resource_path('icon.ico')
    print(iconpath)
    icon = QIcon(iconpath)
    app.setWindowIcon(icon)

    #app.setStyle('macintosh')
    #app.setStyle('windows')
    #app.setStyle('windowsvista')
    app.setStyle('Fusion')

    font=app.font()
    font.setPointSize(12)
    app.setFont(font)
    main = MainWindow()
    main.setWindowIcon(icon)
    main.showMaximized()
    QtWidgets.qApp.processEvents()
    # testing code
    #folder="/home/kamian/MIPS_Autograder/Tests/Task1"
    #thread = main.LoadSettings(filePath="{folder}/part1.json".format(folder=folder)) 
    #thread.finished.connect(lambda: main.RunMips(submissionPath="{folder}/part1.s".format(folder=folder)))
    
    sys.exit(app.exec_())
