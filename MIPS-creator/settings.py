import json,os,sys

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
        self.UserInput = False
        self.AllTests=[]


    def __init__(self, file):
    
        with open(file, 'r') as f: io = json.load(f)
        self.io=io

        self.SubroutineName=io["subroutine_name"]
        self.PromptGrade=float(io["PromptGrade"])
        self.TestGrade=float(io["TestGrade"])
        
        try:self.ECTestGrade=float(io["ECTestGrade"])
        except: self.ECTestGrade=self.TestGrade

        try:self.MessageToStudent=io["MessageToStudent"]
        except:self.MessageToStudent=""

        try: self.ShowAll=io["ShowAll"].lower()=="true"
        except: self.ShowAll = False
        
        try: self.ShowAllOutput=io["ShowAllOutputs"].lower()=="true"
        except: self.ShowAllOutput = False
        
        
        try: self.BareMode=io["BareMode"].lower()=="true"
        except: self.BareMode = False
        
        try: self.UserInput=io["UserInput"].lower()=="true"
        except: self.UserInput = False

        self.CreateTests(io["tests"],io)



    def CreateTests(self,alltests_json,io):
        self.AllTests=[]
        for i,testjs in enumerate(alltests_json):
            test=self.Test(testjs,io,self.TestGrade,self.ECTestGrade,i)
            self.AllTests.append(test)

    def getAllUserInputLines(self):
        for test in self.AllTests:
            for line in test.filelines:
                yield line

    def printHeader(self):
        print("\n\nREQUIRED ROUTINE: %s"%self.SubroutineName)
        if self.MessageToStudent:
            print("GENERAL MESSAGE: %s\n"%self.MessageToStudent)

    class Test:
        def __init__(self):
            self.show = False
            self.testName = "Test"
        
            self.ExtraCredit = False
            self.showOutput = False
            self.OutOf = 0
            self.filelines = []

            self.MemInputs=[]
            self.RegInputs=[]
            self.Output=[]


        def __init__(self, parent, testjs,io,testNumber):
            try: self.show=testjs["show"].lower()=="true"
            except: self.show = False

           # Name and Number should make finding a specific Test in the .s file easier 
            try: self.testName=testjs["name"].strip()
            except: self.testName = "Test"
            self.testNumber=testNumber   
        
            try:    self.ExtraCredit = testjs["ExtraCredit"].lower() == 'true'
            except: self.ExtraCredit = False
        
            try: self.showOutput = (io["ShowOutput"].lower()=="true") or parent.showAllOutputs
            except: 
                try: self.showOutput = testjs["ShowOutput"].lower() == "true"
                except: self.showOutput = False
            
            try: self.OutOf = testjs["OutOf"]
            except:
                if self.ExtraCredit: self.OutOf = parent.ECTestGrade
                else: self.OutOf = parent.TestGrade
            
            try: self.filelines=testjs["filelines"]
            except: self.filelines = []


            self.MemInputs=[]
            self.RegInputs=[]
            self.Output=[]
            try: self.setInputs(testjs["inputs"])
            except: None
            self.ExpectedAnswers=self.setOutputs(testjs["outputs"])

            
        def setInputs(self, inputs):
            for inp in inputs:
                try: self.MemInputs.append( self.__MemInput__( inp["addr"], inp["data"],inp["type"]))
                except: None
            
                try: self.RegInputs.append( self.__RegInput__( inp["reg"], inp["addr"]))
                except: None

                try: self.RegInputs.append( self.__RegInput__( inp["reg"], inp["val"]))
                except: None

        def setOutputs(self, outputs):
            ExpectedAnswers=[]
            for out in outputs:
                ExpectedAnswers.append(out["CorrectAnswer"])
                try: # print string stored at address out["addr"] 
                    self.Output.append( self.__Output__( type='4', reg='a0', addr=out["addr"] ))
                    continue
                except: None
            
                try: # print value of register
                    self.Output.append( self.__Output__(  type=out["type"], reg=out["reg"]))
                except:  raise Exception("Output not address or register")
            return ExpectedAnswers

                


        class __RegInput__:
            def __init__(self,reg,value):
                self.reg='$'+reg.replace('$','')
                self.value=value
        class __MemInput__:
            def __init__(self,addr,data,type):
                self.addr=addr
                self.data=data
                self.type=type
        
        class __Output__:
            def __init__(self,type,reg,addr=None):
                self.reg = '$'+reg.replace('$','')
                self.type = type
                self.addr = addr
                
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
                

def isInt(val):
    try:
        float(val)
        return True
    except:
        return False

        


            


