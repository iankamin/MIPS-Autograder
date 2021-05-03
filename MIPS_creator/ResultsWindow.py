from PyQt5 import QtCore, QtWidgets,uic
from MIPS_creator.ui_files.filepaths import resultswindow_ui

class ResultsWindow(QtWidgets.QMainWindow):
    textBox:QtWidgets.QTextEdit
    lineNum:QtWidgets.QTextEdit
    scrollArea:QtWidgets.QScrollArea

    def __init__(self, title, parent, text=None):
        super(QtWidgets.QMainWindow, self).__init__(parent) 
        uic.loadUi(resultswindow_ui, self)
        self.setWindowTitle(title)
        self.textBox.wheelEvent = self.scrollArea.wheelEvent
        self.lineNum.wheelEvent = self.scrollArea.wheelEvent
    
    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus(): 
            return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)
 
    def resizeEvent(self, event): 
        self.scrollArea.setMinimumWidth(self.width())
        self.scrollArea.setMaximumWidth(self.width())
        self.scrollArea.setMinimumHeight(self.height())
        self.scrollArea.setMaximumHeight(self.height())

        

    def displayFile(self,filepath, showLineNumbers=False):
        data=""
        nums=""
        with open(filepath,'r') as f: 
            i=1
            flist=f.readlines()
            for line in flist:
                if showLineNumbers:
                    nums+=str(i)+'<br>'
                    i=i+1
                data+=line


        nums="<p style=\"text-align: right\">%s"%nums
        self.textBox.setText(data)
        self.textBox.setMinimumHeight((self.textBox.fontMetrics().height()*i)+50)
        if showLineNumbers:
            self.lineNum.setHtml(nums)
            self.lineNum.setMinimumHeight(self.textBox.fontMetrics().height()*i)
            self.lineNum.setFixedWidth((10*len(str(i)))+10)
        else: self.lineNum.hide()

