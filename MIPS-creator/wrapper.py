# This Python file uses the following encoding: utf-8
import sys,os,random

from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.sip import delete
from mainwindow import Ui_MainWindow
from TestLayout import Test



class MainWindow(QtWidgets.QMainWindow): 
	allTests:QtWidgets.QVBoxLayout
	def __init__(self): 
		super(MainWindow, self).__init__() 
		uic.loadUi('mainwindow.ui', self)
		self.allTests.addStretch(500)
		self.AddTestButton.pressed.connect(self.addTest) 
		self.numberOfTests=0
		#self.ui = Ui_MainWindow()
		#self.ui.setupUi(self)

	def resizeEvent(self, event): 
		self.resizeThis(self.centralWidget,True,True)
		self.resizeThis(self.frame,True,False)
		self.resizeThis(self.scrollArea,True,False)
		self.resizeThis(self.testScroll,True,True)
		self.resizeThis(self.testScrollArea,True,True)

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

	def insertWidget(self,widget): 
		vlay = self.allTests 
		
		vlay.insertWidget(vlay.count()-1,widget)
	

	def updateAllTestIndices(self):
		lay=self.allTests
		items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
		i=0
		test:Test 
		for test in items: 
			if test is None: continue
			test.index=i
			test.name=test.name
			i+=1
			
	def deleteTest(self,test:Test): 
		lay=self.allTests
		lay.removeWidget(test)
		self.numberOfTests-=1
		del test
		self.updateAllTestIndices()
			

	def addTest(self,newTest=None): 
		vlay = self.allTests 
		index=self.numberOfTests
		if newTest is None: 
			newTest=Test(index=index,parent=self)
		else: 
			newTest.index=index
			newTest.name=newTest.name
		self.insertWidget(newTest)
		self.numberOfTests+=1






if __name__ == '__main__':
	os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()

	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap("Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	main.addTest()
	main.addTest()
	main.addTest()
	
	main.show()

	sys.exit(app.exec_())
