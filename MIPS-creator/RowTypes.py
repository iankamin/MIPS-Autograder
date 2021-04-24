from abc import abstractmethod
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
	
	@abstractmethod
	def getKwargs(self):
			return

class TestTopRow(QtWidgets.QWidget):
	TestName:QtWidgets.QLineEdit
	ShowLevel:QtWidgets.QComboBox
	MaxPoints:QtWidgets.QDoubleSpinBox
	ExtraCredit:QtWidgets.QCheckBox
	CopyButton:QtWidgets.QPushButton
	DeleteButton:QtWidgets.QPushButton
	def __init__(self): 
	   super(QtWidgets.QWidget, self).__init__()
	   uic.loadUi('ui_files/TopRow.ui', self)
	   self.ShowLevel.wheelEvent = self.scrollWheelEvent
	
	# Prevents the scroll wheel from affecting combobox
	def scrollWheelEvent(self, *args, **kwargs):
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
		sa=False
		so=False
		i = self.ShowLevel.currentIndex
		if i == 1:so=True
		if i == 2:sa=True
	
		return {
			'show':sa       ,
			'showOutput':so,
			'testName':self.TestName.text() or "Test"  ,
			'ExtraCredit':self.ExtraCredit.isChecked(),
			'OutOf':self.MaxPoints.value() 
			}
		



class UserInputRow(Row):
	DeleteButton:QtWidgets.QPushButton
	UserInput:QtWidgets.QLineEdit
	def __init__(self,parent=None): 
		super().__init__()
		uic.loadUi('ui_files/UserInputRow.ui', self)
		self.parent=parent
		self.DeleteButton.pressed.connect(self.delete)

	def copy(self):
		copy=UserInputRow()
		copy.UserInput.setText(self.UserInput.text())
		return copy
	
	def getKwargs(self):
			return {"UserInput":self.UserInput.text()}
	
class DataRow(Row):
	DeleteButton:QtWidgets.QPushButton
	address:QtWidgets.QLineEdit
	data:QtWidgets.QLineEdit
	type:QtWidgets.QComboBox
	reg:QtWidgets.QComboBox
	def __init__(self,parent=None): 
		super().__init__()
		uic.loadUi('ui_files/DataRow.ui', self)
		self.parent=parent
		self.DeleteButton.pressed.connect(self.delete)
	
	def copy(self):
		copy=DataRow()
		copy.address.setText(self.address.text())
		copy.data.setText(self.data.text())
		copy.type.setCurrentIndex(self.type.currentIndex())
		copy.reg.setCurrentIndex(self.reg.currentIndex())
		return copy
	def getKwargs(self):
		reg=self.reg.currentIndex()
		if reg == 0: reg=None
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
	def __init__(self,parent=None): 
		super().__init__()
		uic.loadUi('ui_files/regInput.ui', self)
		self.parent=parent
		self.DeleteButton.pressed.connect(self.delete)
	
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

class OutputRow(Row):
	DeleteButton:QtWidgets.QPushButton
	reg:QtWidgets.QLineEdit
	type:QtWidgets.QComboBox
	address:QtWidgets.QLineEdit
	CorrectAnswer:QtWidgets.QLineEdit
	def __init__(self,parent=None): 
		super().__init__()
		uic.loadUi('ui_files/regOutput.ui', self)
		self.parent=parent
		self.DeleteButton.pressed.connect(self.delete)
		self.address.hide()
		
		self.type:QtWidgets.QComboBox
		self.type.currentTextChanged.connect(self.ComboBoxChanged)
	
	def ComboBoxChanged(self,i):
		print(i)
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
	def getSyscall(_,inst):
		return { 'Integer':1, 'Float':2, 'Double':3, 'String':4, 'Character':11
		}[inst]

	def getKwargs(self):
		i=self.type.currentText()
		if i=="String":
   			return {
				'type':self.getSyscall(i),
				'addr':self.address.text(),
				'CorrectAnswer':self.CorrectAnswer.text()
				}
		else:	
			return {
				'type':self.getSyscall(i),
				'reg':self.reg.text(),
				'CorrectAnswer':self.CorrectAnswer.text()
				}
		
	