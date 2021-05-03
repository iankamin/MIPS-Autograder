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
allWs=[]
def showResults(parent):
    for w in allWs: w.close()
    
    w1=ResultsWindow("Raw MIPS Output",parent)
    w1.displayFile(grader_data_loc+"output.txt",True)
    w1.setMaximumWidth(w1.width()*2/3)
    w1.move(0,0)
    w2=ResultsWindow("Concatenated MIPS File",parent)
    w2.displayFile(grader_data_loc+"concat.s",True)
    w2.move(w1.width(),0)
    w3=ResultsWindow("Autograder Results",parent)
    w3.displayFile(grader_data_loc+"graderResults.txt",True)
    w3.move(w1.width()+w2.width(),0)
    
    w1.show()
    w2.show()
    w3.show()
    allWs.append(w1)
    allWs.append(w2)
    allWs.append(w3)
    os.system("make clean")
    os.system("make UI_clean")

    
    
makeW=None
def CreateTAR(settingsFile, tarDestination,parent):
    makeW.close()
    destSettingsFile="grader/settings.json"
    copyfile(settingsFile,destSettingsFile)
    os.system("make UI_tar")
    tarPath = grader_data_loc+"UI.tar"
    copyfile(tarPath,tarDestination)
    
    makeW=ResultsWindow("Autograder Makefile",parent)
    makeW.displayFile(grader_data_loc+"Makefile",False)
    makeW.move(100,0)
    makeW.show()