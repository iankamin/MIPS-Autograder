import os,sys

currentDir=os.path.dirname(__file__)
iconPath = os.path.join(currentDir,"Icons/")
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class ui:
    print(os.listdir(resource_path("ui_files")))
    mainwindow = resource_path( "ui_files/mainwindow.ui")
    resultswindow = resource_path( "ui_files/ResultsWindow.ui")

    RegInput     = resource_path( "ui_files/regInput.ui")
    RegOutput    = resource_path( "ui_files/regOutput.ui")
    DataRow      = resource_path( "ui_files/DataRow.ui")
    TopRow       = resource_path( "ui_files/TopRow.ui")
    UserInputRow = resource_path( "ui_files/UserInputRow.ui")


class Icons:
    add     = resource_path( "ui_files/Icons/add.png")
    add2    = resource_path( "ui_files/Icons/add2.png")
    remove  = resource_path( "ui_files/Icons/remove.png")
    remove2 = resource_path( "ui_files/Icons/remove2.png")
    upArrow    = resource_path( "ui_files/Icons/up_arrow.png")
    downArrow    = resource_path( "ui_files/Icons/down_arrow.png")
    leftArrow    = resource_path( "ui_files/Icons/left_arrow.png")
    rightArrow    = resource_path( "ui_files/Icons/right_arrow.png")
    checkmark    = resource_path( "ui_files/Icons/checkmark.png")
    white    = resource_path( "ui_files/Icons/white.png")