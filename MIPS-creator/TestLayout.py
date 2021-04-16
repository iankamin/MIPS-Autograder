# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from collapsibleBox import CollapsibleBox
from TestLayoutTopRow import Ui_TopRow


class Test(QtWidgets.QWidget): 
    def __init__(self): 
        super(QtWidgets.QWidget, self).__init__() 
        self.setupUi()

    def setupUi(self):
        self.setObjectName("test") 
        self.setMinimumWidth(725)
        self.verticalLayout = QtWidgets.QVBoxLayout(self) 
        
        self.verticalLayout.setObjectName("verticalLayout")
        self.HidingBox=CollapsibleBox("Test")
        self.verticalLayout.addWidget(self.HidingBox)
        self.TopRow=Ui_TopRow()
        self.HidingBox.addWidget(self.TopRow)
        self.allUserInput=CollapsibleBox("User Input",self.HidingBox)
        self.DataInput=CollapsibleBox("Data Input",self.HidingBox)
        self.InputRegisters=CollapsibleBox("Input Registers",self.HidingBox)
        self.OutputRegisters=CollapsibleBox("Output Registers",self.HidingBox)


        Addbutton = QtWidgets.QPushButton()
        self.allUserInput.addWidget()
        self.allUserInput.addWidget(QtWidgets.QPushButton())
        self.allUserInput.addWidget(QtWidgets.QPushButton())
        self.DataInput.addWidget(QtWidgets.QPushButton())
        self.DataInput.addWidget(QtWidgets.QPushButton())
        self.DataInput.addWidget(QtWidgets.QPushButton())
        self.InputRegisters.addWidget(QtWidgets.QPushButton())
        self.InputRegisters.addWidget(QtWidgets.QPushButton())
        self.InputRegisters.addWidget(QtWidgets.QPushButton())
        self.InputRegisters.addWidget(QtWidgets.QPushButton())
        self.OutputRegisters.addWidget(QtWidgets.QPushButton())
        self.OutputRegisters.addWidget(QtWidgets.QPushButton())
    
        


        self.verticalLayout.addStretch()
        self.retranslateUi() 
    def retranslateUi(self): 
        pass
         