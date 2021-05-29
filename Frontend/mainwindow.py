from typing import List, Tuple
from types import resolve_bases
from Frontend.ResultsWindow import ResultsWindow
from PyQt5 import QtCore, QtWidgets,uic
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtCore import QObject, QThread

from PyQt5.sip import delete
import os
import Autograder
try: from .resources.filepaths import resource_path, ui,Icons
except: from resources.filepaths import resource_path, ui,Icons
try: from .grader_controller import *
except: from grader_controller import *
try: from .utilities import settings,settingsWorker
except: from utilities import settings,settingsWorker
try: from .TestLayout import Test
except: from TestLayout import Test
try: from .RowTypes import DataRow,RegisterRow,UserInputRow,OutputRow
except: from RowTypes import DataRow,RegisterRow,UserInputRow,OutputRow

class MainWindow(QtWidgets.QMainWindow): 
    AllGradedTests:QtWidgets.QVBoxLayout 
    AllSampleTests:QtWidgets.QVBoxLayout 
    AllCurrentTests:QtWidgets.QVBoxLayout 
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
    skeletonScrollArea:QtWidgets.QScrollArea
    currentTestArea:QtWidgets.QWidget
    rawMipsDock:ResultsWindow
    gradeDock:ResultsWindow
    concatAsmDock:ResultsWindow
    makefileDock:ResultsWindow
    errorDock:ResultsWindow
    toggleOutputBtn:QtWidgets.QPushButton
    tabWidget:QtWidgets.QTabWidget
    actionSave_Settings:QtWidgets.QAction
    actionLoad_Settings:QtWidgets.QAction
    actionCreate_TAR_File:QtWidgets.QAction
    
    actionRun_MIPS_File:QtWidgets.QAction
    actionAdd_New_Test:QtWidgets.QAction
    actionGenerate_Skeleton_Code:QtWidgets.QAction

    actionExpand_All_Tests:QtWidgets.QAction
    actionCollapse_All_Tests:QtWidgets.QAction
    actionValidate_Tests:QtWidgets.QAction
    actionHide_Output_Window:QtWidgets.QAction


    #1080P size
    #  Window
    #     width=1536
    #     height=801


    def __init__(self): 
        super(MainWindow, self).__init__() 
        uic.loadUi(ui.mainwindow, self)
        self.threads=[]
        self.workers=[]
        self.AllGradedTests.addSpacing(600)
        self.AllGradedTests.addStretch(500)
        self.AllSampleTests.addSpacing(600)
        self.AllSampleTests.addStretch(500)
        self.numberOfTests=0
        self.numberOfSamples=0
        self.lastSaveLocation=""
        self.UI_ButtonConnections()
        self.UI_SettingsFrame()
        self.UI_DockWidgets()
        self.BareMode.pressed.connect(self.tester)
        self.UI_TabWidget()
        self.UI_ActionMenu()
    def UI_ButtonConnections(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Icons.downArrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExpandBtn.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Icons.upArrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CollapseBtn.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Icons.rightArrow), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleOutputBtn.setIcon(icon)
        self.AddTestButton.pressed.connect(self.addTest) 
        self.SaveSettingsBtn.pressed.connect(self.SaveSettings)
        self.LoadSettingsBtn.pressed.connect(self.LoadSettings)
        self.RunMipsBtn.pressed.connect(self.RunMips)
        self.CreateTarBtn.pressed.connect(self.CreateTar)
        self.ExpandBtn.pressed.connect(self.ExpandAll)
        self.CollapseBtn.pressed.connect(self.CollapseAll)
        self.toggleOutputBtn.pressed.connect(self.toggleOutputPressed)
    def UI_SettingsFrame(self):
        self.ShowLevel.wheelEvent=self.wheelEvent
        self.JsonStyle.wheelEvent=self.wheelEvent
    def UI_DockWidgets(self):   
        self.rawMipsDock=ResultsWindow("MIPS Output",self)
        self.gradeDock=ResultsWindow("Grade Output",self)
        self.concatAsmDock=ResultsWindow("ASM File",self)
        self.makefileDock=ResultsWindow("Makefile",self)
        self.errorDock=ResultsWindow("Errors",self)
        self.docks=[self.gradeDock,self.rawMipsDock,self.concatAsmDock,self.makefileDock,self.errorDock]
        for dock in self.docks: self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        for dock in self.docks[1:]: self.tabifyDockWidget(self.docks[0],dock)
        
        self.outputHidden=True
        for dock in self.docks:
            dock.hide()

        self.toggleOutputBtn.hide()
    def UI_TabWidget(self):
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.tabWidget.setCurrentIndex(1)
    def UI_ActionMenu(self):
        self.actionGenerate_Skeleton_Code.triggered.connect(self.createSkeletonCode)
        self.actionAdd_New_Test.triggered.connect(self.addTest) 
        self.actionSave_Settings.triggered.connect(self.SaveSettings)
        self.actionLoad_Settings.triggered.connect(self.LoadSettings)
        self.actionRun_MIPS_File.triggered.connect(self.RunMips)
        self.actionCreate_TAR_File.triggered.connect(self.CreateTar)
        self.actionExpand_All_Tests.triggered.connect(self.ExpandAll)
        self.actionCollapse_All_Tests.triggered.connect(self.CollapseAll)
        self.actionHide_Output_Window.triggered.connect(self.toggleOutputPressed)
        self.actionValidate_Tests.triggered.connect(self.validate)

    @property
    def currentNumberOfTests(self):
        if self.tabWidget.currentWidget().objectName() =='skeleton': return self.numberOfSamples
        if self.tabWidget.currentWidget().objectName() =='grading': return self.numberOfTests
    @currentNumberOfTests.setter
    def currentNumberOfTests(self,value):
        if self.tabWidget.currentWidget().objectName() =='skeleton': self.numberOfSamples = value
        if self.tabWidget.currentWidget().objectName() =='grading': self.numberOfTests = value

    def tabChanged(self, index) -> None:
        if self.tabWidget.widget(index).objectName()=='skeleton':
            self.currentTestArea=self.skeletonScrollArea
            self.AllCurrentTests=self.AllSampleTests
            self.SkeltonCreatorMode=True

        if self.tabWidget.widget(index).objectName()=='grading':
            self.currentTestArea=self.testScrollArea
            self.AllCurrentTests=self.AllGradedTests
            self.SkeltonCreatorMode=False
            
    def wheelEvent(self, *args, **kwargs) -> None: 
        if self.hasFocus(): return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)
    
    def toggleOutputPressed(self):
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(Icons.rightArrow)
            if self.outputHidden else 
            QtGui.QPixmap(Icons.leftArrow) 
            ,QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleOutputBtn.setIcon(icon)

        self.toggleOutput(self.outputHidden)
        self.outputHidden = not self.outputHidden

    def toggleOutput(self, visibile):
        if visibile:
            for dock in self.docks: dock.show() if dock.canShow() else None
        else:
            for dock in self.docks: dock.hide()
    
    # Prevents the scroll wheel from affecting combobox
    def tester(self):
        print("\n\n")
        print("Window size")
        print(self.width())
        print("Test Size")
        print(self.AllGradedTests.itemAt(0).widget().width())
        print("Makefile Dock Size")
        print(self.makefileDock.width())
        print("grade Dock Size")
        print(self.gradeDock.textBox.width())

    def ExpandAll(self):
        test:Test
        items=self.getTests()
        for test in items: 
            if test is None: continue
            test.ExpandAndCollapseAll(True)
    def CollapseAll(self):
        test:Test
        lay=self.AllCurrentTests
        items=self.getTests()
        for test in items: 
            test.ExpandAndCollapseAll(False)

    def insertWidget(self,widget): 
        vlay = self.AllCurrentTests 
        vlay.insertWidget(self.currentNumberOfTests,widget)

    def updateAllTestIndices(self):
        items=self.getTests()
        test:Test 
        for i,test in enumerate(items): 
            test.index=i
            test.name=test.name
        
    def deleteTest(self,test:Test): 
        lay=self.AllCurrentTests
        lay.removeWidget(test)
        self.currentNumberOfTests-=1
        self.currentNumberOfTests = 0 if self.currentNumberOfTests < 0 else self.currentNumberOfTests
        delete(test)
        self.updateAllTestIndices()
            
    def addTest(self,newTest=None): 
        vlay = self.AllCurrentTests 
        index=self.currentNumberOfTests
        if newTest is None: 
            newTest=Test(index=index,parent=self,isSkelton=self.SkeltonCreatorMode)
        else: 
            newTest.index=index
            newTest.name=newTest.name
        self.insertWidget(newTest)
        self.currentNumberOfTests+=1
        self.setStyleSheet(self.styleSheet())
        self.setStyle(self.style())
        return newTest
    def getTests(self,lay=None) -> List[Test]:
        if lay is None: lay=self.AllCurrentTests
        items = [lay.itemAt(i).widget() for i in range(lay.count()) if lay.itemAt(i).widget()is not None ]
        return items

    def validateWindow(self) -> Tuple[bool,str]:
        valid=True
        output=""

        if self.subroutine_name.text()=="": 
            self.subroutine_name.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            output+="\n - Subroutine Name is required"
            valid = False
        else: 
            self.subroutine_name.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid= valid and True
        
        if self.SkeltonCreatorMode: return valid,output
        
        if self.TestPoints.value()==0:
            self.TestPoints.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            output+="\n - Test Points Cannot be zero"
            valid = False
        else: 
            self.TestPoints.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid= valid and True
        
        return valid,output
    def validateTests(self) -> Tuple[bool,str]:
        output=""
        valid = True
        
        if self.currentNumberOfTests == 0: 
            output+="\n\n - No Tests to Run"
            valid = False
            return valid,output
       
        test:Test
        tests = self.getTests(self.AllGradedTests)
        for test in tests:  
            v, out=test.validate()
            if not v:
                valid = False
                output+='\n'+out
        return valid,output

    def validate(self) -> bool:
        validWind,outputWind=self.validateWindow()
        validTests,outputTests=self.validateTests()
        valid = validWind and validTests
    
        if not valid: 
            self.outputHidden=False
            self.toggleOutputBtn.show()
            output="\n cannot proceed until the following issues are corrected\n===============================================\n"
            output+=outputWind+outputTests
            errorDisplay(self,output)
        else:
            errorDisplay(self,"")
            
        return valid

    def convertToSettings(self,layout) -> Tuple[bool,settings]:
        setting = settings(
                    subroutine_name = self.subroutine_name.text()	,
                    PromptGrade	    = self.PromptPoints.value()		,
                    TestGrade		= self.TestPoints.value()		,
                    ECTestGrade		= self.EC_TestPoints.value()	,
                    MessageToStudent= self.message.toPlainText()	,
                    BareMode 		= self.BareMode.isChecked()  	,
                    Shuffle 		= self.Shuffle.isChecked() 	,
                    RequiresUserInput=self.RequireUserInput.isChecked(),
                    ShowLevel       = self.ShowLevel.currentIndex(),
                    JsonStyle       = self.JsonStyle.currentIndex())

        valid=True
        tests = self.getTests(layout)
        for test in tests: 
            setting.AddTest(test.convertToSettingsTest(setting=setting))
        if len(tests)==0: return False,None
        if not valid: return False,None

        return True,setting

    def SaveSettings(self,loc=None,updateSaveLocation=True) -> bool:
        self.tabWidget.setCurrentIndex(1)
        if not self.validate(): return False

        success,setting = self.convertToSettings(self.AllGradedTests)
        if not success: return False

        #output=QtWidgets.QFileDialog.getOpenFileName(self) #file needs to exist
        if loc is None:
            output=QtWidgets.QFileDialog.getSaveFileName(self,"Save Settings as",self.lastSaveLocation,"*.json")
            if output[1].replace("*",'') not in output[0]:
                out=output[0].strip()+output[1].replace("*",'')
            else: out=output[0]
            if updateSaveLocation: self.lastSaveLocation=os.path.split(out)[0]+'/'
            if output[1]:
                with open(out, 'w') as f: f.write(setting.GetJSON())
        else:
            with open(loc, 'w') as f: f.write(setting.GetJSON())
        return True
    
    def DeleteAllTests(self):
        lay=self.AllGradedTests
        tests = self.getTests(self.AllGradedTests)
        test:Test 
        for test in tests: 
            self.deleteTest(test)
        self.numberOfTests=0

    def createThread(self,worker:QObject,workerFunction,*onfinish):
        self.threads.append(QThread())
        self.workers.append(worker)
        thread:QThread
        thread=self.threads[-1]
        worker=self.workers[-1]
        worker.moveToThread(thread)
        thread.started.connect(workerFunction)
        for f in onfinish:
            worker.finished.connect(f)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.start()

    def LoadSettings(self):
        self.tabWidget.setCurrentIndex(1)
        filePath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Settings JSON", self.lastSaveLocation,"*.json")[0] #file needs to exist
        if not filePath: return
        self.lastSaveLocation=os.path.split(filePath)[0]+'/'
       # filePath=["/home/kamian/MIPS_Autograder/Tests/part4/part4.json"]
        self.DeleteAllTests()

        worker=settingsWorker(file=filePath)
        self.createThread(worker,worker.get,self.LoadSettings_2)

        #set=settings(filePath)
    def LoadSettings_2(self,set:settings):
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
        
        testJS:settings.set_Test
        for testJS in set.AllTests:
            #TODO ADD TOP ROW
            test=self.addTest()
            test:Test
            i:Autograder.Test.__RegInput__
            for i in testJS.MemInputs: test.addRow(DataRow, **i.ToDict())
            for i in testJS.RegInputs: 
                if i.ToDict() is None: continue
                test.addRow(RegisterRow,**i.ToDict())
            for i in testJS.UserInput: test.addRow(UserInputRow, text=i)
            for i in testJS.Output: test.addRow(OutputRow, **i.ToDict())

            test.TopRow.replaceInfo(**testJS.ToDict())

    def createSkeletonCode(self):
        self.tabWidget.setCurrentIndex(0)
        if not self.validate(): return
        success,setting = self.convertToSettings(self.AllSampleTests)
        if not success: return
        code=Autograder.createSkeletonCode(setting)
        self.concatAsmDock.setContents(code,showLineNumbers=True)
        self.concatAsmDock.raise_()

    def RunMips(self):
        self.tabWidget.setCurrentIndex(1)
        self.outputHidden=False
        self.toggleOutputBtn.show()
        errorDisplay(self,"\n\n\n\n   Autograder in progress")
        
        set_file = resource_path("temp.json")
        print(set_file)
        success = self.SaveSettings(set_file)
        if not success: return
        
        
        submissionPath=QtWidgets.QFileDialog.getOpenFileName(self,"Select Assembly file", self.lastSaveLocation,"Assembly Files (*.s *.asm)")[0] #file needs to exist
        if not submissionPath: return
        # submissionPath="/home/kamian/MIPS_Autograder/Tests/part4/part4.s"
        # submissionPath="/home/kamian/MIPS_Autograder/Tests/part4/iankamin@buffalo.edu_30_handin.s"
        print(submissionPath)
        self.lastSaveLocation=os.path.split(submissionPath)[0]+'/'
        
        mips=MipsWorker ( settingsFile=set_file, submissionFile=submissionPath)
        self.createThread(mips,mips.run,self.runMips_2)

    def runMips_2(self):
        outputDisplay(self)
        self.toggleOutput(True)
        self.gradeDock.raise_()

    def CreateTar(self):
        self.tabWidget.setCurrentIndex(1)
        self.outputHidden=False
        self.toggleOutputBtn.show()
        TarDestination=QtWidgets.QFileDialog.getSaveFileName(self,"Save TAR File as", self.lastSaveLocation,"TAR File (*.tar *.TAR)")[0] #file needs to exist
        if not TarDestination: return
        self.lastSaveLocation=os.path.split(TarDestination)[0]+'/'
        set_file = resource_path("temp.json")
        print(set_file)
        success = self.SaveSettings(set_file,updateSaveLocation=False)
        if not success: return
        CreateTAR(set_file, TarDestination,self)
        deleteFile(set_file)
        self.toggleOutput(True)
        self.makefileDock.raise_()







        
