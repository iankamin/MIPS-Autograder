import json
import os
import sys
import subprocess
import re
from settings import settings


#os.chdir(os.getcwd()+"/"+os.path.dirname(sys.argv[0])) # ensures proper initial directory



def generateInput():
    global io
    
    lines=list(io.getAllUserInputLines())
    if len(lines)>0: 
        with open('input.txt', 'w') as inp:  
            inp.writelines('\n'.join(lines))
        return " < input.txt "
    
    return ""

def mips():
    global io
    subprocess.call("echo \"\" > output.txt", shell=True)
    subprocess.call("echo \"\" > error.txt", shell=True)
    
    userInput = generateInput()
    
    if io.BareMode: BM = "-bare "
    else: BM = ""

    try: 
        subprocess.call("spim %s -file concat.s %s >> output.txt 2>> error.txt"%(BM,userInput),shell=True,timeout=3)
    except subprocess.TimeoutExpired: 
        return '    Your Program Timed Out due to an infinite loop in MIPS'
    except: 
        return "    UH-OH your program failed to run for an unknown reason"
    return ""
    
def GetMipsOutput():
    NoneAsciiMSG=""
    try:
        with open('output.txt',mode='r' ) as f: output=f.read()
    except:
        with open('output.txt',mode='rb') as f: output=f.read()

        probIndices=reversed([(m.start(0),m.end(0)) for m in re.finditer(bytes('[^\x00-\x7F]+','utf-8'),output)])
        for (s,e) in probIndices:
            asc=hex(int.from_bytes(output[s:e],"big"))
            output=output[:s]+bytes('<NON ASCII DATA>( %s )'%asc,'utf-8')+output[e:]

        NoneAsciiMSG = "non ascii characters were printed"
        #output=re.sub(bytes('[^\x00-\x7F]+','utf-8'),bytes('<NON ASCII DATA>','utf-8'), output)
        output=output.decode('utf-8','replace')
        with open('output2.txt',mode='w') as f: f.write(output)
    output = output.split('\nXXFFVV3793\n')

    output=[o.strip() for o in output]
    
    header_error=output.pop(0)
    header_error=header_error.split('\n',6)     # a JAL instruction is missing a corresponding label
    header_error=header_error[6].strip() if len(header_error)>=6 else ""
    
    return output,header_error,NoneAsciiMSG

def PrintMipsError(headerErr, lastOutput, SPIMerror, NonAsciiMSG,completionErr,runMips):
    print("\nthe following errors occurred")
    print("=============================")
    allErrors=""
    # errors/Warnings that occurred while concatenating the submission
    with open('concatErrors.txt', 'r') as f:  
        concatErr = f.read().strip()
    if len(concatErr)>0: 
        allErrors+=concatErr+"\n\n"

    # States that the program terminated early
    if len(completionErr)>0: 
        allErrors+=completionErr+"\n\n"

    # SPIM was force quit due to infinite loop
    if len(SPIMerror)>0: 
        allErrors+=SPIMerror+"\n\n" 

    # problem occurred while reading output such as non ascii data
    if len(NonAsciiMSG)>0: 
        allErrors+=NonAsciiMSG+"\n\n"

    # prints out the MIPS HEADER section excluding The emulator header - will be empty if ran successfully
    if len(headerErr)>0: 
        allErrors+=headerErr.strip()+"\n\n"
    
    # Any errors generated by while running mips program such as syntax errors etc
    if(runMips):
        with open('error.txt', 'r') as f:  
            MIPSerr = f.read().strip()
    else: MIPSerr = "program was never run due to potential illegal syscalls"
    if len(MIPSerr)>0:  allErrors += "runtime error:\n   %s\n"%MIPSerr
    if ("Attempt to execute non-instruction" in MIPSerr):
        allErrors += "   ^^^ Your subroutine must terminate with a JUMP RETURN\n\n"
    elif len(MIPSerr)>0: allErrors+='\n'

    # prints out the last section of mips output will be empty if ran successfully
    if len(lastOutput)>0: allErrors+=lastOutput.strip() + "\n\n" 
    
    if len(allErrors)>0: print(allErrors.strip())
    else: print("    None")
    print("=============================\n")

def autograder(IO = None, _ShowAll=False, runMips=True):
    global ShowAll, io
    if IO == None: io =settings("settings.json")
    else : io=IO
    ShowAll = _ShowAll or io.ShowAll
    tests = io.AllTests
    
    io.printHeader()

    if runMips: 
        SPIMerror = mips()
        output, header_error, NoneAsciiMSG = GetMipsOutput()
        completionErr="Program Terminated Early without running all tests" if len(io.AllTests)*3 > len(output) else ""
    
        try: lastOutput=output[-1].strip()
        except: lastOutput=""
        PrintMipsError( header_error, lastOutput, SPIMerror, NoneAsciiMSG, completionErr, runMips)
    else:
        PrintMipsError( "", "", "", "", "", runMips)
        output = []
    
    TotalNumTests=len(io.AllTests)
    promptPoints = [0 for _ in range(TotalNumTests)]
    testPoints = [0 for _ in range(TotalNumTests)]
    EC_Points = [0 for _ in range(TotalNumTests)]

    prevFilelines=[]
    for testNum in range(TotalNumTests):
        test=io.AllTests[testNum]
        expectedAns=test.ExpectedAnswers
        
        StudentOutput,StudentPrompt= getStudentPromptAndOutputPerTest(output,testNum)

        if len(test.filelines)>0:
            filelines=test.filelines
            [prevFilelines.append(f) for f in filelines]
            prevFilelines.sort(key=len)
            prevFilelines.reverse()
        else: filelines=[]

    # check if test it extra credit

        EC_Points[testNum] = test.ExtraCredit

        if io.PromptGrade > 0: ShowDetails(testNum+1,test,StudentOutput,StudentPrompt)
        else:                  ShowDetails(testNum+1,test,StudentOutput,None)

    # grades student prompt
        if io.PromptGrade > 0:
            for line in prevFilelines: StudentPrompt = StudentPrompt.replace(line,"")    # removes user input if they decided to print it out
            if ("<NON ASCII DATA>" in StudentPrompt): 
                print("\nNon-Ascii characters were found in your prompt credit cannot be given ")
            elif ("<NO PROMPT FOUND>") in StudentPrompt:
                None
            else:
                if len(StudentPrompt.strip())>3: promptPoints[testNum]=1

        numOfrequiredAns=len(expectedAns)
        for i,line in enumerate(StudentOutput):
            try:    ea=expectedAns[i]
            except: ea="garbage_sdakfjlkasdjlfk" #if student Output is longer than actual output the current expected answer doesnt exist

            if line == ea:
                testPoints[testNum] += test.OutOf / numOfrequiredAns
                expectedAns[i]="garbage_sdakfjlkasdjlfk"    #ensures students cant get credit if they print the same answer musltiple times
            
            elif line in expectedAns:   #if they swapped the registers they get partial credit
                testPoints[testNum] += (.5*test.OutOf) / numOfrequiredAns
                ind = expectedAns.index(line)
                expectedAns[ind]="garbage_sdakfjlkasdjlfk"
        
        temp=testPoints[testNum]
        if test.ExtraCredit and ( testPoints[testNum] < test.OutOf ):
                print("\nExtra Credit must work fully to receive credit\noriginal score ",end='')
                temp=0

        print(" - %.3f out of %s"%(testPoints[testNum],test.OutOf))
        print("............................................")
        testPoints[testNum]=temp

    scores={}

    #scores["total"] = sum(testPoints)
    if io.PromptGrade > 0:
        scores["PromptPrinted"] = (io.PromptGrade * sum(promptPoints)) / TotalNumTests
        #scores["total"] += scores["PromptPrinted"]
        print("Prompt - %.3f out of %s"%( scores["PromptPrinted"], io.PromptGrade ))
    
    for i in range(1,TotalNumTests+1):
        scores["test%i"%i]=testPoints[i-1]
    
    JSONscores= {'scores':scores}

    print('\n\n======== RESULTS ========\n')
    print(json.dumps(JSONscores))
    return


def getStudentPromptAndOutputPerTest(output,testNum):
# Split and clean MIPS results
    try: StudentPrompt=output[testNum*3].strip()
    except: StudentPrompt = "<NO PROMPT FOUND>"
    try: StudentOutput=output[(testNum*3)+1]
    except: StudentOutput = "<NO OUTPUT FOUND>"
    
    StudentPrompt=StudentPrompt.replace('\n','\n   ')
    while '\n\n' in StudentOutput: StudentOutput = StudentOutput.replace('\n\n','\n')
    StudentOutput = [r.strip() for r in StudentOutput.split('\n')]
    return StudentOutput,StudentPrompt


        

overridePrompt="The following is the result of every test"
def ShowDetails(testNum,test,StudentOutput,StudentPrompt=None):
    global overridePrompt,ShowAll,io
    print("TEST %i "%(testNum), end='')
    if test.ExtraCredit: print( '(Extra Credit) ', end='')
    
    if not ShowAll: # Checks ShowAll
        if not test.show: 
            if test.showOutput:
                print("(Output Only)")
                printOutput(test,StudentOutput, False)
                print("TEST %i "%(testNum), end='')
            return
        else: print("\nSample Output\n==============")
    else:
        print(overridePrompt)
        overridePrompt=""
        print("=========== test%i =========="%testNum)

    PrintMemInputs(test)
    PrintRegInputs(test)
    PrintStudentPrompt(StudentPrompt)
    printUserInput(test)
    printOutput(test,StudentOutput, True)

    print("TEST %i"%(testNum), end='')


def PrintMemInputs(test):    
    if len(test.MemInputs)>0: 
        print("\nInitial Data in Memory -->")   
    for inp in test.MemInputs:
        print("   addr(%s) =  %s \"%s\""%(inp.addr,inp.type,inp.data))

def PrintRegInputs(test):
    if len(test.RegInputs): 
        print("\nRegister Input Values -->")   
    for inp in test.RegInputs:
        val = GetHexAndDecOrString(inp.value)
        print("   reg: %s = %s"%(inp.reg,val))

def PrintStudentPrompt(StudentPrompt):
    if StudentPrompt != None:
        print("\nYour Prompt -->")
        if len(StudentPrompt.strip())<2: print("   <NO PROMPT WAS FOUND>")
        else: 
            print("   %s"%StudentPrompt)

def printUserInput(test):
    fl = test.filelines
    if len(fl)>0: print("\nUser Input -->")   
    for line in fl:
        print("   %s"%line)

def printOutput(test,StudentOutput, _printHeader):    
    if _printHeader: print("\nOutput -->")
    for i, Eoutput in enumerate(test.Output):
        if Eoutput.addr is None:
            ExAns = GetHexAndDecOrString(test.ExpectedAnswers[i], int(Eoutput.type))
            print(" Expected   %s = %s"%(Eoutput.reg,ExAns))
            try:
                studentAns = GetHexAndDecOrString(StudentOutput[i],int(Eoutput.type))
                print("   Actual   %s = %s\n"%(Eoutput.reg,studentAns))

            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    print("   <FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT>")
                    print(StudentOutput[i])
                except: 
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        print("   Actual   %s = %s\n"%(Eoutput.reg,studentAns))
                    else:
                        print(StudentOutput)
            continue
        else: 
            print(" Expected   %s at address %s"%(test.ExpectedAnswers[i],Eoutput.addr))
            try:
                r=StudentOutput[i]
                if len(r.strip())==0:
                    r = "NO STRING WAS FOUND" 
                print("   Actual   %s at address %s\n"%(r,Eoutput.addr))
            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    print("   FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT")
                    print(StudentOutput[i])
                except: 
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        print("   Actual   %s at address %s\n"%(r,Eoutput.addr))
                    else:
                        print(StudentOutput)
            continue

def Is_int(s):
    try:
        int(s)
        return True
    except: return False

def to_hex(val, nbits=32):
    val=int(val)
    return hex((val + (1 << nbits)) % (1 << nbits))

def GetHexAndDecOrString(s, type=0):
    s=s.strip()
    if type == 11 and len(s)==1:  return " %s ( \'%s\' )"%(to_hex(ord(s)),s)

    if Is_int(s): return "%s ( %s )"%(s, to_hex(s))
    
    if s[0:1] == '0x': return "%s ( %i )"%(int(s[2:],16), s)
    
    return s


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=False # overrides json "show" and shows the StudentOutputs of every test

    autograder(_ShowAll=_ShowAll)