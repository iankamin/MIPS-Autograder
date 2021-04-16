import os
import sys
from tkinter import *
from tkinter import ttk
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

def TarCallBack():
    None


def main():
    global BareMode,ShowAll,UserInput,testPTS,ECtestPTS,promptPTS,MessageToStudents
    io = settings("settings.json")
    window=Tk() 
    window.title('Helo Python')
    window.geometry("1600x800")
    dock=Frame(window, bg='Gray',width=300)
    dock.pack(anchor=W,fill="y",expand=True)

    

    TopDock(dock)
    BottomDock(dock)

    window.mainloop()


def TopDock(dock):
    global BareMode,ShowAll,UserInput,testPTS,ECtestPTS,promptPTS,MessageToStudents
    box = Frame(dock, bg="red", borderwidth=10)

    Button(box,width=10, text ="Load Settings", command = LoadCallBack).grid(row=1, column=0, sticky="W",pady=5, padx=5)
    Button(box,width=10, text ="Save Settings", command = SaveCallBack).grid(row=0,column=0,sticky="W",pady=5,padx=5)
    Button(box,width=14, text ="Run Assembly File", command = RunCallBack).grid(row=0, column=1, sticky="E",pady=5, padx=5)
    Button(box,width=14, text ="Create TAR", command = TarCallBack).grid(row=1, column=1, sticky="E",pady=5, padx=5)
    box.pack(anchor=NW,fill=X)
    


def BottomDock(dock):
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
    
    Bot = ScrollableFrame(dock,bg,W,310)
    
    
    e=Frame(Bot,bg=bg)
    e.pack(side=TOP, fill=X, padx=5)
    Label(e,bg=bg, text=" Subroutine Name").pack( side = TOP, anchor=W)
    Entry(e,bg='white', bd=3, textvariable=SubroutineName,justify=LEFT).pack(fill=X)
    

    Checkbutton(Bot,bg=bg, text = "Bare Mode", \
                variable = BareMode, onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    Checkbutton(Bot,bg=bg, text = "Requires User Input",  \
                variable = UserInput, onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    Checkbutton(Bot,bg=bg, text = "Show All Results", \
                variable = ShowAll,  onvalue = True, offvalue = False ).pack(side=TOP,anchor=W, pady=5)
    
    
    e=Frame(Bot,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd=3, textvariable=testPTS, width=4, justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Test Points" ).pack( side = LEFT)
    
    e=Frame(Bot,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd=3, textvariable=ECtestPTS,width=4,justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Prompt Points").pack( side = LEFT)
    
    e=Frame(Bot,bg=bg)
    e.pack(side=TOP, fill=X, pady=5)
    Entry(e,bg='white', bd=3, textvariable=ECtestPTS,width=4,justify=CENTER).pack( side = LEFT, padx=6)
    Label(e,bg=bg, text=" Extra Credit Points").pack( side = LEFT)
    
    e=Frame(Bot,bg=bg)
    e.pack(side=TOP, pady=5,padx=5)
    MessageToStudents=Text(e,bg='white', bd=3, width=36,height=20).pack( side = BOTTOM, fill=BOTH)
    Label(e,bg=bg, text="General Message").pack( side = LEFT)


def ScrollableFrame(dock, bg, anchor,canvas_width=0):
    container = Frame(dock,bg=bg,pady=3)
    canvas = Canvas(container,bg=bg,width=canvas_width)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview,width=20)
    scrollable_frame = Frame(canvas,bg=bg)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    container.pack(anchor=anchor,fill="y",expand=True)
    canvas.pack(side="left", fill="y", expand=True)
    scrollbar.pack(side="right", fill="y")
    if canvas_width!=0: canvas.pack_propagate(False)

    return scrollable_frame

class Test:
    def __init__(self):
        pass

    def draw(self):
        pass


main()