from subprocess import run
import sys,os
import Autograder


def runGrader(settingsFile="settings.json",submissionFile="submission.s",
              outputFile="output.txt",concatFile="concat.s",autograderOutput="graderResults.txt",
              ShowAll=False,printResults=True):
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test
    _ShowAll=_ShowAll or ShowAll

    io=Autograder.settings(settingsFile)

    runMips=Autograder.concat(IO=io,sfile=submissionFile,concatFile=concatFile)
    Autograder.autograder(IO=io,_ShowAll=_ShowAll, runMips=runMips,outputDest=outputFile, concatFile=concatFile,
    autograderOutput=autograderOutput,printResults=printResults)


if __name__ == "__main__":
    
    
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    runGrader()