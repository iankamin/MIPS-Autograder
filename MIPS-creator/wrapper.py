# This Python file uses the following encoding: utf-8
import sys,os
from PyQt5 import  QtGui, QtWidgets
from TestLayout import Test
from mainwindow import MainWindow

def createTest(main):
	test:Test
	test=main.addTest()
	test.HidingBox.on_pressed()
	test.allUserInput.on_pressed()
	test.InputRegisters.on_pressed()
	test.DataInput.on_pressed()
	test.Outputs.on_pressed()
	test.addUserInputRow()
	test.addUserInputRow()
	test.addDataRow()
	test.addDataRow()
	test.addRegisterRow()
	test.addRegisterRow()
	test.addOutputRow()
	test.addOutputRow()

if __name__ == '__main__':
	os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()

	main.show()
	createTest(main)

	sys.exit(app.exec_())
