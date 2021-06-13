from io import FileIO
import json
import os, sys
import re
from typing import List, Tuple

try: from .settings import settings,Test,Show
except: from settings import settings,Test,Show

localDir = os.path.dirname(__file__)+"/"
StorageDir=localDir

'''
splits student submission 
'''    
runMips=True
def getSubmission(sfile:FileIO) -> (tuple([str,str])):
    """[summary]

    Args:
        sfile (FileIO): [description]

    Returns:
        (data,text) (str,str): returns the data and text sections of the student submission 
    """
    global runMips
    errors = open(localDir + "concatErrors.txt",'w')
    errors.write('\n') 
    try:
        with open(sfile,'r') as f: 
            submission=f.read()
    except:
        with open(sfile,'rb') as f:
            submission=f.read()
        
        probIndices=[(m.start(0),m.end(0)) for m in re.finditer(bytes('[^\x00-\x7F]+','utf-8'),submission)]
        
        submission=re.sub(bytes('[^\x00-\x7F]','utf-8'),bytes(' ','utf-8'), submission)
        submission=submission.decode('utf-8')
        
        problems=''
        for (s,e) in probIndices:
            linestart,lineend=submission[:s].rfind('\n')+1,submission[e:].find('\n')+e
            sub=submission[linestart:s]+'X'*(e-s)+submission[e:lineend]
            problems+=sub+'\n'
        errors.write("NON ASCII CHARACTER was found in your program\nAttempting to fix but may cause additional issues\nplease check your code and remove potential problems\nPotential Problems denoted with \'X\' :\n%s\n"%problems)
    
    submission = removeComments(submission)
    submission = AddLineNumbers(submission)
    submission = submission.replace("XXAAXX783908782388289038339",'#XXAAXX783908782388289038339 #')
    submission = submission.replace(".globl",'#.globl')
    submission = submission.replace(".global",'#.global')
    submission = submission.replace("XXFFVV3793","studentGBG") #just in case the unique print marker is used by the student coincidentally used by the student
    submission = submission.split("XXAAXX783908782388289038339")

    if len(submission) != 3:
        errors.writelines("Unable to find Skeleton Code. \nI Give Up.\n")
        runMips=False
        errors.close()
        return None,None,None

    errors.close()  
    dataSectT,textSect=mergeMemory(submission[0].strip())
    submission[2]='\n'.join(submission[2].split('\n')[1:])
    dataSectB,textSectB=mergeMemory(submission[2].strip())
    textSect+=textSectB
       
    #print(submission)
    return '\n'.join(dataSectT),'\n'.join(dataSectB),'\n'.join(textSect)
def AddLineNumbers(submission:str):
    out=''
    for i,line in enumerate(submission.split('\n')):
        if line.strip() == "": 
            out += '\n' #uncomment to increase readability of ASM concat file
            continue
        if len(line) < 30: 
            line = "{0: <30}".format(line)
        line += " # line %s\n"%(i+1)
        out = out+line
    return out

'''
If the student places .data at the bottom of the code this will move it to the top 
(hopefully this should preserve the location of data in memory)
'''
def mergeMemory(sub:str):
    dataConcat = ""#".global main\n"
    dataSect=[]
    textSect=[]
    # splits expected .text section if .data is found
    sects = sub.split(".data")
    sects:list
    topText=sects.pop(0)
    textSect.append(topText)
    for sect in sects:
        sect = sect.split(".text")
        dataSect.append("\n.data"+sect.pop(0))
        for text in sect:
            textSect.append("\n.text"+text)

    return dataSect,textSect





def bareModeIllegalSyntax(data:str, text:str, errors:FileIO):
    global runMips
    pseudo_list = ['li ', 'la ', 'move ', 'mov ', 'blt ', 'ble ','bgt ','bge ' ] 

    used_inst=[]
    for line in text.split('\n'):
        for inst in pseudo_list:
            vvv = inst in line
            if vvv:
                if notComment(line, inst): 
                    used_inst.append("the (NON-BAREMODE) pseudoinstruction \"%s\" was used here -> %s\n"%(inst.strip(), line.strip()))
                    runMips=False
    errors.writelines(used_inst)

def bannedISA_SyntaxChecks(text:str,errors:FileIO):
    global runMips
    pseudo_list = io.BannedISA
    
    used_inst=[]
    for inst in pseudo_list:
        inst:str
        inst=inst.lower()
        inst=inst.strip()+' '
        for line in text.split('\n'):
            linelow=line.lower().strip()
            found = inst in linelow
            if found:
                if notComment(linelow, inst): 
                    used_inst.append("the instruction \"%s\" is banned for this assignement but was used here -> %s\n"%(inst.strip(), line.strip()))
                    runMips=False

    errors.writelines(used_inst)



def illegalSyscalls(line:str, syscode:str):
        if "$v0" not in line: return False

        while '0x0' in line: line= line.replace('0x0','0x')
        
        hexcode=hex(syscode).replace('0x','')
        if " %s "%syscode in line or ',%s '%syscode in line or '0x%s '%hexcode.lower in line:
            if "li" in line and notComment(line,"li"): return True
            if "addi" in line and notComment(line,"addi"): return True
        return False

def illegalSyntax(data:str, text:str, bareMode:bool):
    global io
    global runMips
    errors=open(localDir + "concatErrors.txt","a+")
    errors.writelines("\n")
    if io.BareMode: bareModeIllegalSyntax(data,text, errors)
    bannedISA_SyntaxChecks(text,errors)
    
    for line in data.split('\n') :
        linelow=line.lower()
        if io.SubroutineName in linelow:
            if notComment(linelow, io.SubroutineName):
                errors.writelines("   The Required Subroutine \"%s\" cannot be used as a label in the data section -> %s\n"%(io.SubroutineName, line.strip()))

    if io.SubroutineName not in text:
        errors.writelines("   The Required Subroutine \"%s\" was not found in the text section\n"%io.SubroutineName)

    illegalLines=[]
    for line in text.split('\n'):
        line:str
        line = line + ' '
        line = line.replace('#', ' #')
        
        linelow=line.lower()
        if illegalSyscalls(linelow, 10): errors.writelines("your program is a subroutine it must not terminate with syscall 10 -> %s\n"%line)

        if not io.RequiresUserInput:
            if illegalSyscalls(linelow, 5) or illegalSyscalls(linelow, 6) or illegalSyscalls(linelow, 7) or illegalSyscalls(linelow, 8) or illegalSyscalls(linelow, 12) : 
                runMips=False
                illegalLines.append(line)
    
    if len(illegalLines)>0:
        errors.writelines("\nYou should not be requesting user input in this submission. \nyou program will not run until the following lines are removed or modified\n")
        for line in illegalLines:
            errors.writelines("    %s\n"%line.strip())

    errors.close()
        
def notComment(line:str, substr:str) -> (bool):
    """ determines if a given substring is a comment.
        The comment marker is '#'

    Args:
        line (str): the line of text to search through
        substr (str): the substring to check if is/is not a comment

    Returns:
        [bool]: False if substring is a comment
    """
    index=line.find(substr)
    comment=line.find('#')
    if comment == -1: return True
    return index<comment

def removeComments(submission:str) -> (str):
    """removes all comments(#) from a block of code

    Args:
        submission (str): the original code

    Returns:
        [str]: the comment free version of code
    """
    out=""
    for i,line in enumerate(submission.split("\n")):
        if "XXAAXX783908782388289038339" in line: 
            out += line+"\n"
            continue
        if "#" in line:
            line = line[:line.index("#")]
        out += line+"\n"
    return out


def createSkeletonCode(io:settings,destFile=localDir+"Skeleton.s"):
    allTrials=""
    dataSect=""

    with open(localDir + 'template/TemplateSkeletonTrial','r') as f: trialTemplate = f.read()
    trialTemplate = trialTemplate.replace("<student_subroutine>",io.SubroutineName)
    for test in io.getTests(canShuffle=False):
        inputs,memory = CreateAllInputs(test)
        trial = trialTemplate.replace("<inputs>",inputs)
        
        dataSect+=memory
        allTrials+=trial

    with open(localDir + 'template/TemplateSkeleton','r') as f: output=f.read()
    output=output.replace("<TRIALS>",allTrials)
    output=output.replace("<DATA SECTION>",dataSect)
    if io.BareMode:
        output=output.replace("<STUDENT_ADDRESS>",'0x10000000')
    else:
        output=output.replace("<STUDENT_ADDRESS>",'0x10010000')

    with open(destFile,'w') as f: f.write(output)
    return output

def concat(IO=None,sfile="submission.s",concatFile="concat.s", skeleton=False):
    global inputs,io
    global runMips,output,S_Header,S_Trailer
    if concatFile == "concat.s": output=open(localDir + 'concat.s','w')
    else: output=open(concatFile,'w')

    if IO == None: io =settings("settings.json")
    else : io=IO
    
    runMips=True
    
    #with open("mipsCreator.json") as j: io=json.load(j)
    output.write(".globl main\n.globl %s\n"%(io.SubroutineName))
    dataSectT,dataSectB,textSect = getSubmission(sfile)

    if runMips==False: return False
    
    output.write(dataSectT)
    
    illegalSyntax(dataSectT+dataSectB,textSect,io.BareMode)

    allTests=""
    memorySect=""
    test:Test
    for test in io.getTests(canShuffle=True):
        with open(localDir + 'template/TemplateTrial','r') as S_Trial:
            body = S_Trial.read()
            body=body.replace("<student_subroutine>",io.SubroutineName)
            body=body.replace("<TEST NAME>",test.testName)
            body=body.replace("<TEST NUMBER>",str(test.testNumber))

        inputs,memory=CreateAllInputs(test)
        memorySect+=memory       
        outputs=CreateAllOutputs(test)

        body=body.replace("<inputs>",inputs)
        body=body.replace("<outputs>",outputs)
        allTests+=body
        #print(allTests)


    S_Trailer=open(localDir + 'template/TemplateStaticTrailer','r')
    output.write(S_Trailer.read().replace("<TRIALS>",allTests))
    output.write(textSect)
    output.write(dataSectB)
    
    with open(localDir + 'template/TemplateStaticHeader','r') as h: 
        output.write('\n'+h.read())
    output.write(memorySect)
    output.close()
    return runMips

def CreateAllInputs(test:Test):
    global io
    inputs=""
    memory=""

    for inp in test.MemInputs:
        memory+=createInputMem(inp.addr,inp.data,inp.type)
    
    for inp in test.RegInputs:
        inputs+=createInputReg(inp.reg,inp.value)

    return inputs,memory
        
def CreateAllOutputs(test:Test):
    outputs=""

    for out in test.Output: 
        outputs+=createOutput(out)
    return outputs

def createInputMem(_addr:str,_data:str,_type:str):
    _type='.'+_type.replace(".",'')
    with open(localDir + "template/TemplateInitMemory",'r') as f:
        contents=f.read()
        contents=contents.replace("<addr>",_addr)
        contents=contents.replace("<type>",_type)
        contents=contents.replace("<data>",_data)
        return contents

def createInputReg(_reg:str,_val:str):
    _reg='$'+_reg.replace('$','')
    if '0x' in _val.strip():
        _val= '0x'+_val[2:].zfill(8)
        #print(_val)
    with open(localDir + "template/TemplateInitRegister",'r') as f:
        contents=f.read()
        contents=contents.replace("<reg>",_reg)

        if '0x' in _val:
            contents=contents.replace("<upper_val>",'0x'+_val[2:6])
            contents=contents.replace("<lower_val>",'0x'+_val[6:])
        else:
            contents=contents.replace("<upper_val>",'0')
            contents=contents.replace("<lower_val>",_val)
        
        return contents

def createOutput(out:Test.__Output__):
    with open(localDir + "template/TemplateOut",'r') as f:
        contents=f.read()
        contents=contents.replace("<upper_addr>",out.upper_addr)
        contents=contents.replace("<lower_addr>",out.lower_addr)
        contents=contents.replace("<reg>",out.reg)
        contents=contents.replace("<lui_reg>",out.lui_reg)
        contents=contents.replace("<type>",out.type)
        return contents
    

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    concat()