from subprocess import run
import sys,os



def main():
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test
    
    io=settings("settings.json")

    runMips=concat(IO=io,sfile="submission.s")
    autograder(IO=io,_ShowAll=_ShowAll, runMips=runMips)


if __name__ == "__main__":
    from settings import settings
    from autograder import autograder
    from concat import concat
    
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    main()