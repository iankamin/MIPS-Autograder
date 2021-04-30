from MIPS_creator.utilities.settings import settings
import os
from shutil import copyfile
from grader.wrapper import runGrader

def transferFile(settingsFile,submissionFile):
    grader_data_loc = os.path.join(os.path.dirname(__file__), "grader_data/")
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

