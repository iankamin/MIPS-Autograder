# This Python file uses the following encoding: utf-8
import sys,os
from PyQt5 import  QtGui, QtWidgets
from Frontend import Test,MainWindow
from Frontend.RowTypes import DataRow, OutputRow, RegisterRow, UserInputRow
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

def folderGenerate(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

if __name__ == '__main__':
    folderGenerate("Frontend")

    app = QtWidgets.QApplication(sys.argv)
    font=app.font()
    font.setPointSize(12)
    app.setFont(font)
    main = MainWindow()
    print(main.geometry())
    main.showMaximized()
    sys.exit(app.exec_())
