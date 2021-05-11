import grader
from MIPS_creator.utilities.settings import settings
import os
from shutil import copyfile
from grader.wrapper import runGrader
from MIPS_creator.ResultsWindow import ResultsWindow
from subprocess import call,PIPE


grader_data_loc = os.path.join(os.path.dirname(__file__), "grader_data/")
grader_file_loc = os.path.join(os.path.dirname(__file__), "grader/")

def transferFile(settingsFile,submissionFile):
    if not os.path.exists(grader_data_loc):
        os.makedirs(grader_data_loc)
    localSettingsFile=grader_data_loc+"settings.json"
    copyfile(settingsFile,localSettingsFile)
    localSubmissionFile=grader_data_loc+"submission.s"
    copyfile(submissionFile,localSubmissionFile)
    runGrader( **{
        'settingsFile':localSettingsFile,
        'submissionFile':localSubmissionFile ,
        'outputFile':grader_data_loc+"output.txt",
        'concatFile':grader_data_loc+"concat.s",
        'autograderOutput':grader_data_loc+"graderResults.txt",
        'ShowAll':False,
        'printResults':False}
    )
w1:ResultsWindow
w2:ResultsWindow
w3:ResultsWindow
w1,w2,w3=None,None,None
def initResults(parent,msg):
    parent.gradeDock.isUsed=True
    parent.gradeDock.setText(msg)
    parent.gradeDock.show()
    parent.gradeDock.raise_()

def showResults(parent):
    
    parent.rawMipsDock.displayFile(grader_data_loc+"output.txt",True)
    parent.concatAsmDock.displayFile(grader_data_loc+"concat.s",True)
    parent.gradeDock.displayFile(grader_data_loc+"graderResults.txt",True)
    parent.rawMipsDock.show()
    parent.gradeDock.show()
    parent.concatAsmDock.show()
    
    os.system("make clean")
    os.system("make UI_clean")

    
    
def CreateTAR(settingsFile, tarDestination,parent):
    destSettingsFile="grader/settings.json"
    copyfile(settingsFile,destSettingsFile)
    os.system("make UI_tar")
    tarPath = grader_data_loc+"UI.tar"
    copyfile(tarPath,tarDestination)
    
    parent.makefileDock.displayFile(grader_data_loc+"Makefile",False)