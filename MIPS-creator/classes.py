import random
from PyQt5 import QtWidgets,uic
from PyQt5.sip import delete
from PyQt5.QtCore import pyqtSignal


class Row(QtWidgets.QWidget):
    Deleted = pyqtSignal(QtWidgets.QWidget,QtWidgets.QAbstractScrollArea)
    def __init__(self):
        super(QtWidgets.QWidget,self).__init__()
        self.parent=None
    def delete(self):
        self.Deleted.emit(self,self.parent)
        delete(self)

class TestTopRow(QtWidgets.QWidget):
    def __init__(self): 
       super(QtWidgets.QWidget, self).__init__()
       uic.loadUi('TestLayoutTopRow.ui', self)

class UserInputRow(Row):
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('UserInputRow.ui', self)
        self.parent=parent
        if parent is not None: self.parent.addWidget(self)
        self.DeleteButton.pressed.connect(self.delete)

    
class DataRow(Row):
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('DataRow.ui', self)
        self.parent=parent
        if parent is not None: self.parent.addWidget(self)
        self.DeleteButton.pressed.connect(self.delete)

class RegisterRow(Row):
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('regInput.ui', self)
        self.parent=parent
        if parent is not None: self.parent.addWidget(self)
        self.DeleteButton.pressed.connect(self.delete)

class OutputRow(Row):
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('regOutput.ui', self)
        self.parent=parent
        if parent is not None: self.parent.addWidget(self)
        self.DeleteButton.pressed.connect(self.delete)
        self.address.hide()
        
        self.type:QtWidgets.QComboBox
        self.type.currentIndexChanged.connect(self.ComboBoxChanged)
    
    def ComboBoxChanged(self,i):
        print(i)
        if i==0 or i==1: 
            self.register_2.show()
            self.address.hide()
        if i==2:
            self.register_2.hide()
            self.address.show()

    