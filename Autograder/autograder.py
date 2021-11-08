import json
import os
import sys
import subprocess
import re
from typing import List
try: from .settings import settings,Test,Show
except: from settings import settings,Test,Show

localDir = os.path.dirname(__file__)+"/"

#os.chdir(os.getcwd()+"/"+os.path.dirname(sys.argv[0])) # ensures proper initial directory
def autograder(IO = None, _ShowAll=False, runMips=True, printResults=True,
               outputDest="output.txt",autograderOutput="graderResults.txt",
               settingsFile="settings.json",concatFile="concat.s"):
    global io,outputFile,autograderResults
    if IO == None: io = settings(settingsFile)
    else : io=IO
    AllTests = io.getTests(canShuffle=True)
    outputFile=outputDest
    autograderResults=open(autograderOutput,'w')
    
    io.printHeader(autograderResults)

    if runMips: 
        SPIMerror = mips(concatFile)
        output, header_error, NoneAsciiMSG = GetMipsOutput()
        completionErr="Program Terminated Early without running all tests" if len(AllTests)*3 > len(output) else ""
    
        try: lastOutput=output[-1].strip()
        except: lastOutput=""
        PrintMipsError( header_error, lastOutput, SPIMerror, NoneAsciiMSG, completionErr, runMips)
    else:
        PrintMipsError( "", "", "", "", "", runMips)
        output = []
    
    TotalNumTests=len(AllTests)
    promptPoints = [0 for _ in range(TotalNumTests)]
    testPoints = [0 for _ in range(TotalNumTests)]
    EC_Points = [0 for _ in range(TotalNumTests)]

    prevUserInput=[]
    for testNum in range(TotalNumTests):
        test=AllTests[testNum]
        expectedAns=test.ExpectedAnswers
        
        StudentOutput,StudentPrompt,StudentPromptWithErrors,ErrorInPrompt = getStudentPromptAndOutputPerTest(output,testNum)

        RegexChecks=test.PromptRegex
        if len(test.UserInput)>0:
            UserInput=test.UserInput
            [prevUserInput.append(f) for f in UserInput]
            prevUserInput.sort(key=len)
            prevUserInput.reverse()
        else: UserInput=[]

        # check if test is extra credit
        EC_Points[testNum] = test.ExtraCredit
        
        numOfrequiredAns=len(expectedAns)
        if io.PromptGrade==0: numOfrequiredAns+=len(RegexChecks)

        # grades student prompt
        regMatches=None
        if io.PromptGrade > 0 or len(RegexChecks)>0:
            #for line in prevUserInput: StudentPrompt = StudentPrompt.replace(line,"")    # removes user input if they decided to print it out
            if ("<NON ASCII DATA>" in StudentPrompt) or ("<NO PROMPT FOUND>" in StudentPrompt):  
                None
            elif io.PromptGrade == 0: 
                promptPoints[testNum],regMatches=GradePrompt(StudentPrompt,RegexChecks)
            dispStudentPrompt=StudentPromptWithErrors
        else :
            dispStudentPrompt=None
        
        if io.PromptGrade == 0: 
            testPoints[testNum]=(promptPoints[testNum]*len(RegexChecks)) * (test.OutOf / numOfrequiredAns)

        ShowDetails(testNum+1,test,StudentOutput,dispStudentPrompt,regMatches,ErrorInPrompt)

        for i,line in enumerate(StudentOutput):
            try:    ea=expectedAns[i]
            except: ea="garbage_sdakfjlkasdjlfk" #if student Output is longer than actual output the current expected answer doesnt exist
            
            if ea[0:2] == "0x": ea=to_int(ea,nbits=32)

            if line == ea:
                testPoints[testNum] += test.OutOf / numOfrequiredAns
                expectedAns[i]="garbage_sdakfjlkasdjlfk"    #ensures students cant get credit if they print the same answer musltiple times
            
            elif line in expectedAns:   #if they swapped the registers they get partial credit
                testPoints[testNum] += (.5*test.OutOf) / numOfrequiredAns
                ind = expectedAns.index(line)
                expectedAns[ind]="garbage_sdakfjlkasdjlfk"
        temp=testPoints[testNum]
        if ErrorInPrompt: temp=temp*io.ErrorPenalty
        if test.ExtraCredit and ( testPoints[testNum] < test.OutOf ) and not ErrorInPrompt:
                autograderResults.write("\nExtra Credit must work fully to receive credit\noriginal score ")
                temp=0

        autograderResults.write(" - %.3f out of %s\n"%(testPoints[testNum],test.OutOf))
        testPoints[testNum]=temp
    
    simpleGrade=True
    scores={}
    Prompt=0
    total=0
    if io.PromptGrade > 0:
        pp=sum(promptPoints)
        if pp>=io.NumberOfRegularTests: Prompt = io.PromptGrade
        else: Prompt = (io.PromptGrade * sum(promptPoints)) / io.NumberOfRegularTests
        autograderResults.write("Prompt - %.3f out of %s\n"%( Prompt, io.PromptGrade ))
    
    if io.JsonStyle==0:
        total=Prompt
    if io.JsonStyle==1 or io.JsonStyle==2:
        if io.PromptGrade > 0:
            scores["Prompt"]=Prompt

    if io.JsonStyle==0 or io.JsonStyle==1:
        total+=sum(testPoints[:io.NumberOfRegularTests])
        scores["Total"]=total
        if len(testPoints[io.NumberOfRegularTests:])>0:
            ectotal=sum(testPoints[io.NumberOfRegularTests:])
            scores["Extra Credit"]=ectotal

    if io.JsonStyle==2:   
        test:Test
        total+=sum(testPoints[:io.NumberOfRegularTests])
        for i in range(0,TotalNumTests):
            test=AllTests[i]
            scores["%i"%(test.testNumber)]=testPoints[i]
    

    autograderResults.write('\n\n======== RESULTS ========\n')
    autograderResults.write("    {grade} out of {total}\n\n\n".format(grade=total,total=io.total))
    JSONscores= {'scores':scores}
    autograderResults.write(json.dumps(JSONscores))

    autograderResults.close()
    if printResults: print(open(autograderResults.name).read())
    return

def GradePrompt(prompt:str,regexArr:List[str]) -> (int):
    if len(regexArr) == 0:    # if there are no Regex Checks than the grade will be based on printing at least 3 characters
        if len(prompt.strip())>3: return 1
        else: return 0,None
    else: 
        return CheckPromptForRegex(prompt,regexArr)

def CheckPromptForRegex(prompt:str,regexArr:List[str]):
    value=1/len(regexArr)
    total=0
    matchPairs=[]

    if prompt == "<NO PROMPT FOUND>":
        for regex in regexArr: matchPairs.append((regex,None))
        return total,matchPairs

    for regex in regexArr:
        i=1+1
        r = re.compile(regex,re.IGNORECASE|re.MULTILINE)
        match=r.search(prompt)
        if match:
            total=total+value
            matchPairs.append((regex,match.group(0).strip()))
        else:
            matchPairs.append((regex,None))
    return total,matchPairs

def getStudentPromptAndOutputPerTest(output,testNum:List[str]):
    # Split and clean MIPS results
    try: StudentPromptRegex=output[testNum*3].strip()
    except: StudentPromptRegex = "<NO PROMPT FOUND>"
    try: StudentOutput=output[(testNum*3)+1]
    except: StudentOutput = "<NO OUTPUT FOUND>"
    
    StudentPromptRegex,StudentPromptWithErrors,hasError=RemoveErrorsFromPrompt(StudentPromptRegex)
    StudentPromptRegex=StudentPromptRegex.replace('\n','\n   ')
    StudentPromptWithErrors=StudentPromptWithErrors.replace('\n','\n   ')
    while '\n\n' in StudentOutput: StudentOutput = StudentOutput.replace('\n\n','\n')
    StudentOutput = [r.strip() for r in StudentOutput.split('\n')]
    return StudentOutput,StudentPromptRegex,StudentPromptWithErrors,hasError

def RemoveErrorsFromPrompt(prompt):
    error=False
    pattern=r"Attempt to execute non-instruction at 0x[0-9abcdefABCDEF]{8}.*"
    prompt = re.sub(pattern, '',prompt)
    pattern=r"Instruction references undefined symbol at 0x[0-9abcdefABCDEF]{8}.*"
    prompt = re.sub(pattern, '',prompt)
    pattern=r"\[0x[0-9abcdefABCDEF]{8}\]\t0x[0-9abcdefABCDEF]{8} [ $,a-zA-Z0-9\t]*\[[a-zA-Z0-9]*\] *;.*$"
    prompt = re.sub(pattern, '',prompt)
    promptDisplay=None
    if len(prompt.strip()) == 0: 
        prompt = "<NO PROMPT FOUND>"
    else:
        pattern=r"(?m)(\s*Exception.*ignored$(\n)?)"
        search = re.search(pattern, prompt)
        if search is not None:
            error=True 
            promptWithError=CleanMipsOutput(prompt,2)[0]
            promptDisplay=promptWithError
            pattern=r"(?m)(\s*Exception.*ignored$(\n)?)"
            prompt = re.sub(pattern, '',prompt)
            
    return prompt.strip(),promptDisplay.strip() if promptDisplay else prompt.strip(),error

def generateInput():
    global io
    if not(io.RequiresUserInput): return ""
    lines=list(io.getAllUserInputLines())

    if len(lines)>0: 
        lines.append("YOU SHOULD NOT BE ABLE TO SEE THIS")
        inputFile = open(localDir + 'input.txt','w')
        inputFile.writelines('\n'.join(lines))
        inputFile.writelines('\n')
        inputFile.close()
        return " < %sinput.txt "%localDir
    
    return ""

def mips(concatFile= "concat.s"):
    global io,outputFile
    if os.path.exists("%serror.txt"%localDir): os.remove("%serror.txt"%localDir)
    if os.path.exists(outputFile): os.remove(outputFile)
    
    try: # PyInstaller creates a temp folder and stores path in _MEIPASS
        SPIM_PATH = os.path.join(sys._MEIPASS,"spim")
    except Exception:
        SPIM_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","spim")
    print(SPIM_PATH)
    command = ""
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin') or sys.platform.startswith('msys'):
        command = os.path.join(SPIM_PATH, "spim.exe")
    else:
        command = 'spim'

    exceptionPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template","exceptions.s")

    userInput = generateInput()
    
    if io.BareMode: BareMode = "-bare "
    else: BareMode = ""
    localError=localDir+'error.txt'
    localOutput=localDir + 'output.txt'
    if concatFile == "concat.s": concatpath=localDir+'concat.s'
    else: concatpath = concatFile
    instruction="{command} {baremode} -exception_file {exceptionPath} -file {concat} >> {output} 2>> {error}".format(
        command=command, baremode=BareMode, exceptionPath=exceptionPath,
        concat=concatpath,    error=localError,
        output=localOutput ) # done for testing purposes
        #userinput=userInput,  output=outputFile )
        #userinput="",  
    
    return RunMipsSubprocess(instruction,localOutput)

def RunMipsSubprocess(instruction,outputFile,sleepTime=0.05):
    """
        Interactively runs the MIPS subprocess. checks for SPIM response after each character.
        TODO: start using modified version of spim emulator. 
              that will print out a message when any READ syscall is used so that the 
              autograder can differentiate read syscalls without needing the student 
              to output to console
        TODO: in output.txt differentiate between Test and section splits
    Args:
        instruction ([str]): [The Terminal command to run SPIM] 
        outputFile ([type]): [The desitination file for the output of the MIPS program]
        sleepTime ([type], optional): [The time to sleep between each character. Defaults to 0.05].

    Returns:
        [str]: [an error message if the program detect an issue with how much user input the program requested] 
    """
    import time
    
    if not io.RequiresUserInput:   
        try:
            subprocess.call(instruction,shell=True,timeout=3)
            return ""
        except subprocess.TimeoutExpired: 
            return '    Your Program Timed Out due to an infinite loop in MIPS\n'
        except:
            return "    UH-OH your program failed for an unknown reason\n"
    
    outmsg=""
    UserInput=io.getUserInputbyTest()
    process = subprocess.Popen(instruction,shell=True,stdin=subprocess.PIPE)
    
    time.sleep(0.2)
    with open(outputFile,'r') as f: processResponse = f.read()
    
    diff = "\n".join(processResponse.split('\n')[7:])
    sleep=.001
    for i,test in enumerate(UserInput):
        if i!=0: diff=""
        for line in test:
            if "XXFFVV3793" in diff:   # This is in case the MIPS code is requesting less user input than the test requires. program will skip any test inputs 
                outmsg += "Test {i} was unable to input all seperate User Inputs before subroutine completion\n".format(i=i)
                break                  #    it will seperate the tests a bit so a student can potentially get more credit for a future test
            
            with open(outputFile,'r') as f:
                lastProcessResponse = f.read()

            for char in line:
                #print(char)
                try:
                    process.stdin.write(char.encode())
                    process.stdin.flush()
                    time.sleep(sleep)
                except:
                    outmsg += "Was unable to write char during Test {i}".format(i=i)
                with open(outputFile,'r') as f:
                    processResponse = f.read()
                diff = processResponse.replace(lastProcessResponse,"")
                if diff != "":
                    outmsg += "An input for Test {i} was cutoff early.\n".format(i=i)
                    break
            lastProcessResponse = processResponse
            if diff == "":
                try:
                    process.stdin.write('\n'.encode())
                    process.stdin.flush()
                    time.sleep(sleep)
                except:
                    outmsg += "Was unable to write newline during test{i}".format(i=i)
                
                with open(outputFile,'r') as f:
                    processResponse = f.read()
                diff = processResponse.replace(lastProcessResponse,"")
        
        if "XXFFVV3793" not in diff: 
            outmsg+="ERROR!!!: Grading Terminated early. During Test {i} subroutine never returned\n".format(i=i)
            break
    try:
        process.stdin.close()
        process.wait(timeout=3) 
    except subprocess.TimeoutExpired: 
        #process.kill()
        process.terminate()
        outmsg+='    Your Program Timed Out due to an infinite loop in MIPS or an extra User Input Request\n'
    except:
        #process.kill()
        process.terminate()
        outmsg+= "    UH-OH your program failed to complete for an unknown reason\n"
    return outmsg
    
def GetMipsOutput():
    global outputFile
    NonAsciiMSG=""
    localOutput=localDir + 'output.txt'
    try:
        with open(localOutput,mode='r' ) as f: output=f.read()
    except:
        with open(localOutput,mode='rb') as f: output=f.read()

        probIndices=reversed([(m.start(0),m.end(0)) for m in re.finditer(bytes('[^\x00-\x7F]+','utf-8'),output)])
        for (s,e) in probIndices:
            asc=hex(int.from_bytes(output[s:e],"big"))
            output=output[:s]+bytes('<NON ASCII DATA>( %s )'%asc,'utf-8')+output[e:]

        NonAsciiMSG = "Non-Ascii Characters Were Printed"
        #output=re.sub(bytes('[^\x00-\x7F]+','utf-8'),bytes('<NON ASCII DATA>','utf-8'), output)
        output=output.decode('utf-8','replace')
        with open(localOutput,mode='w') as f: f.write(output)
    
    output,output_with_message=CleanMipsOutput(output)
    with open(outputFile,mode='w') as f: f.write(output_with_message if output_with_message else output)
    #with open(localDir + 'output.txt',mode='w') as f: f.write(output)
    output=[o.strip() for o in output.split('\nXXFFVV3793\n')]
    
    header=output.pop(0)
    header_error=re.search("Loaded(.|\n)*",header)
    header_error=header_error.group(0)
    header_error=header_error.split('\n',1)
    try: header_error=header_error[1]
    except: header_error=""
    
    return output,header_error,NonAsciiMSG
def CleanMipsOutput(output:str,exceptionCount=10):
    """
        Cleans the output of the MIPS program to remove extraneous information. 
        Current just removes excessive instances of 'Exception occurred and ignored'.
    Args:
        output ([str]): [The output of the MIPS program]
        exceptionCount ([int])(default:10): [The number of times the exception message is allowed to appear in a row]

    Returns:
        [str]: [The cleaned output]
        [str]: [The cleaned output with a message where a crop occurred]
    """
    ect=str(exceptionCount)
    ect1=str(exceptionCount+1)
    cropMessage = "       .......\n       message was cropped to reduce space"
    pattern=r"(?m)((^|\s)\s*Exception.*ignored$(\n)?)"
    exceptionOccurred=re.search(pattern+"{"+ect+"}",output)
    errorFound=exceptionOccurred is not None
    removeExtraExceptions=re.search(pattern+"{"+(ect1)+",}",output)
    output_with_message=output
    while removeExtraExceptions is not None:
        output_with_message=output[0:removeExtraExceptions.span(0)[0]]+exceptionOccurred.group(0)+cropMessage+output[removeExtraExceptions.span(0)[1]:]
        output=output[0:removeExtraExceptions.span(0)[0]]+exceptionOccurred.group(0)+output[removeExtraExceptions.span(0)[1]:]
        exceptionOccurred=re.search(pattern+"{"+ect+"}",output)
        removeExtraExceptions=re.search(pattern+"{"+(ect1)+",}",output)
    if errorFound:
        return output,output_with_message
    else:
        return output,""

def CleanMipsError(errorMsg:str):
    if ("Attempt to execute non-instruction" in errorMsg):
        if 'syntax error' in errorMsg: 
            pattern=r"Attempt to execute non-instruction at 0x[0-9abcdefABCDEF]{8}.*" 
            errorMsg = re.sub(pattern, '',errorMsg)
        else:
            errorMsg += "\n^^^ Your subroutine must terminate with a JUMP RETURN\n\n"
    cropMessage = "\n        .......\n     spim error was cropped to reduce space"
    if len(errorMsg.splitlines())>30:  errorMsg="\n".join(errorMsg.splitlines()[:30])+cropMessage
    return errorMsg

def PrintMipsError(headerErr:str, lastOutput, SPIMerror, NonAsciiMSG,completionErr,runMips):
    autograderResults.write("\nThe Following Errors Occurred\n")
    autograderResults.write("=============================\n")
    allErrors=""
    # errors/Warnings that occurred while concatenating the submission
    with open(localDir + 'concatErrors.txt', 'r') as f:  concatErr = f.read().strip()
    if len(concatErr)>0: allErrors+=concatErr+"\n\n"

    # States that the program terminated early
    if len(completionErr)>0: allErrors+=completionErr+"\n\n"

    # SPIM was force quit due to infinite loop
    if len(SPIMerror)>0: allErrors+=SPIMerror+"\n\n" 

    # problem occurred while reading output such as non ascii data
    if len(NonAsciiMSG)>0: allErrors+=NonAsciiMSG+"\n\n"

    # prints out the MIPS HEADER section excluding the emulator header - will be empty if ran successfully
    if len(headerErr)>0: allErrors+=headerErr.strip()+"\n\n"
    
    # Any errors generated while running mips program such as syntax errors etc
    if(runMips):
        with open(localDir + 'error.txt', 'r') as f:  
            MIPSerr = f.read().strip()
    else: 
        MIPSerr = "program was never run due to issues during setup"
    
    if len(MIPSerr)>0:  
        MIPSerr= CleanMipsError(MIPSerr)
        
        allErrors += "Errors From SPIM:\n    %s\n"%MIPSerr.replace('\n','\n    ')
        allErrors+='\n'

    # prints out the last section of mips output will be empty if ran successfully
    if len(lastOutput)>0: allErrors+=lastOutput.strip() + "\n\n" 

    if len(allErrors)>0: 
        autograderResults.write(allErrors.strip())
    else: 
        autograderResults.write("    None")
    autograderResults.write("\n=============================\n\n")
    
def ShowInput(test):
    PrintMemInputs(test)
    PrintRegInputs(test)
    printUserInput(test)
    print('\n')

def ShowOutput(test,StudentOutput,StudentPrompt,RegexChecks):
    PrintStudentPrompt(StudentPrompt)
    PrintRegexChecks(RegexChecks)
    printOutput(test,StudentOutput, True)

def ShowAll(test,StudentOutput,StudentPrompt,RegexChecks,):
    PrintMemInputs(test)
    PrintRegInputs(test)
    PrintStudentPrompt(StudentPrompt)
    PrintRegexChecks(RegexChecks)
    printUserInput(test)
    printOutput(test,StudentOutput, True)

def ShowDetails(testNum,test:Test,StudentOutput,StudentPrompt=None,RegexChecks=None,ErrorInPrompt=False):
    printHeader="{number}. {name}".format(name=test.testName,number=test.testNumber)
    if test.ExtraCredit:printHeader+='(Extra Credit) '
    
    autograderResults.write("---------------------------------------------------\n%s"%(printHeader))
    if test.getShowLevel()==Show.HIDE: 
        return
    elif test.getShowLevel()==Show.INPUT:
        autograderResults.write("(Input Only)")
        ShowInput(test)
    elif test.getShowLevel()==Show.OUTPUT:
        autograderResults.write("(Output Only)")
        ShowOutput(test,StudentOutput, StudentPrompt,RegexChecks)
    elif test.getShowLevel()==Show.ALL:
        ShowAll(test,StudentOutput,StudentPrompt,RegexChecks)
    if ErrorInPrompt:
        autograderResults.write("\nNOTICE:\n  An Exception occurred during the run.\n  A penalty of {penalty}% has been applied\n".format(penalty=io.ErrorPenalty*100))
        
    autograderResults.write("\n")
    autograderResults.write(printHeader)

def PrintMemInputs(test:Test):    
    if len(test.MemInputs)>0: 
        autograderResults.write("\nInitial Data in Memory -->\n")   
    for inp in test.MemInputs:
        autograderResults.write("   addr(%s) =  %s %s\n"%(inp.addr,inp.type,inp.data))

def PrintRegInputs(test:Test):
    if len(test.RegInputs): autograderResults.write("\nRegister Input Values -->\n")   
    for inp in test.RegInputs:
        val = GetHexAndDecOrString(inp.value)
        autograderResults.write("   reg: %s = %s\n"%(inp.reg,val))

def PrintStudentPrompt(StudentPrompt:str):
    if StudentPrompt != None:
        autograderResults.write("\nYour Prompt -->\n")
        if ("<NON ASCII DATA>" in StudentPrompt):  
            autograderResults.write("Non-Ascii characters were found in your prompt credit cannot be given \n")
        elif len(StudentPrompt.strip())<2: 
            autograderResults.write("   <NO PROMPT WAS FOUND>\n")
        else: 
            autograderResults.write("   %s\n"%StudentPrompt)

def PrintRegexChecks(regMatches):
    if regMatches != None:
        autograderResults.write("\nSearching Prompt for Regex Expressions -->")
        for regex,match in regMatches:
            if match == None: match = "no match was found"
            autograderResults.write("\n   regex: %s \n"  %(regex))
            autograderResults.write(  "   match: %s \n"%(match))

def printUserInput(test:Test):
    fl = test.UserInput
    if len(fl)>0: autograderResults.write("\nUser Input -->\n")   
    for line in fl:
        autograderResults.write("   %s\n"%line)

def printOutput(test:Test, StudentOutput:List[str], _printHeader:bool):    
    if len(test.Output)==0: return
    autograderResults.write("\n")
    if _printHeader: 
        autograderResults.write("Output -->")
    for i, Eoutput in enumerate(test.Output):
        if Eoutput.addr is None:
            ExAns = GetHexAndDecOrString(test.ExpectedAnswers[i], int(Eoutput.type))
            autograderResults.write("\n Expected   %s = %s\n"%(Eoutput.reg,ExAns))
            try:
                studentAns = GetHexAndDecOrString(StudentOutput[i],int(Eoutput.type))
                autograderResults.write("   Actual   %s = %s\n"%(Eoutput.reg,studentAns))
            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    autograderResults.write("   <FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT>\n")
                    autograderResults.write(StudentOutput[i])
                except:
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        autograderResults.write("   Actual   %s = <FAILED TO RETRIEVE STUDENT OUTPUT>\n"%(Eoutput.reg))
                    else:
                        #autograderResults.write(StudentOutput) #uncomment to see what happened This is the most edgy of edge cases
                        autograderResults.write("\n\n!!!!! SOMETHING WENT HORRIBLY WRONG !!!!!\n Please report this bug to an administrator \n\n")
            continue
        else: 
            autograderResults.write("\n Expected   %s at address %s\n"%(test.ExpectedAnswers[i],Eoutput.addr))
            try:
                r=StudentOutput[i]
                if len(r.strip())==0: r="<FAILED TO RETRIEVE DATA>"
                autograderResults.write("   Actual   %s at address %s\n"%(r,Eoutput.addr))
            except:
                try: 
                    StudentOutput[i] # test for value before printing anything
                    autograderResults.write("   <FAILED TO PROPERLY RETRIEVE STUDENT OUTPUT>\n")
                    autograderResults.write(StudentOutput[i])
                except: 
                    if ("<NO OUTPUT FOUND>") in StudentOutput:
                        r="<FAILED TO RETRIEVE DATA>"
                        autograderResults.write("   Actual   %s at address %s\n"%(r,Eoutput.addr))
                    else:
                        #autograderResults.write(StudentOutput) #uncomment to see what happened This is the most edgy of edge cases
                        #autograderResults.write("\n\n!!!!! SOMETHING WENT HORRIBLY WRONG !!!!!\n If you are a student please inform an administrator of this bug so that they can report the issue \n\n")
                        r="<FAILED TO RETRIEVE DATA>"
                        autograderResults.write("   Actual   %s at address %s\n"%(r,Eoutput.addr))
            continue

def Is_int(s):
    try:
        int(s)
        return True
    except: return False

def to_hex(val, nbits=32):
    val=int(val)
    return hex((val + (1 << nbits)) % (1 << nbits))

def to_int(val, nbits=32):
    val=int(val,16)
    low=1<<nbits
    if val < low: return val
    return val-low


def GetHexAndDecOrString(s, type=0):
    s=s.strip()
    if type == 11 and len(s)==1:  return " %s ( \'%s\' )"%(to_hex(ord(s)),s)
    
    if Is_int(s): return "%s ( %s )"%(s, to_hex(s))
    
    if s[0:2] == '0x': return "%s ( %s )"%(int(s[2:],16), s.lower())
    
    return s


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    try: _ShowAll=sys.argv[1]
    except: _ShowAll=Show.NONE # overrides json "show" and shows the StudentOutputs of every test

    autograder(_ShowAll=_ShowAll)
