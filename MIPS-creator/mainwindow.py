from PyQt5 import QtCore, QtWidgets,uic
from PyQt5.sip import delete
from settings import settings
from TestLayout import Test


class MainWindow(QtWidgets.QMainWindow): 
	allTests:QtWidgets.QVBoxLayout 
	subroutine_name:QtWidgets.QLineEdit
	EC_TestPoints:QtWidgets.QDoubleSpinBox
	TestPoints:QtWidgets.QDoubleSpinBox
	PromptPoints:QtWidgets.QDoubleSpinBox
	RequireUserInput:QtWidgets.QCheckBox
	BareMode:QtWidgets.QCheckBox
	Shuffle:QtWidgets.QCheckBox
	ShowLevel:QtWidgets.QComboBox
	message:QtWidgets.QTextEdit
	SaveSettingsBtn:QtWidgets.QPushButton
	LoadSettingsBtn:QtWidgets.QPushButton
	RunMipsBtn:QtWidgets.QPushButton
	CreateTarBtn:QtWidgets.QPushButton
	AddTestButton:QtWidgets.QPushButton

	def __init__(self): 
		super(MainWindow, self).__init__() 
		uic.loadUi('ui_files/mainwindow.ui', self)
		self.allTests.addStretch(500)
		self.AddTestButton.pressed.connect(self.addTest) 
		self.SaveSettingsBtn.pressed.connect(self.SaveSettings)
		self.numberOfTests=0
		self.lastSaveFile=""
		self.lastSaveDirectory=""


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
		return newTest

	def SaveSettings(self):
		sa=False
		so=False
		i = self.ShowLevel.currentIndex
		if i == 1:so=True
		if i == 2:sa=True

		setJS = settings(
					subroutine_name = self.subroutine_name.text()	,
					PromptGrade	    = self.PromptPoints.value()		,
					TestGrade		= self.TestPoints.value()		,
					ECTestGrade		= self.EC_TestPoints.value()	,
					MessageToStudent= self.message.toPlainText()	,
					BareMode 		= self.BareMode.isChecked()  	,
					Shuffle 		= self.Shuffle.isChecked() 	,
					RequiresUserInput=self.RequireUserInput.isChecked(),
					ShowAll 		= sa  	,
					ShowAllOutput 	= so  	,
				)
		
		lay=self.allTests
		tests = [lay.itemAt(i).widget() for i in range(lay.count()) ]
		test:Test 
		for test in tests: 
			if test is None: continue
			setJS.AddTest(test.SaveSettings(setJS))

		#output=QtWidgets.QFileDialog.getOpenFileName(self) #file needs to exist
		output=QtWidgets.QFileDialog.getSaveFileName(self,"Save Settings as",self.lastSaveDirectory,"*Setting Files (*.json)")
		print(output)
		with open(output[0], 'w') as f: f.write(setJS.GetJSON())


