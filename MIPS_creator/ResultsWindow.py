from PyQt5 import QtCore, QtWidgets,uic
from MIPS_creator.ui_files.filepaths import resultswindow_ui

class ResultsWindow(QtWidgets.QMainWindow):
    textBox:QtWidgets.QTextEdit
    def __init__(self, title, parent, text=None):
        super(QtWidgets.QMainWindow, self).__init__(parent) 
        uic.loadUi(resultswindow_ui, self)
        self.setWindowTitle(title)
 
    def resizeEvent(self, event): 
        self.textBox.setMinimumWidth(self.width())
        self.textBox.setMinimumHeight(self.height())

    def displayFile(self,filepath, allLineNumbers=False):
        data=""
        with open(filepath,'r') as f: 
            i=1
            flist=f.readlines()
            for line in flist:
                if allLineNumbers:
                    line = "{:>3}    {}".format(i,line)
                    i=i+1
                data+=line
                
        self.textBox.setText(data)

