from PyQt5 import QtWidgets,uic

class TestTopRow(QtWidgets.QWidget):
    def __init__(self): 
       super(QtWidgets.QWidget, self).__init__()
       uic.loadUi('TestLayoutTopRow.ui', self)

class UserInputRow(QtWidgets.QWidget):
    def __init__(self): 
       super(QtWidgets.QWidget, self).__init__()
       uic.loadUi('UserInputRow.ui', self)