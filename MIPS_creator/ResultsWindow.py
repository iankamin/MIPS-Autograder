from PyQt5 import QtCore, QtWidgets,uic,QtGui
from ui_files.filepaths import ui 

class ResultsWindow(QtWidgets.QDockWidget):
    textBox:QtWidgets.QTextEdit
    horizontalScrollBar:QtWidgets.QScrollBar
    verticalScrollBar:QtWidgets.QScrollBar
    lineNum:QtWidgets.QTextEdit
    scrollArea:QtWidgets.QScrollArea

    def __init__(self, title, parent, text=None):
        super(QtWidgets.QDockWidget, self).__init__(parent) 
        uic.loadUi(ui.resultswindow, self)
        header=Header(title)
        header.setStyleSheet("QFrame,QLabel{background-color:rgb(200,200,200)}")
        header.closeBtn.pressed.connect(self.hide)
        header.popoutBtn.pressed.connect(self.popout)
        self.setTitleBarWidget(header)
        self.setWindowTitle(title)
        #self.textBox.textChanged.connect(self.updateScrollBars)
        self.verticalScrollBar=self.textBox.verticalScrollBar()
        self.horizontalScrollBar=self.textBox.horizontalScrollBar()
        self.lineNum.setVerticalScrollBar(self.verticalScrollBar)
       # self.verticalScrollBar.sliderMoved.connect(self.verticalMovement)
        self.isUsed=False
    def popout(self):
        self.setFloating(not self.isFloating())    
    def verticalMovement(self) : 
        self.lineNum.verticalScrollBar().setValue(self.verticalScrollBar.value())

 
    #def resizevent(self, event): 
#        self.scrollArea.setMinimumWidth(self.width())
#        self.scrollArea.setMaximumWidth(self.width())
#        self.scrollArea.setMinimumHeight(self.height())
#        self.scrollArea.setMaximumHeight(self.height())

    def setText(self,text): self.textBox.setText(text)    

    def displayFile(self,filepath, showLineNumbers=False):
        data=""
        nums=""
        try:
            with open(filepath,'r') as f: 
                flist=f.readlines()
        except FileNotFoundError: 
            self.hide()
            self.isUsed=False
            return False

        self.isUsed=True
        i=1
        for line in flist:
            if showLineNumbers:
                nums+=str(i)+'<br>'
                i=i+1
            data+=line

        self.textBox.setText(data)
        #self.updateScrollBars()
        if showLineNumbers:
            nums="<p style=\"text-align: right\">%s"%nums
            self.lineNum.setHtml(nums)
        else: self.lineNum.hide()
        self.show()
        return True

class Header(QtWidgets.QWidget):
    def __init__(self,title):
        super(QtWidgets.QWidget, self).__init__() 
        self.setObjectName("header")
        self.resize(335, 30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        lay = QtWidgets.QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        frame=QtWidgets.QFrame()
        lay.addWidget(frame)



        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 30))
        self.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalLayout = QtWidgets.QHBoxLayout(frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title = QtWidgets.QLabel(self,text=title)
        self.Title.setText(title)
        self.Title.setObjectName("Title")
        self.horizontalLayout.addWidget(self.Title)
        self.popoutBtn = QtWidgets.QToolButton(self)
        self.popoutBtn.setObjectName("popoutBtn")
        self.horizontalLayout.addWidget(self.popoutBtn)
        self.closeBtn = QtWidgets.QToolButton(self)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Title.setText(_translate("header", "TextLabel"))
        self.popoutBtn.setText(_translate("header", "--"))
        self.closeBtn.setText(_translate("header", "X"))

