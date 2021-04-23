# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from collapsibleBox import CollapsibleBox
from classes import *
from copy import deepcopy



class Test(QtWidgets.QWidget): 
    def __init__(self,index,parent,TopRow=None): 
        super(QtWidgets.QWidget, self).__init__() 
        self.parent=parent
        if TopRow is None or TopRow.TestName.text()=="": self._name="Test"
        else: self._name = TopRow.TestName.text()
        self.TopRow=TopRow
        self._index=index
        self.setupUi()

    @property
    def name(self): return self._name
    @name.setter
    def name(self,s):
        if s == "": self._name = "Test"
        else: self._name=s
        self.HidingBox.toggle_button.setText("%s - %s"%(self.name,self.index))
    def setName(self,s):
        self.name=s
    @property
    def index(self): return self._index
    @index.setter
    def index(self,i):
        self._index=i
        self.HidingBox.indexUpdated(i)
        self.HidingBox.toggle_button.setText("%s - %s"%(self.name,self.index))

    def setupUi(self):
        self.setObjectName("test") 
        self.setMinimumWidth(550)
        self.verticalLayout = QtWidgets.QVBoxLayout(self) 
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
        if self.TopRow is None:self.TopRow=TestTopRow()
        
        self.HidingBox=CollapsibleBox("%s - %s"%(self.name,self.index),index=self.index)
        self.HidingBox.content_area.layout().setContentsMargins(20,0,0,0)
        
        self.verticalLayout.addWidget(self.HidingBox)

        self.TopRow.TestName.textChanged.connect(self.setName)
        self.HidingBox.addWidget(self.TopRow)
        self.allUserInput=CollapsibleBox("User Input",self.HidingBox,self.addUserInputRow)
        self.DataInput=CollapsibleBox("Data Input",self.HidingBox,self.addDataRow)
        self.InputRegisters=CollapsibleBox("Input Registers",self.HidingBox,self.addRegisterRow)
        self.Outputs=CollapsibleBox("Output Registers",self.HidingBox,self.addOutputRow)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.TopRow.CopyButton.pressed.connect(self.Copy) 
        self.TopRow.DeleteButton.pressed.connect(self.deleteSelf)

        self.verticalLayout.addStretch()
        self.retranslateUi() 
    
    def deleteSelf(self): 
        self.parent.deleteTest(self)
    def __del__(self):
        del self.TopRow
        del self.allUserInput
        del self.DataInput
        del self.InputRegisters
        del self.Outputs
        
    #TODO make the add user input button work
    def addUserInputRow(self,row=None):
        if row is None:row=UserInputRow(parent=self.allUserInput)
        else: row.parent = self.allUserInput
        row.Deleted.connect(self.rowDeleted)
    
    def addDataRow(self,row=None):
        if row is None: row=DataRow(parent=self.DataInput)
        else: row.parent = self.DataInput
        row.Deleted.connect(self.rowDeleted)
    
    def addRegisterRow(self, row=None):
        if row is None: row=RegisterRow(parent=self.InputRegisters)
        else: row.parent = self.InputRegisters
        row.Deleted.connect(self.rowDeleted)
    
    def addOutputRow(self,row=None):
        if row is None: row=OutputRow(parent=self.Outputs)
        else: row.parent = self.Outputs
        row.Deleted.connect(self.rowDeleted)
   
    def rowDeleted(self, row,box):
        box.updateHeight(row,Forward=False)

    
    def Copy(self):
        newTest = deepcopy(self)
        self.parent.addTest(newTest)

    def retranslateUi(self): 
        pass
         
    def __deepcopy__(self,_):
        topRow=self.TopRow.copy()
        copy = Test(index=self.index,parent=self.parent,TopRow=topRow)
        
        lay=self.allUserInput.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not UserInputRow: continue
            copy.addUserInputRow(item.copy())
        
        lay=self.DataInput.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not DataRow: continue
            copy.addDataRow(item.copy())
        
        lay=self.InputRegisters.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not RegisterRow: continue
            copy.addRegisterRow(item.copy())
        
        lay=self.Outputs.content_area.layout()
        items = [lay.itemAt(i).widget() for i in range(lay.count()) ]
        for item in items: 
            i=type(item)
            if i is not OutputRow: continue
            copy.addOutputRow(item.copy())

        return copy