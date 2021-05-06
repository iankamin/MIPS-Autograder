from MIPS_creator.ResultsWindow import ResultsWindow
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
    resultsDock:QtWidgets.QDockWidget
    frame:QtWidgets.QFrame
    scrollArea:QtWidgets.QScrollArea
    testScroll:QtWidgets.QScrollArea
    testScrollArea:QtWidgets.QWidget
    rawMipsDock:QtWidgets.QDockWidget
    gradeDock:QtWidgets.QDockWidget
    toggleOutputBtn:QtWidgets.QPushButton

    #1080P size
    #  Window
    #     width=1536
    #     height=801

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
        self.JsonStyle.wheelEvent=self.wheelEvent
        self.rawMipsDock=ResultsWindow("MIPS Output",self)
        self.gradeDock=ResultsWindow("Grade Output",self)
        self.concatAsmDock=ResultsWindow("ASM File",self)
        self.makefileDock=ResultsWindow("Makefile",self)

        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.makefileDock)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.rawMipsDock)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.concatAsmDock)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.gradeDock)
        self.tabifyDockWidget(self.gradeDock,self.rawMipsDock)
        self.tabifyDockWidget(self.gradeDock,self.concatAsmDock)
        self.tabifyDockWidget(self.gradeDock,self.makefileDock)
#        g=self.gradeDock.geometry()
#        g=QtCore.QRect(g.x()-200,g.y(),1000,g.height())
#        self.gradeDock.setGeometry(g)
#        self.rawMipsDock.setGeometry(g)
#        self.concatAsmDock.setGeometry(g)
#        self.makefileDock.setGeometry(g)

        self.outputHidden=True
        self.makefileDock.hide()
        self.rawMipsDock.hide()
        self.concatAsmDock.hide()
        self.gradeDock.hide()
        
        self.toggleOutputBtn.hide()
        self.toggleOutputBtn.pressed.connect(self.toggleOutputPressed)
        self.BareMode.pressed.connect(self.tester)
    
    def wheelEvent(self, *args, **kwargs): 
        if self.hasFocus(): return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)
    
    def toggleOutputPressed(self):
        self.toggleOutput(self.outputHidden)
        self.outputHidden = not self.outputHidden

    def toggleOutput(self, visibile):
        if visibile:
            if self.makefileDock.isUsed : self.makefileDock.show()
            if self.rawMipsDock.isUsed : self.rawMipsDock.show()
            if self.concatAsmDock.isUsed : self.concatAsmDock.show()
            if self.gradeDock.isUsed : self.gradeDock.show()
        else:
            self.makefileDock.hide()
            self.rawMipsDock.hide()
            self.concatAsmDock.hide()
            self.gradeDock.hide()
    

    # Prevents the scroll wheel from affecting combobox
    def tester(self):
        print("\n\n")
        print("Window size")
        print(self.width())
        print("Test Size")
        print(self.allTests.itemAt(0).widget().width())
        print("Makefile Dock Size")
        print(self.makefileDock.width())
        print("grade Dock Size")
        print(self.gradeDock.textBox.width())


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
        setJS = settings(
                    subroutine_name = self.subroutine_name.text()	,
                    PromptGrade	    = self.PromptPoints.value()		,
                    TestGrade		= self.TestPoints.value()		,
                    ECTestGrade		= self.EC_TestPoints.value()	,
                    MessageToStudent= self.message.toPlainText()	,
                    BareMode 		= self.BareMode.isChecked()  	,
                    Shuffle 		= self.Shuffle.isChecked() 	,
                    RequiresUserInput=self.RequireUserInput.isChecked(),
                    ShowLevel       = self.ShowLevel.currentIndex(),
                    JsonStyle       = self.JsonStyle.currentIndex()
                )
        
        lay=self.allTests
        tests = [lay.itemAt(i).widget() for i in range(lay.count()) if lay.itemAt(i).widget() is not None ]
        test:Test 
        for test in tests: 
            setJS.AddTest(test.convertToJSON(setting=setJS))
        if len(tests)==0: return False


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
        return True
    
    def DeleteAllTests(self):
        lay=self.allTests
        tests = [lay.itemAt(i).widget() for i in range(lay.count()) if lay.itemAt(i).widget() is not None]
        test:Test 
        for test in tests: 
            self.deleteTest(test)
        self.numberOfTests=0

    def LoadSettings(self):
        #filePath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Settings JSON", self.lastSaveLocation,"*.json") #file needs to exist
        #if not filePath[0]: return
        filePath=["/home/kamian/MIPS_Autograder/Tests/part4/part4.json"]
        self.DeleteAllTests()
        set=settings(filePath[0])

        self.subroutine_name.setText( set.SubroutineName)
        self.EC_TestPoints.setValue( set.ECTestGrade)
        self.TestPoints.setValue( set.TestGrade)
        self.PromptPoints.setValue( set.PromptGrade)
        self.RequireUserInput.setChecked( set.RequiresUserInput)
        self.BareMode.setChecked( set.BareMode)
        self.Shuffle.setChecked( set.Shuffle)
        self.JsonStyle.setCurrentIndex( set.JsonStyle)
        self.message.setText(set.MessageToStudent)
        self.ShowLevel.setCurrentIndex(set.ShowLevel.value)
        
        
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
        #submissionPath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Assembly file", self.lastSaveLocation,"Assembly Files (*.s *.asm)")[0] #file needs to exist
        #if not submissionPath: return
        #submissionPath="/home/kamian/MIPS_Autograder/Tests/part4/part4.s"
        submissionPath="/home/kamian/MIPS_Autograder/Tests/part4/iankamin@buffalo.edu_30_handin.s"
        print(submissionPath)
        self.lastSaveLocation=submissionPath
        
        set_file = os.path.join(os.path.dirname(__file__), "temp.json")
        print(set_file)
        success = self.SaveSettings(set_file)
        if not success: return
        
        transferFile( settingsFile=set_file,
                      submissionFile=submissionPath)
        showResults(self)
        self.toggleOutputBtn.show()
        self.outputHidden=False
        self.toggleOutput(True)
        self.gradeDock.raise_()

    def CreateTar(self):
        TarDestination=QtWidgets.QFileDialog.getSaveFileName(self,"Save TAR File as", self.lastSaveLocation,"TAR File (*.tar *.TAR)")[0] #file needs to exist
        if not TarDestination: return
        self.lastSaveLocation=TarDestination

        set_file = os.path.join(os.path.dirname(__file__), "temp.json")
        print(set_file)
        success = self.SaveSettings(set_file)
        if not success: return
        CreateTAR(set_file, TarDestination,self)
        self.toggleOutputBtn.show()
        self.outputHidden=False
        self.toggleOutput(True)
        self.makefileDock.raise_()







        
