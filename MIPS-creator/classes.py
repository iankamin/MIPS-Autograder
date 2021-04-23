import random
from PyQt5 import QtWidgets,uic
from PyQt5.sip import delete
from PyQt5.QtCore import pyqtSignal


class Row(QtWidgets.QWidget):
    Deleted = pyqtSignal(QtWidgets.QWidget,QtWidgets.QAbstractScrollArea)
    def __init__(self):
        super(QtWidgets.QWidget,self).__init__()
        self._parent=None

    def delete(self):
        self.Deleted.emit(self,self.parent)
        delete(self)
    
    @property
    def parent(self):
        return self._parent
    def height(self):
        return super().sizeHint().height()
    @parent.setter
    def parent(self,parent):
        self._parent=parent
        if parent is None: return
        self._parent.addWidget(self)

class TestTopRow(QtWidgets.QWidget):
    TestName:QtWidgets.QLineEdit
    ShowLevel:QtWidgets.QComboBox
    MaxPoints:QtWidgets.QDoubleSpinBox
    ExtraCredit:QtWidgets.QCheckBox
    CopyButton:QtWidgets.QPushButton
    DeleteButton:QtWidgets.QPushButton
    def __init__(self): 
       super(QtWidgets.QWidget, self).__init__()
       uic.loadUi('TestLayoutTopRow.ui', self)
    def copy(self):
        copy=TestTopRow()
        copy.TestName.setText(self.TestName.text())
        copy.ShowLevel.setCurrentIndex(self.ShowLevel.currentIndex())
        copy.MaxPoints.setValue(self.MaxPoints.value())
        copy.ExtraCredit.setChecked(self.ExtraCredit.isChecked())
        return copy


class UserInputRow(Row):
    DeleteButton:QtWidgets.QPushButton
    UserInput:QtWidgets.QLineEdit
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('UserInputRow.ui', self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)

    def copy(self):
        copy=UserInputRow()
        copy.UserInput.setText(self.UserInput.text())
        return copy
    
class DataRow(Row):
    DeleteButton:QtWidgets.QPushButton
    address:QtWidgets.QLineEdit
    data:QtWidgets.QLineEdit
    type:QtWidgets.QComboBox
    reg:QtWidgets.QComboBox
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('DataRow.ui', self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
    
    def copy(self):
        copy=DataRow()
        copy.address.setText(self.address.text())
        copy.data.setText(self.data.text())
        copy.type.setCurrentIndex(self.type.currentIndex())
        copy.reg.setCurrentIndex(self.reg.currentIndex())
        return copy
    

class RegisterRow(Row):
    DeleteButton:QtWidgets.QPushButton
    reg:QtWidgets.QLineEdit
    value:QtWidgets.QLineEdit
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('regInput.ui', self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
    
    def copy(self):
        copy=RegisterRow()
        copy.reg.setText(self.reg.text())
        copy.value.setText(self.value.text())
        return copy

class OutputRow(Row):
    DeleteButton:QtWidgets.QPushButton
    reg:QtWidgets.QLineEdit
    type:QtWidgets.QComboBox
    address:QtWidgets.QLineEdit
    CorrectAnswer:QtWidgets.QLineEdit
    def __init__(self,parent=None): 
        super().__init__()
        uic.loadUi('regOutput.ui', self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
        self.address.hide()
        
        self.type:QtWidgets.QComboBox
        self.type.currentIndexChanged.connect(self.ComboBoxChanged)
    
    def ComboBoxChanged(self,i):
        print(i)
        if i==0 or i==1: 
            self.reg.show()
            self.address.hide()
        if i==2:
            self.reg.hide()
            self.address.show()

    def copy(self):
        copy=OutputRow()
        copy.address.setText(self.address.text())
        copy.CorrectAnswer.setText(self.CorrectAnswer.text())
        copy.reg.setText(self.reg.text())
        copy.type.setCurrentIndex(self.type.currentIndex())
        return copy
    