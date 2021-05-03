# This Python file uses the following encoding: utf-8
import sys,os
from PyQt5 import  QtGui, QtWidgets
from MIPS_creator import *
from MIPS_creator.RowTypes import DataRow, OutputRow, RegisterRow, UserInputRow
from MIPS_creator.grader_controller import transferFile
def createTest(main,a,b,c,d):
    test:Test
    test=main.addTest()
    test.HidingBox.on_pressed()
    test.allUserInput.on_pressed()
    test.InputRegisters.on_pressed()
    test.DataInput.on_pressed()
    test.Outputs.on_pressed()
    for _ in range(a): test.addRow(UserInputRow)
    for _ in range(b): test.addRow(DataRow)
    for _ in range(c): test.addRow(RegisterRow)
    for _ in range(d): test.addRow(OutputRow)

if __name__ == '__main__':
    #os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    #createTest(main,1,1,1,1)
    #createTest(main,2,2,2,2)
    ##createTest(main,3,1,2,5)
    ##createTest(main,5,4,2,1)
    ##input("clicktoDelete")
    ##main.DeleteAllTests()
    ##createTest(main,3,3,3,3)

    sys.exit(app.exec_())
