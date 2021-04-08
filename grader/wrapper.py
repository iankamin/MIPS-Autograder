from subprocess import run
import sys,os
os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
from settings import settings
from autograder import autograder
from concat import concat



def main():
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test
    
    io=settings("settings.json")

    runMips=concat(IO=io,sfile="submission.s")
    autograder(IO=io,_ShowAll=_ShowAll, runMips=runMips)

main()