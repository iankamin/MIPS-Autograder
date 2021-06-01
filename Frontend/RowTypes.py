from abc import abstractmethod
import random
from PyQt5 import QtWidgets,uic
from PyQt5.QtGui import QRegExpValidator
from PyQt5.sip import delete
from PyQt5.QtCore import QRegExp, pyqtSignal
try: from .resources import ui,Icons
except: from resources import ui,Icons
try: from .utilities import validity
except: from utilities import validity

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
    
    @staticmethod
    def createFromJSON(**kwargs):return
    
    @abstractmethod
    def getKwargs(self): raise NotImplementedError()
    
    def regLimit(self,text:str):
        if len(text)==0: return
        if text[0] in ['f','$']:
            self.reg.setMaxLength(3)
        else:
            self.reg.setMaxLength(2)
    
    def addressChanged(self,text:str):
        self.address:QtWidgets.QLineEdit
        if len(text) == 0: return
        if text[0]=='-': self.address.setMaxLength(11)
        else: self.address.setMaxLength(10)
        if text[-1] not in "-x0123456789abcdefABCDEF": self.address.setText(text[:-1])
    
    # Prevents the scroll wheel from affecting combobox
    def scrollWheelEvent(self, *args, **kwargs):
        if self.hasFocus(): return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)
    
        


class TestTopRow(QtWidgets.QWidget):
    TestName:QtWidgets.QLineEdit
    ShowLevel:QtWidgets.QComboBox
    MaxPoints:QtWidgets.QDoubleSpinBox
    ExtraCredit:QtWidgets.QCheckBox
    CopyButton:QtWidgets.QPushButton
    DeleteButton:QtWidgets.QPushButton
    def __init__(self,name=None,ShowLevel=None,MaxPoints=None,ExtraCredit=None): 
        super(QtWidgets.QWidget, self).__init__()
        uic.loadUi(ui.TopRow, self)
        self.ShowLevel.wheelEvent = self.wheelEvent
        self.MaxPoints.wheelEvent = self.wheelEvent
        
        if(name) is not None: self.TestName.setText(name)
        if(ShowLevel) is not None: self.ShowLevel.setCurrentIndex(ShowLevel)
        if(ExtraCredit) is not None: self.MaxPoints.setValue(ExtraCredit)
        if(MaxPoints) is not None: self.ExtraCredit.setChecked(MaxPoints)
    # Prevents the scroll wheel from affecting combobox
    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus(): 
            return QtWidgets.QComboBox.wheelEvent(self, *args, **kwargs)
    def copy(self):
        copy=TestTopRow()
        copy.TestName.setText(self.TestName.text())
        copy.ShowLevel.setCurrentIndex(self.ShowLevel.currentIndex())
        copy.MaxPoints.setValue(self.MaxPoints.value())
        copy.ExtraCredit.setChecked(self.ExtraCredit.isChecked())
        return copy
    def GetKwargs(self):
        return {
            'ShowLevel':self.ShowLevel.currentIndex()      ,
            'testName':self.TestName.text() or self.TestName.placeholderText()  ,
            'ExtraCredit':self.ExtraCredit.isChecked(),
            'OutOf':self.MaxPoints.value() 
            }
    def replaceInfo(self,name=None,ShowLevel=None,OutOf=None,ExtraCredit=None,**kwargs):
        if (name is not None) and (name != self.TestName.placeholderText()): self.TestName.setText(name)
        if(ShowLevel) is not None: self.ShowLevel.setCurrentIndex(ShowLevel)
        if(ExtraCredit) is not None: self.MaxPoints.setValue(OutOf)
        if(OutOf) is not None: self.ExtraCredit.setChecked(ExtraCredit)

class PromptRegexRow(Row):
    DeleteButton:QtWidgets.QPushButton
    RegexExp:QtWidgets.QLineEdit
    def __init__(self,parent=None,text=None): 
        super().__init__()
        uic.loadUi(ui.RegexRow, self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
        if(text) is not None: self.RegexExp.setText(text)

    def copy(self):
        copy=PromptRegexRow()
        copy.RegexExp.setText(self.RegexExp.text())
        return copy
    def validate(self):
        if len(self.RegexExp.text())== 0: 
            self.RegexExp.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            return False
        else: 
            self.RegexExp.setStyleSheet("background-color: rgb(255, 255, 255);")
            return True
    def getKwargs(self): return {"PromptRegex":self.RegexExp.text()}

class UserInputRow(Row):
    DeleteButton:QtWidgets.QPushButton
    UserInput:QtWidgets.QLineEdit
    def __init__(self,parent=None,text=None): 
        super().__init__()
        uic.loadUi(ui.UserInputRow, self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
        if(text) is not None: self.UserInput.setText(text)

    def copy(self):
        copy=UserInputRow()
        copy.UserInput.setText(self.UserInput.text())
        return copy
    def validate(self):
        if len(self.UserInput.text())== 0: 
            self.UserInput.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            return False
        else: 
            self.UserInput.setStyleSheet("background-color: rgb(255, 255, 255);")
            return True
    def getKwargs(self): return {"UserInput":self.UserInput.text()}
    
class DataRow(Row):
    DeleteButton:QtWidgets.QPushButton
    address:QtWidgets.QLineEdit
    data:QtWidgets.QLineEdit
    type:QtWidgets.QComboBox
    reg:QtWidgets.QComboBox
    def __init__(self,parent=None,addr=None,data=None,type=None,reg=None): 
        super().__init__()
        uic.loadUi(ui.DataRow, self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
        
        self.reg.setValidator(validity.registerRegexValidator)
        self.address.setValidator(validity.addressRegexValidator)

        self.type.wheelEvent=self.wheelEvent
        self.reg.wheelEvent=self.wheelEvent
        
        if reg is not None: self.reg.setCurrentText(reg)
        if type is not None: self.type.setCurrentText(type.replace(".",'').lower())
        if addr is not None: self.address.setText(addr)
        if data is not None: self.data.setText(data)
    def validate(self):
        valid = True
        if len(self.data.text())== 0: 
            self.data.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            valid = False
        else: 
            self.data.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid = valid and True
        
        if len(self.address.text())== 0: 
            self.address.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            valid = False
        else: 
            self.address.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid = valid and True
        return valid
    def copy(self):
        copy=DataRow()
        copy.address.setText(self.address.text())
        copy.data.setText(self.data.text())
        copy.type.setCurrentIndex(self.type.currentIndex())
        copy.reg.setCurrentIndex(self.reg.currentIndex())
        return copy
    def getKwargs(self):
        regI=self.reg.currentIndex()
        if regI == 0: reg=None
        else: reg=self.reg.currentText()
        return {
            'reg':reg,
            'addr':self.address.text(),
            'data':self.data.text(),
            'type':self.type.currentText()
        }
    
class RegisterRow(Row):
    DeleteButton:QtWidgets.QPushButton
    reg:QtWidgets.QLineEdit
    value:QtWidgets.QLineEdit
    def __init__(self,parent=None,reg=None,value=None): 
        super().__init__()
        uic.loadUi(ui.RegInput, self)
        self.parent=parent
        self.DeleteButton.pressed.connect(self.delete)
        self.reg.textChanged.connect(self.regLimit)
        
        if reg is not None: self.reg.setText(reg)
        if value is not None: self.value.setText(value)
    def validate(self):
        valid = True
        if len(self.reg.text())== 0: 
            self.reg.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            valid = False
        else: 
            self.reg.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid = valid and True
        if len(self.value.text())== 0: 
            self.value.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            valid = False
        else: 
            self.value.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid = valid and True
        return valid
    def copy(self):
        copy=RegisterRow()
        copy.reg.setText(self.reg.text())
        copy.value.setText(self.value.text())
        return copy
    def getKwargs(self):
        return{
            'reg':self.reg.text(),
            'value':self.value.text()
        }
    def valueLimit(self,text:str):
        if text[0]=='-': self.value.setMaxLength(11)
        else: self.value.setMaxLength(10)


class OutputRow(Row):
    DeleteButton:QtWidgets.QPushButton
    reg:QtWidgets.QLineEdit
    type:QtWidgets.QComboBox
    address:QtWidgets.QLineEdit
    CorrectAnswer:QtWidgets.QLineEdit
    def __init__(self,parent=None,reg=None,type=None,addr=None,CorrectAnswer=None): 
        super().__init__()
        uic.loadUi(ui.RegOutput, self)
        self.parent=parent
        self.address.hide()
        self.type.currentTextChanged.connect(self.ComboBoxChanged)
        
        self.DeleteButton.pressed.connect(self.delete)
        self.type.wheelEvent=self.wheelEvent
        
        if type is not None: 
            type=self.getSyscall(type)
            if validity.isInt(type): self.type.setCurrentText()
            else: self.type.setCurrentText(type)
        if reg is not None: self.reg.setText(reg)
        if addr is not None: self.address.setText(addr)
        if CorrectAnswer is not None: self.CorrectAnswer.setText(CorrectAnswer)
        
        self.reg.textChanged.connect(self.regLimit)
        self.address.textChanged.connect(self.addressChanged)
    def addressChanged(self,text:str):
        if len(text) == 0: return
        #if text[-1] not in "-x0123456789abcdefABCDEF": self.address.setText(text[:-1])
    def validate(self):
        valid = True
        if len(self.CorrectAnswer.text())== 0: 
            self.CorrectAnswer.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
            valid = False
        else: 
            self.CorrectAnswer.setStyleSheet("background-color: rgb(255, 255, 255);")
            valid = valid and True
        
        if self.type.currentText()=="String":
            if len(self.address.text())== 0: 
                self.address.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
                valid = False
            else: 
                self.address.setStyleSheet("background-color: rgb(255, 255, 255);")
                valid = valid and True
        else: 
            if len(self.reg.text())== 0: 
                self.reg.setStyleSheet("border: 1px solid red;background-color: rgb(255, 255, 255);")
                valid = False
            else: 
                self.reg.setStyleSheet("background-color: rgb(255, 255, 255);")
                valid = valid and True
        return valid
    def ComboBoxChanged(self,i):
        #print(i)
        if i=="String":
            self.reg.hide()
            self.address.show()
        else: 
            self.reg.show()
            self.address.hide()
    def copy(self):
        copy=OutputRow()
        copy.address.setText(self.address.text())
        copy.CorrectAnswer.setText(self.CorrectAnswer.text())
        copy.reg.setText(self.reg.text())
        copy.type.setCurrentIndex(self.type.currentIndex())
        return copy
    def getSyscall(_,type):
        return { 1 :'Integer'  , 2 :'Float'  , 3 :'Double'  , 4 :'String'  , 11 :'Character', 
                '1':'Integer'  ,'2':'Float'  ,'3':'Double'  ,'4':'String'  ,'11':'Character', 
                    'Integer':1,    'Float':2,    'Double':3,    'String':4,     'Character':11 }[type]
    def getKwargs(self):
        i=self.type.currentText()
        if i=="String": return { 'type':self.getSyscall(i), 'addr':self.address.text(), 'CorrectAnswer':self.CorrectAnswer.text() }
        else:	return { 'type':self.getSyscall(i), 'reg':self.reg.text(), 'CorrectAnswer':self.CorrectAnswer.text() } 
    