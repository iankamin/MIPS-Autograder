import json,os,sys

class settings():
    def __init__(self, file):
    
        with open(file, 'r') as f: io = json.load(f)

        self.SubroutineName=io["subroutine_name"]
        self.PromptGrade=float(io["PromptGrade"])
        self.TestGrade=float(io["TestGrade"])
        
        try:self.ECTestGrade=float(io["ECTestGrade"])
        except: self.ECTestGrade=self.TestGrade

        try:self.MessageToStudent=io["MessageToStudent"]
        except:self.MessageToStudent=""

        try: self.ShowAll=io["ShowAll"].lower()=="true"
        except: self.ShowAll = False
        
        
        try: self.BareMode=io["BareMode"].lower()=="true"
        except: self.BareMode = False
        
        try: self.UserInput=io["UserInput"].lower()=="true"
        except: self.UserInput = False

        self.CreateTests(io["tests"],io)



    def CreateTests(self,alltests_json,io):
        self.AllTests=[]
        for testjs in alltests_json:
            test=self.Test(testjs,self.TestGrade,self.ECTestGrade,io)
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
        def __init__(self, testjs,tg,ectg,io):
            try: self.show=testjs["show"].lower()=="true"
            except: self.show = False
        
            try:    self.ExtraCredit = testjs["ExtraCredit"].lower() == 'true'
            except: self.ExtraCredit = False
        
            try: self.showOutput = io["ShowOutput"].lower()=="true"
            except: 
                try: self.showOutput = testjs["ShowOutput"].lower() == "true"
                except: self.showOutput = False
            
            try: self.OutOf = testjs["OutOf"]
            except:
                if self.ExtraCredit: self.OutOf = ectg
                else: self.OutOf = tg
            
            self.ExpectedAnswers=testjs["ExpectedAnswers"]
            
            try: self.filelines=testjs["filelines"]
            except: self.filelines = []


            self.MemInputs=[]
            self.RegInputs=[]
            self.Output=[]
            try: self.setInputs(testjs["inputs"])
            except: None
            self.setOutputs(testjs["outputs"])

            
        def setInputs(self, inputs):
            for inp in inputs:
                try: self.MemInputs.append( self.__MemInput__( inp["addr"], inp["data"],inp["type"]))
                except: None
            
                try: self.RegInputs.append( self.__RegInput__( inp["reg"], inp["addr"]))
                except: None

                try: self.RegInputs.append( self.__RegInput__( inp["reg"], inp["val"]))
                except: None

        def setOutputs(self, outputs):
            for out in outputs:
                try: 
                    self.Output.append( self.__Output__( type='4', reg='a0', addr=out["addr"] ))
                    continue
                except: None
            
                try: 
                    self.Output.append( self.__Output__(  type=out["type"], reg=out["reg"]))
                except:  raise Exception("Output not address or register")

                


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

        


            


