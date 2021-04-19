# This Python file uses the following encoding: utf-8
import sys,os,random

from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from TestLayout import Test



class MainWindow(QtWidgets.QMainWindow): 
	def __init__(self): 
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def resizeEvent(self, event): 
		self.resizeThis(self.ui.centralWidget,True,True)
		self.resizeThis(self.ui.frame,True,False)
		self.resizeThis(self.ui.scrollArea,True,False)
		self.resizeThis(self.ui.scrollAreaWidgetContents,True,False)
		self.resizeThis(self.ui.testScroll,True,True)
		self.resizeThis(self.ui.testScrollArea,True,True)

	def resizeThis(self,widget,updateHeight,updateWidth):
		parentWidth=widget.parent().geometry().width()
		parentHeight=widget.parent().geometry().height()
		x=widget.geometry().x()
		y=widget.frameGeometry().y()
		if updateHeight: height=parentHeight-y
		else:            height=widget.geometry().height()
		if updateWidth: width=parentWidth-x
		else:           width=widget.geometry().width()
		s=QtCore.QRect(x,y,width,height)
		widget.setGeometry(s)

	def addTest(self,widget): 
		vlay = main.ui.allTests 
		vlay.insertWidget(vlay.count()-1,Test())








if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()


	vlay = main.ui.allTests
	main.addTest(Test())
	main.addTest(Test())
	main.addTest(Test())
	main.addTest(Test())
	
	










	
	main.show()

	sys.exit(app.exec_())
