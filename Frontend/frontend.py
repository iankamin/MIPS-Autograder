import os
import sys
from tkinter import *
from typing import List

os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory

sys.path.insert(1, '../grader' )
from settings import settings
os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory

def LoadCallBack():
    None

def SaveCallBack():
    None

def RunCallBack():
    None



def main():
    global BareMode,ShowAll,UserInput,testPTS,ECtestPTS,promptPTS,MessageToStudents
    io = settings("settings.json")
    windo=Tk() 
    windo.title('Helo Python')
    windo.geometry("1600x800")
    window=Frame(windo, bg='Gray',height=1080,width=1920)
    window.pack(fill=BOTH)
    window.rowconfigure(3, minsize=400)
    window.columnconfigure(4, minsize=200)


    TopLeft(window)
    BottomLeft(window)
    windo.mainloop()


def TopLeft(window):
    global BareMode,ShowAll,UserInput,testPTS,ECtestPTS,promptPTS,MessageToStudents
    TL = Frame(window, bg="red", borderwidth=20)
    Button(TL,width=17, text ="Run Assembly File", command = RunCallBack).grid(row= 0, column=0, sticky="NW",pady=5, padx=5)
    Entry(TL,width=20).grid(row=1,column=0,sticky="NW",pady=5,padx=5)
    Button(TL,width=10, text ="Load Settings", command = LoadCallBack).grid(row= 0, column=1, sticky="NW",pady=5, padx=5)
    Button(TL,width=10, text ="Save Settings", command = SaveCallBack).grid(row=1,column=1,sticky="NW",pady=5,padx=5)
    TL.grid(row = 0, column = 0, sticky=E+W+N+S)
    


def BottomLeft(window):
    global BareMode,ShowAll,UserInput,testPTS,ECtestPTS,promptPTS,MessageToStudents
    BareMode = BooleanVar()
    ShowAll = BooleanVar()
    UserInput = BooleanVar()
    testPTS = IntVar()
    ECtestPTS = IntVar()
    promptPTS = IntVar()
    MessageToStudents = StringVar()
    SubroutineName = StringVar()
    
    bg='lightgray'
    BL = Frame(window ,bg=bg, borderwidth=20, bd=30)
    BL.grid(row = 1, column = 0, rowspan=2,sticky=NSEW)
    
    e=Frame(BL,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Label(e,bg=bg, text=" Subroutine Name").pack( side = TOP, anchor=W)
    Entry(e,bg='white', bd =3, textvariable=SubroutineName,justify=LEFT).pack( fill=X)
    

    Checkbutton(BL,bg=bg, text = "Bare Mode", height=1, \
                variable = BareMode, onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    Checkbutton(BL,bg=bg, text = "Requires User Input", height=1, \
                variable = UserInput, onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    Checkbutton(BL,bg=bg, text = "Show All Results", height=1, \
                variable = ShowAll,  onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    
    
    e=Frame(BL,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd =3, textvariable=testPTS, width=4, justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Test Points" ).pack( side = LEFT)
    
    e=Frame(BL,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd =3, textvariable=ECtestPTS,width=4,justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Prompt Points").pack( side = LEFT)
    
    e=Frame(BL,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd =3, textvariable=ECtestPTS,width=4,justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Extra Credit Points").pack( side = LEFT)
    
    e=Frame(BL,bg=bg)
    e.pack(side=TOP, pady=5)
    MessageToStudents=Text(e,bg='white', bd=3, width=30, height=19).pack( side = BOTTOM, fill=BOTH)
    Label(e,bg=bg, text="General Message").pack( side = LEFT)

main()