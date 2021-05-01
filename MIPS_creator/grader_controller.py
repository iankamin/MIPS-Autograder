from MIPS_creator.utilities.settings import settings
import os
from shutil import copyfile
from grader.wrapper import runGrader
from MIPS_creator.ResultsWindow import ResultsWindow

grader_data_loc = os.path.join(os.path.dirname(__file__), "grader_data/")

def transferFile(settingsFile,submissionFile):
    if not os.path.exists(grader_data_loc):
        os.makedirs(grader_data_loc)
    localSettingsFile=grader_data_loc+"settings.json"
    print("HHHHHH")
    print (localSettingsFile)
    print (settingsFile)
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
def showResults(parent):
    w1=ResultsWindow("Raw MIPS Output",parent)
    w1.displayFile(grader_data_loc+"output.txt",True)
    w1.show()
    w2=ResultsWindow("Concatenated MIPS File",parent)
    w2.displayFile(grader_data_loc+"concat.s",True)
    w2.show()
    w2=ResultsWindow("Autograder Results",parent)
    w2.displayFile(grader_data_loc+"graderResults.txt",True)
    w2.show()

