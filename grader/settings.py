import json,os,sys,random
from enum import Enum

class Show(Enum):
    NONE=0
    INPUT=1
    OUTPUT=2
    ALL=3

    def __gt__(self,other): return self.value>other.value
    def __ge__(self,other): return self.value>=other.value
    def __lt__(self,other): return self.value<other.value
    def __le__(self,other): return self.value<=other.value


#TODO MAX points need to account for individual tests
#TODO Prompt Points must ignore extra credit
#TODO seperate Regular Tests and extra credit Tests
class settings():


    def __init__(self, file=None,**kwargs):
        if file is None:
            self.empty(**kwargs)
            return

        with open(file, 'r') as f: io = json.load(f)
        self.io=io

        self.SubroutineName=io["subroutine_name"]
        
        self.PromptGrade=float(io.get("PromptGrade",0))
        self.TestGrade=float(io.get("TestGrade",1))
        self.ECTestGrade=float(io.get("ECTestGrade",self.TestGrade))
        self.ShowLevel=Show(io.get("ShowLevel",0))
        self.MessageToStudent=io.get("MessageToStudent","")
        self.BareMode = io.get("BareMode",False)
        self.Shuffle = io.get("Shuffle",False)
        self.JsonStyle = io.get("JsonStyle",0)
        self.RequiresUserInput = io.get("RequiresUserInput",False)
        
        if type(self.BareMode) is str: self.BareMode = self.BareMode.lower()=="true"
        if type(self.Shuffle)  is str: self.Shuffle  = self.Shuffle.lower() =="true"
        if type(self.RequiresUserInput) is str: self.RequiresUserInput = self.RequiresUserInput.lower()=="true"
        
        self.NumberOfRegularTests=0
        self.AllTests=self.CreateTests(io["tests"],io)


    def empty(self,**kwargs):
        self.io=None
        self.SubroutineName=None
        self.PromptGrade=None
        self.TestGrade=None
        self.ECTestGrade=None
        self.MessageToStudent=None
        self.ShowLevel=Show.NONE
        self.BareMode = False
        self.RequiresUserInput = False
        self.AllTests=[]

    def CreateTests(self,alltests_json,io):
        reg,ec=[],[]
        for i,testjs in enumerate(alltests_json):
            test=Test(parent=self,testjs=testjs,testNumber=i)
            if test.ExtraCredit: ec.append(test)
            else:                reg.append(test)
        self.reg=reg
        self.ec=ec
        self.NumberOfRegularTests=len(reg)
        self.NumberOfExtraCreditTests=len(ec)
        return reg+ec
    def getTests(self, canShuffle=True):
        self.reg=self.AllTests[:self.NumberOfRegularTests]
        self.ec=self.AllTests[self.NumberOfRegularTests:]
        if self.Shuffle and canShuffle:
            random.shuffle(self.ec)
            random.shuffle(self.reg)
        return self.reg+self.ec


    def getAllUserInputLines(self):
        for test in self.AllTests:
            for line in test.UserInput:
                yield line

    def printHeader(self):
        print("\n\nREQUIRED ROUTINE: %s"%self.SubroutineName)
        if self.MessageToStudent:
            print("GENERAL MESSAGE: %s\n"%self.MessageToStudent)
    def ToDict(self):
        io={}
        io["subroutine_name"]=self.SubroutineName
        io["PromptGrade"]=self.PromptGrade
        io["TestGrade"]=self.TestGrade
        io["ECTestGrade"]=self.ECTestGrade
        io["MessageToStudent"]=self.MessageToStudent
        io["BareMode"]=self.BareMode
        io["RequiresUserInput"]=self.RequiresUserInput
        io["ShowLevel"]=self.ShowLevel.value
        io["Shuffle"]=self.Shuffle
        io["JsonStyle"]=self.JsonStyle
        io["tests"]=[t.ToDict() for t in self.AllTests]
        return io

class Test():
    parent:settings
    # Initialize from JSON
    def __init__(self,parent, testjs=None,testNumber=0,**kwargs):
        self.parent=parent
        if testjs is None: 
            self.empty(**kwargs)
            return

        self.ShowLevel =  max(Show(testjs.get("ShowLevel",0)) , parent.ShowLevel )
        self.testName   = testjs.get("name","Test").strip()
        self.testNumber = testNumber   
        self.ExtraCredit= testjs.get("ExtraCredit",False) 
        self.OutOf      = testjs.get("OutOf",0) or (parent.ECTestGrade if self.ExtraCredit else parent.TestGrade)
        self.UserInput  = testjs.get("UserInput",[])
        
        if type(self.ExtraCredit) is str: self.ExtraCredit= self.ExtraCredit.lower()=="true"
        
        # Get Inputs and Outputs
        self.MemInputs,self.RegInputs = self.setInputs(testjs.get("inputs",[]))
        self.ExpectedAnswers,self.Output=self.setOutputs(testjs["outputs"])
        i=0
    def empty(self,**kwargs):
        self.testName = "Test"
    
        self.ExtraCredit = False
        self.ShowLevel=Show.NONE
        self.OutOf = 0
        self.UserInput = []

        self.MemInputs=[]
        self.RegInputs=[]
        self.Output=[]
    
    def ToDict(self):
        testjs={}
        testjs["name"]=self.testName
        testjs["ExtraCredit"]=self.ExtraCredit 
        if self.OutOf==(self.parent.ECTestGrade if self.ExtraCredit else self.parent.TestGrade):
            testjs["OutOf"]=0
        else: testjs["OutOf"]=self.OutOf 
        testjs["ShowLevel"]=Show.NONE.value if self.ShowLevel == self.parent.ShowLevel else self.ShowLevel.value
        testjs["UserInput"]=self.UserInput
        testjs["inputs"]=[i.ToDict() for i in self.MemInputs]
        testjs["inputs"] += [i.ToDict() for i in self.RegInputs if not i.memPointer]
        testjs["outputs"]=[i.ToDict() for i in self.Output]
        return testjs
        
    def setInputs(self, inputs):
        memInputs=[]
        regInputs=[]
        for inp in inputs:

            try: 
                memInputs.append( self.__MemInput__( inp["addr"], inp["data"],inp["type"]))
                try: 
                    memInputs[-1].reg=inp["reg"]
                    regInputs.append( self.__RegInput__( inp["reg"], inp["addr"],memPointer=True))
                except KeyError as e:pass #print(e)
            except KeyError: None

            try: regInputs.append( self.__RegInput__( inp["reg"], inp["value"]))
            except KeyError: None
        return memInputs,regInputs

    def setOutputs(self, outputsJS):
        ExpectedAnswers=[]
        outputs=[]
        for out in outputsJS:
            ans=out["CorrectAnswer"]
            ExpectedAnswers.append(ans)
            try: # print string stored at address out["addr"] 
                outputs.append( self.__Output__( type='4', reg='a0', addr=out["addr"],CorrectAnswer=ans))
                continue
            except KeyError as e: pass#print(e) 
        
            try: # print value of register
                outputs.append( self.__Output__(  type=out["type"], reg=out["reg"],CorrectAnswer=ans))
            except:  raise Exception("Output not address or register")
        return ExpectedAnswers,outputs

            
    class __RegInput__:
        def __init__(self,reg,value,memPointer=False):
            self.reg='$'+reg.replace('$','')
            self.value=value
            self.memPointer=memPointer
        
        def ToDict(self):
            if self.memPointer is False: 
                return {"reg":self.reg.replace("$",""),"value":self.value}

    class __MemInput__:
        def __init__(self,addr,data,type,reg=None):
            self.addr=addr
            self.data=data
            self.type=type
            self.reg=reg
            
            if "ascii" in type.lower(): 
                self.data=self.data.replace("\\\"","quote_7654123")
                self.data=self.data.replace("\"","")
                self.data=self.data.replace("quote_7654123","\\\"")
                self.data='\"'+self.data+'\"'

        
        def ToDict(self):
            d = { "type":self.type, "addr":self.addr, 'data':self.data.replace("\"","") }
            if self.reg is not None: d["reg"]=self.reg.replace("$","")
            return d
    
    class __Output__:
        def __init__(self,type,CorrectAnswer,reg=None,addr=None):
            if reg is None and addr is None: raise Exception("reg or addr must be given a value")
            if reg is not None: self.reg = '$'+reg.replace('$','')
            else:self.reg=reg
            self.type = str(type)
            self.addr = addr
            self.CorrectAnswer = CorrectAnswer
            
            if addr is None:
                self.lui_reg = "$0"
                self.upper_addr = '0'
                self.lower_addr = '0'
            else:
                if reg is not None: self.lui_reg = '$'+reg.replace('$','')
                if '0x' in addr.strip(): 
                    addr = addr.strip()[2:].zfill(8)
                self.upper_addr = '0x'+addr[:4]
                self.lower_addr = '0x'+addr[4:]
        
        def ToDict(self):
            d = {"type":self.type, "CorrectAnswer":self.CorrectAnswer }
            if self.addr is not None: d["addr"]=self.addr
            if self.reg is not None: d["reg"]=self.reg.replace("$","")
            return d
                

def isInt(val):
    try:
        float(val)
        return True
    except:
        return False


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    tt = settings("settings.json")
    d=tt.ToDict()
    j=json.dumps(d,indent=4)
    print(j)



            


