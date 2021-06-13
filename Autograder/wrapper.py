from subprocess import run
import sys,os
try: from .concat import concat
except: from concat import concat
try: from .settings import settings,Test,Show
except: from settings import settings,Test,Show
try: from .autograder import autograder
except: from autograder import autograder



def runGrader(
    settingsFile="settings.json",
    submissionFile="submission.s",
    outputFile="output.txt",
    concatFile="concat.s",
    autograderOutput="graderResults.txt",
    ShowAll=False,  
    printResults=True,
    IO=None):
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test
    _ShowAll=_ShowAll or ShowAll

    if IO is None: io=settings(settingsFile)
    else: io=IO

    runMips=concat(
        IO=io,
        sfile=submissionFile,
        concatFile=concatFile)
    autograder(
        IO=io,
        _ShowAll=_ShowAll,
        runMips=runMips,
        outputDest=outputFile, 
        concatFile=concatFile,
        autograderOutput=autograderOutput,
        printResults=printResults)


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    runGrader()