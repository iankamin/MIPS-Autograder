from PyQt5 import QtCore, QtWidgets,uic
from PyQt5.QtGui import QFont
from PyQt5.sip import delete
import os
from MIPS_creator.collapsibleBox import CollapsibleBox
from MIPS_creator.utilities import settings,set_Test
from MIPS_creator.TestLayout import Test
from MIPS_creator.ui_files.filepaths import mainwindow_ui
from MIPS_creator.RowTypes import DataRow, OutputRow, UserInputRow,RegisterRow
from .grader_controller import transferFile,showResults, CreateTAR

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
    ExpandBtn:QtWidgets.QPushButton
    CollapseBtn:QtWidgets.QPushButton
    RunMipsBtn:QtWidgets.QPushButton
    CreateTarBtn:QtWidgets.QPushButton
    AddTestButton:QtWidgets.QPushButton
    fontComboBox:QtWidgets.QFontComboBox
    JsonStyle:QtWidgets.QComboBox

    def __init__(self): 
        super(MainWindow, self).__init__() 
        uic.loadUi(mainwindow_ui, self)
        self.allTests.addSpacing(600)
        self.allTests.addStretch(500)
        self.AddTestButton.pressed.connect(self.addTest) 
        self.SaveSettingsBtn.pressed.connect(self.SaveSettings)
        self.LoadSettingsBtn.pressed.connect(self.LoadSettings)
        self.RunMipsBtn.pressed.connect(self.RunMips)
        self.CreateTarBtn.pressed.connect(self.CreateTar)
        self.ExpandBtn.pressed.connect(self.ExpandAll)
        self.CollapseBtn.pressed.connect(self.CollapseAll)
        self.numberOfTests=0
        self.lastSaveLocation=""
        self.ShowLevel.wheelEvent=self.wheelEvent


    # Prevents the scroll wheel from affecting combobox
    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus(): return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)

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

    def ExpandAll(self):
        test:Test
        lay=self.allTests
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for test in items: 
            if test is None: continue
            test.ExpandAndCollapseAll(True)
    def CollapseAll(self):
        test:Test
        lay=self.allTests
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for test in items: 
            if test is None: continue
            test.ExpandAndCollapseAll(False)


    def insertWidget(self,widget): 
        vlay = self.allTests 
        vlay.insertWidget(self.numberOfTests,widget)

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
        delete(test)
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

    def SaveSettings(self,loc=None,updateSaveLocation=True):
        sa=False
        so=False
        i = self.ShowLevel.currentIndex()
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
                    JsonStyle       = self.JsonStyle
                )
        
        lay=self.allTests
        tests = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        test:Test 
        for test in tests: 
            if test is None: continue
            setJS.AddTest(test.convertToJSON(setting=setJS))

        #output=QtWidgets.QFileDialog.getOpenFileName(self) #file needs to exist
        if loc is None:
            output=QtWidgets.QFileDialog.getSaveFileName(self,"Save Settings as",self.lastSaveLocation,"*.json")
            if output[1].replace("*",'') not in output[0]:
                out=output[0].strip()+output[1].replace("*",'')
            else: out=output[0]
            if updateSaveLocation: self.lastSaveLocation=out
            if output[1]:
                with open(out, 'w') as f: f.write(setJS.GetJSON())
        else:
            with open(loc, 'w') as f: f.write(setJS.GetJSON())
    
    def DeleteAllTests(self):
        lay=self.allTests
        tests = [lay.itemAt(i).widget() for i in range(lay.count()) if lay.itemAt(i).widget() is not None]
        test:Test 
        for test in tests: 
            self.deleteTest(test)
        self.numberOfTests=0

    def LoadSettings(self):
        filePath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Settings JSON", self.lastSaveLocation,"*.json") #file needs to exist
        if not filePath[0]: return

        self.DeleteAllTests()
        set=settings(filePath[0])

        self.subroutine_name.setText( set.SubroutineName)
        self.EC_TestPoints.setValue( set.ECTestGrade)
        self.TestPoints.setValue( set.TestGrade)
        self.PromptPoints.setValue( set.PromptGrade)
        self.RequireUserInput.setChecked( set.RequiresUserInput)
        self.BareMode.setChecked( set.BareMode)
        self.Shuffle.setChecked( set.Shuffle)
        self.JsonStyle.setChecked( set.JsonStyle)
        set.MessageToStudent = self.message.toPlainText()
        if set.ShowAll: i = 2
        elif set.ShowAllOutput: i = 1
        else: i=0
        self.ShowLevel.setCurrentIndex(i)
        
        
        testJS:set_Test
        for testJS in set.AllTests:
            #TODO ADD TOP ROW
            test=self.addTest()
            test:Test
            i:set_Test.__RegInput__
            for i in testJS.MemInputs: test.addRow(DataRow, **i.ToDict())
            for i in testJS.RegInputs: 
                if i.ToDict() is None: continue
                test.addRow(RegisterRow,**i.ToDict())
            for i in testJS.UserInput: test.addRow(UserInputRow, text=i)
            for i in testJS.Output: test.addRow(OutputRow, **i.ToDict())

            test.TopRow.replaceInfo(**testJS.ToDict())

    def RunMips(self):
        submissionPath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Assembly file", self.lastSaveLocation,"Assembly Files (*.s *.asm)")[0] #file needs to exist
        if not submissionPath: return
        #submissionPath="/home/kamian/MIPS_Autograder/Tests/part4/part4.s"
        print(submissionPath)
        self.lastSaveLocation=submissionPath
        
        set_file = os.path.join(os.path.dirname(__file__), "temp.json")
        print(set_file)
        self.SaveSettings(set_file)
        transferFile( settingsFile=set_file,
                      submissionFile=submissionPath)
        showResults(self)

    def CreateTar(self):
        TarDestination=QtWidgets.QFileDialog.getSaveFileName(self,"Save TAR File as", self.lastSaveLocation,"TAR File (*.tar *.TAR)")[0] #file needs to exist
        if not TarDestination: return
        self.lastSaveLocation=TarDestination

        set_file = os.path.join(os.path.dirname(__file__), "temp.json")
        print(set_file)
        self.SaveSettings(set_file)
        CreateTAR(set_file, TarDestination,self)





        
