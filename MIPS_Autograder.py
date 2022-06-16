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

    partNum = "4"  
    settingsFile ="part%s.json"%partNum
    submissionFile ="part%s.s"%partNum

    all_tests_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Tests")
    test_dir = os.path.join(all_tests_dir,"Task%s"%partNum)
    
    settingsPath = os.path.join(test_dir,settingsFile)
    submissionPath = os.path.join(test_dir,submissionFile)

    thread = main.LoadSettings(filePath=settingsPath) 
    thread.finished.connect(lambda: main.RunMips(submissionPath=submissionPath))
    
    sys.exit(app.exec_())
