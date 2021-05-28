from PyQt5.QtCore import QObject, pyqtSignal
import Autograder
from Frontend.utilities.settings import settings
import os,sys
from shutil import copyfile
from Autograder import runGrader
from Frontend.ResultsWindow import ResultsWindow
from subprocess import call,PIPE


def filepath(dir):
    try: path = os.path.join(sys._MEIPASS,dir)
    except Exception: path = os.path.join(os.path.dirname(__file__),dir)
    return path
grader_data_loc = filepath("grader_data/")
grader_file_loc = filepath("grader/")
    
class MipsWorker(QObject):
    finished=pyqtSignal()
    def __init__(self,settingsFile,submissionFile) :
        super().__init__()
        self.settingsFile=settingsFile
        self.submissionFile=submissionFile
    
    def run(self):
        if not os.path.exists(grader_data_loc):
            os.makedirs(grader_data_loc)
        localSettingsFile=grader_data_loc+"settings.json"
        copyfile(self.settingsFile,localSettingsFile)
        localSubmissionFile=grader_data_loc+"submission.s"
        copyfile(self.submissionFile,localSubmissionFile)
        runGrader( **{
            'settingsFile':localSettingsFile,
            'submissionFile':localSubmissionFile ,
            'outputFile':grader_data_loc+"output.txt",
            'concatFile':grader_data_loc+"concat.s",
            'autograderOutput':grader_data_loc+"graderResults.txt",
            'ShowAll':False,
            'printResults':False})
        self.finished.emit()


w1:ResultsWindow
w2:ResultsWindow
w3:ResultsWindow
w1,w2,w3=None,None,None
def errorDisplay(parent,msg):
    errorDock=parent.errorDock
    errorDock:ResultsWindow
    errorDock.isUsed=True
    errorDock.setText(msg)
    errorDock.setMinimumWidth(500)
    errorDock.lineNum.hide()
    errorDock.show()
    errorDock.raise_()

    for dock in parent.docks:
        if dock is parent.errorDock: continue
        dock.close()

def outputDisplay(parent):
    parent.errorDock.close()
    parent.rawMipsDock.displayFile(grader_data_loc+"output.txt",True)
    parent.concatAsmDock.displayFile(grader_data_loc+"concat.s",True)
    parent.gradeDock.displayFile(grader_data_loc+"graderResults.txt",True)
    parent.gradeDock.setMinimumWidth(500)
    parent.rawMipsDock.show()
    parent.gradeDock.show()
    parent.concatAsmDock.show()
    
    MakeClean()
    #os.system("make UI_clean")
    
def CreateTAR(settingsFile, tarDestination,parent):
    MakeClean()
    try: base_path = sys._MEIPASS+"/Autograder"
    except Exception: base_path = os.path.dirname(__file__)+'/../Autograder'
    destSettingsFile=base_path+"/settings.json"
    print(settingsFile)
    copyfile(src=settingsFile,dst=destSettingsFile)
    #os.system("make UI_tar")
    make_tarfile(tarDestination, base_path)
    deleteFile(destSettingsFile)
    deleteFile(settingsFile)
#    tarPath = grader_data_loc+"UI.tar"
#    copyfile(tarPath,tarDestination)
    
    parent.makefileDock.displayFile(grader_data_loc+"Makefile",False)

def MakeClean():
    try: base_path = sys._MEIPASS+"/Autograder/"
    except Exception: base_path = os.path.dirname(__file__)+'/../Autograder/'
 
    deleteFile(base_path+"error.txt")
    deleteFile(base_path+"concatErrors.txt")
    deleteFile(base_path+"input.txt")
    deleteFile(base_path+"output.txt")
    deleteFile(base_path+"submission.s")
    deleteFile(base_path+"concat.s")
    deleteFile(base_path+"skeleton.s")
    deleteFile(base_path+"grader_data/UI.tar")
    deleteFile(grader_data_loc+"output.txt")
    deleteFile(grader_data_loc+"concat.s")
    deleteFile(grader_data_loc+"graderResults.txt")
    deleteFile(grader_data_loc+"submission.s")
    deleteFile(grader_data_loc+"settings.json")

def deleteFile(_filepath):
    if os.path.exists(_filepath): os.remove(_filepath)

import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
