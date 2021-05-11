import os

currentDir=os.path.dirname(__file__)
iconPath = os.path.join(currentDir,"Icons/")
class ui:
    mainwindow = os.path.join(currentDir, "mainwindow.ui")
    resultswindow = os.path.join(currentDir, "ResultsWindow.ui")

    RegInput     = os.path.join(currentDir, "regInput.ui")
    RegOutput    = os.path.join(currentDir, "regOutput.ui")
    DataRow      = os.path.join(currentDir, "DataRow.ui")
    TopRow       = os.path.join(currentDir, "TopRow.ui")
    UserInputRow = os.path.join(currentDir, "UserInputRow.ui")


class Icons:
    add     = os.path.join(iconPath, "add.png")
    add2    = os.path.join(iconPath, "add2.png")
    remove  = os.path.join(iconPath, "remove.png")
    remove2 = os.path.join(iconPath, "remove2.png")
    upArrow    = os.path.join(iconPath, "up_arrow.png")
    downArrow    = os.path.join(iconPath, "down_arrow.png")
    leftArrow    = os.path.join(iconPath, "left_arrow.png")
    rightArrow    = os.path.join(iconPath, "right_arrow.png")
    checkmark    = os.path.join(iconPath, "checkmark.png")
    white    = os.path.join(iconPath, "white.png")


