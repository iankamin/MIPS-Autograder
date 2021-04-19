import json,os,sys,random
#TODO MAX points need to account for individual tests
#TODO Prompt Points must ignore extra credit
#TODO seperate Regular Tests and extra credit Tests
class settings():
    def __init__(self):
        self.io=None
        self.SubroutineName=None
        self.PromptGrade=None
        self.TestGrade=None
        self.ECTestGrade=None
        self.MessageToStudent=None
        self.ShowAll = False
        self.BareMode = False
        self.RequiresUserInput = False
        self.AllTests=[]


    def __init__(self, file):
    
        with open(file, 'r') as f: io = json.load(f)
        self.io=io

        self.SubroutineName=io["subroutine_name"]
        self.PromptGrade=float(io["PromptGrade"])
        self.TestGrade=float(io["TestGrade"])
        
        try: self.ECTestGrade=float(io["ECTestGrade"])
        except KeyError: self.ECTestGrade=self.TestGrade

        try: self.MessageToStudent=io["MessageToStudent"]
        except KeyError: self.MessageToStudent=""

        try: 
            if type(io["ShowAll"]) is str: self.ShowAll=io["ShowAll"].lower()=="true"
            elif type(io["ShowAll"]) is bool: self.ShowAll = io["ShowAll"]
            else: self.ShowAll
        except KeyError: self.ShowAll = False
        
        try: 
            if type(io["ShowAllOutput"]) is str: self.ShowAllOutput=io["ShowAllOutput"].lower()=="true"
            elif type(io["ShowAllOutput"]) is bool: self.ShowAllOutput = io["ShowAllOutput"]
            else: self.ShowAllOutput
        except KeyError: self.ShowAllOutput = False
        
        
        try: 
            if type(io["BareMode"]) is str: self.BareMode=io["BareMode"].lower()=="true"
            elif type(io["BareMode"]) is bool: self.BareMode = io["BareMode"]
            else: self.BareMode
        except KeyError: self.BareMode = False
        
        try: 
            if type(io["Shuffle"]) is str: self.Shuffle=io["Shuffle"].lower()=="true"
            elif type(io["Shuffle"]) is bool: self.Shuffle = io["Shuffle"]
            else: self.Shuffle
        except KeyError: self.Shuffle = False
        
        try: 
            if type(io["RequiresUserInput"]) is str: self.RequiresUserInput=io["RequiresUserInput"].lower()=="true"
            elif type(io["RequiresUserInput"]) is bool: self.RequiresUserInput = io["RequiresUserInput"]
            else: self.RequiresUserInput
        except KeyError: self.RequiresUserInput = False

        self.AllTests=self.CreateTests(io["tests"],io,canShuffle=True)



    def CreateTests(self,alltests_json,io,canShuffle=False):
        reg,ec=[],[]
        for i,testjs in enumerate(alltests_json):
            test=self.Test(self,testjs,i)
            if test.ExtraCredit: ec.append(test)
            else:                reg.append(test)
        if self.Shuffle and canShuffle:
            random.shuffle(ec)
            random.shuffle(reg)
        return reg+ec

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
        io["ShowAll"]=self.ShowAll
        io["ShowAllOutput"]=self.ShowAllOutput
        io["BareMode"]=self.BareMode
        io["RequiresUserInput"]=self.RequiresUserInput
        io["Shuffle"]=self.Shuffle
        io["tests"]=[t.ToDict() for t in self.AllTests]
        return io

    class Test:
        def __init__(self):
            self.show = False
            self.testName = "Test"
        
            self.ExtraCredit = False
            self.showOutput = False
            self.OutOf = 0
            self.UserInput = []

            self.MemInputs=[]
            self.RegInputs=[]
            self.Output=[]
        def __init__(self,parent, testjs,testNumber):
            try: 
                if type(testjs["show"]) is str: self.show=testjs["show"].lower()=="true"
                elif type(testjs["show"]) is bool: self.show = testjs["show"]
                else: self.show
            except KeyError: self.show = False

           # Name and Number should make finding a specific Test in the .s file easier 
            try: self.testName=testjs["name"].strip()
            except KeyError: self.testName = "Test"
            self.testNumber=testNumber   
        
            try:    
                if type(testjs["ExtraCredit"]) is str: self.ExtraCredit=testjs["ExtraCredit"].lower()=="true"
                elif type(testjs["ExtraCredit"]) is bool: self.ExtraCredit = testjs["ExtraCredit"]
                else: self.ExtraCredit
            except KeyError: self.ExtraCredit = False
        
            try: 
                if type(testjs["showOutput"]) is str: self.showOutput=testjs["showOutput"].lower()=="true"
                elif type(testjs["showOutput"]) is bool: self.showOutput = testjs["showOutput"]
                else: self.showOutput
            except KeyError: 
                self.showOutput = parent.ShowAllOutput
            
            try: self.OutOf = testjs["OutOf"]
            except KeyError:
                if self.ExtraCredit: self.OutOf = parent.ECTestGrade
                else: self.OutOf = parent.TestGrade
            
            try: self.UserInput=testjs["UserInput"]
            except KeyError: self.UserInput = []


            self.MemInputs=[]
            self.RegInputs=[]
            self.Output=[]
            try: i=testjs["inputs"]
            except KeyError: i=[]
            self.setInputs(i)
            
            self.ExpectedAnswers=self.setOutputs(testjs["outputs"])
        
        def ToDict(self):
            testjs={}
            testjs["name"]=self.testName
            testjs["ExtraCredit"]=self.ExtraCredit 
            testjs["OutOf"]=self.OutOf 
            testjs["show"]=self.show
            testjs["ShowOutput"]=self.showOutput 
            testjs["UserInput"]=self.UserInput
            testjs["inputs"]=[i.ToDict() for i in self.RegInputs]
            testjs["outputs"]=[i.ToDict() for i in self.Output]
            return testjs


            
        def setInputs(self, inputs):
            for inp in inputs:

                try: self.MemInputs.append( self.__MemInput__( inp["addr"], inp["data"],inp["type"]))
                except KeyError: None
                try: 
                    self.RegInputs.append( self.__RegInput__( inp["reg"], inp["addr"],memPointer=self.MemInputs[-1]))
                except KeyError as e: print(e)

                try: self.RegInputs.append( self.__RegInput__( inp["reg"], inp["value"]))
                except KeyError: None

        def setOutputs(self, outputs):
            ExpectedAnswers=[]
            for out in outputs:
                ans=out["CorrectAnswer"]
                ExpectedAnswers.append(ans)
                try: # print string stored at address out["addr"] 
                    self.Output.append( self.__Output__( type='4', reg='a0', addr=out["addr"],ans=ans))
                    continue
                except KeyError: None
            
                try: # print value of register
                    self.Output.append( self.__Output__(  type=out["type"], reg=out["reg"],ans=ans))
                except:  raise Exception("Output not address or register")
            return ExpectedAnswers

                


        class __RegInput__:
            def __init__(self,reg,value,memPointer=None):
                self.reg='$'+reg.replace('$','')
                self.value=value
                self.memPointer=memPointer
                if memPointer is not None: self.memPointer.reg=self.reg
            
            def ToDict(self):
                if self.memPointer is None: return {"reg":self.reg,"value":self.value}
                else:                       return self.memPointer.ToDict()

        class __MemInput__:
            def __init__(self,addr,data,type):
                self.addr=addr
                self.data=data
                self.type=type
                self.reg = None
            def ToDict(self):
                d = { "type":self.type, "addr":self.addr, 'data':self.data }
                if self.reg is not None: d["reg"]=self.reg
                return d
        
        class __Output__:
            def __init__(self,type,reg,ans,addr=None):
                self.reg = '$'+reg.replace('$','')
                self.type = type
                self.addr = addr
                self.CorrectAnswer = ans
                
                if addr is None:
                    self.lui_reg = "$0"
                    self.upper_addr = '0'
                    self.lower_addr = '0'
                else:
                    self.lui_reg = '$'+reg.replace('$','')
                    if '0x' in addr.strip(): 
                        addr = addr.strip()[2:].zfill(8)
                    self.upper_addr = '0x'+addr[:4]
                    self.lower_addr = '0x'+addr[4:]
            def ToDict(self):
                d = { "reg":self.reg, "type":self.type, "CorrectAnswer":self.CorrectAnswer }
                if self.addr is not None: d["addr"]=self.addr
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



            


