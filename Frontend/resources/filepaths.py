import os,sys

try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.dirname(__file__)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    return os.path.join(base_path, relative_path)

class ui:
    print(os.listdir(resource_path(".")))
    mainwindow = resource_path( "mainwindow.ui")
    resultswindow = resource_path( "ResultsWindow.ui")

    RegInput     = resource_path( "regInput.ui")
    RegOutput    = resource_path( "regOutput.ui")
    DataRow      = resource_path( "DataRow.ui")
    TopRow       = resource_path( "TopRow.ui")
    UserInputRow = resource_path( "UserInputRow.ui")


class Icons:
    iconPath = "Icons/"
    add     = resource_path( iconPath+"add.png")
    add2    = resource_path( iconPath+"add2.png")
    remove  = resource_path( iconPath+"remove.png")
    remove2 = resource_path( iconPath+"remove2.png")
    upArrow    = resource_path( iconPath+"up_arrow.png")
    downArrow    = resource_path( iconPath+"down_arrow.png")
    leftArrow    = resource_path( iconPath+"left_arrow.png")
    rightArrow    = resource_path( iconPath+"right_arrow.png")
    checkmark    = resource_path( iconPath+"checkmark.png")
    white    = resource_path( iconPath+"white.png")
    copy    = resource_path( iconPath+"copy.png")
    delete    = resource_path( iconPath+"delete.png")