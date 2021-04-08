import json
import os, sys
import re
from settings import settings



'''
splits student submission 
submission[0] - expected data section
submission[1] - skelton code
submission[2] - .text section
'''    
def getSubmission(sfile):
    with open ("concatErrors.txt",'w') as f: f.write('\n') 
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
        with open ("concatErrors.txt",'a+') as f: f.write("NON ASCII CHARACTER was found in your program\nAttempting to fix but may cause additional issues\nplease check your code and remove potential problems\nPotential Problems denoted with \'X\' :\n%s\n"%problems)
        
    submission = submission.replace("XXAAXX783908782388289038339",'#XXAAXX783908782388289038339 #')
    submission = submission.replace(".globl",'#.globl')
    submission = submission.replace(".global",'#.global')
    submission = submission.replace("XXFFVV3793","XXFFAV3793") #just in case its coincidentally used by the student
    submission = submission.split("XXAAXX783908782388289038339")
    #print(submission)
    return submission

'''
If the student places .data at the bottom of the code this will move it to the top 
(hopefully this should preserve the location of data in memory)
'''
def mergeMemory(submission):
    dataConcat = ""#".global main\n"

    # splits expected .text section if .data is found
    
    
    dataCheck = submission[2].split(".data")
    if len(dataCheck)>1:                    # True is '.data' is present
        submission[2]=dataCheck[0]          # assumes .text section is first (should be)
        for sect in dataCheck[1:]:          # adds the term '.data' back after split
            dataConcat+='\n.data'+sect      
    
    #   Gets the static memory data

    S_Header=open('template/TemplateStaticHeader','r')
    dataConcat+='\n'+S_Header.read()
    
    # organizes data found in submission[0] .global is placed at the top everything else is placed at the bottom
    for line in submission[0].split('\n'):
        line=line+'\n'
        if ".global" in line or ".globl" in line:
            dataConcat= line + dataConcat
        else:
            dataConcat+= line
    
    return dataConcat,submission[2]

def bareModeIllegalSyntax(data, text, errors):
    global runMips
    pseudo_list = ['li ', 'la ', 'move ', 'mov ', 'blt ', 'ble ','bgt ','bge ' ] 

    used_inst=[]
    for line in text.split('\n'):
        for inst in pseudo_list:
            vvv = inst in line
            if vvv:
                if notComment(line, ".text"): 
                    used_inst.append("the pseudoinstruction \' %s\' was used here -> %s\n"%(inst, line.strip()))
                    runMips=False
    errors.writelines(used_inst)

def illegalSyscalls(line, syscode):
        if "$v0" not in line: return False

        while '0x0' in line: line= line.replace('0x0','0x')
        
        hexcode=hex(syscode).replace('0x','')
        if " %s "%syscode in line or ',%s '%syscode in line or '0x%s '%hexcode.lower in line:
            if "li" in line and notComment(line,"li"): return True
            if "addi" in line and notComment(line,"addi"): return True
        return False

def illegalSyntax(data, text, bareMode):
    global io
    global runMips
    errors=open("concatErrors.txt","a+")
    errors.writelines("\n")
    if io.BareMode: bareModeIllegalSyntax(data,text, errors)
    
    if ".text" in data.lower(): errors.writelines("your .text section was found somplace it shouldn't be\n")


    for line in data.split('\n') :
        linelow=line.lower()
        if io.SubroutineName in linelow:
            if notComment(linelow, io.SubroutineName):
                errors.writelines("   %s cannot be used as a label in the data section\n"%io.SubroutineName)

    if io.SubroutineName not in text:
        errors.writelines("   Subroutine \" %s \" not found in test section\n"%io.SubroutineName)

    illegalLines=[]
    for line in text.split('\n'):
        line = line + ' '
        line = line.replace('#', ' #')
        
        linelow=line.lower()
        if ".text" in linelow:
            if notComment(linelow, ".text"): 
                errors.writelines("The only .text should be in the skeleton code\n")
                continue
        
        if illegalSyscalls(linelow, 10): errors.writelines("your program is a subroutine it must not terminate with syscall 10\n")

        if not io.UserInput:
            if illegalSyscalls(linelow, 5) or illegalSyscalls(linelow, 6) or illegalSyscalls(linelow, 7) or illegalSyscalls(linelow, 8) or illegalSyscalls(linelow, 12) : 
                runMips=False
                illegalLines.append(line)
    
    if len(illegalLines)>0:
        errors.writelines("You should not be requesting user input in this submission. \nyou program will not run until the following lines are removed or modified\n")
        for line in illegalLines:
            errors.writelines("    %s\n"%line)

    errors.close()
        
def notComment(line, substr)           :
    index=line.find(substr)
    comment=line.find('#')
    if comment == -1: return True
    return index<comment

def removeComments(submission):
    out=""
    for i,line in enumerate(submission.split("\n")):
        if "#" in line:
            line = line[:line.index("#")]
        out += line+"\n"
    return out

def concat(IO=None,sfile="submission.s"):
    global inputs,io
    global runMips,output,S_Header,S_Trailer
    output=open('concat.s','w')
    
    if IO == None: io =settings("settings.json")
    else : io=IO
    runMips=True
    
    #with open("mipsCreator.json") as j: io=json.load(j)

    submission = getSubmission(sfile)
    submission[0] = removeComments(submission[0])
    submission[1] = removeComments(submission[1])
    submission[2] = removeComments(submission[2])
    dataSect,textSect=mergeMemory(submission)
    output.write(dataSect)

    illegalSyntax(dataSect,textSect,io.BareMode)

    allTests=""
    for test in io.AllTests:
        with open('template/TemplateTrial','r') as S_Trial:
            body = S_Trial.read()
            body=body.replace("<student_subroutine>",io.SubroutineName)
        
        inputs=CreateAllInputs(test)
        outputs=CreateAllOutputs(test)

        body=body.replace("<inputs>",inputs)
        body=body.replace("<outputs>",outputs)
        allTests+=body
        #print(allTests)
        
    S_Trailer=open('template/TemplateStaticTrailer','r')
    output.write(S_Trailer.read().replace("<TRIALS>",allTests))
    output.write(textSect)
    output.close()
    return runMips

def CreateAllInputs(test):
    global io
    inputs=""

    for inp in test.MemInputs:
        output.write(createInputMem(inp.addr,inp.data,inp.type))
    
    for inp in test.RegInputs:
        inputs+=createInputReg(inp.reg,inp.value)

    return inputs
        
def CreateAllOutputs(test):
    outputs=""

    for out in test.Output: 
        outputs+=createOutput(out)
    return outputs

def createInputMem(_addr,_data,_type):
    _type='.'+_type.replace(".",'')
    _addr='0x'+_addr.replace("0x",'')
    with open("template/TemplateInitMemory",'r') as f:
        contents=f.read()
        contents=contents.replace("<addr>",_addr)
        contents=contents.replace("<type>",_type)
        contents=contents.replace("<data>","\""+_data+"\"")
        return contents

def createInputReg(_reg,_val):
    _reg='$'+_reg.replace('$','')
    if '0x' in _val.strip():
        _val= '0x'+_val[2:].zfill(8)
        #print(_val)
    with open("template/TemplateInitRegister",'r') as f:
        contents=f.read()
        contents=contents.replace("<reg>",_reg)

        if '0x' in _val:
            contents=contents.replace("<upper_val>",'0x'+_val[2:6])
            contents=contents.replace("<lower_val>",'0x'+_val[6:])
        else:
            contents=contents.replace("<upper_val>",'0')
            contents=contents.replace("<lower_val>",_val)
        
        return contents

def createOutput(out):
    with open("template/TemplateOut",'r') as f:
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