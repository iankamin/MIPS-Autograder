import json,os,sys,random

from PyQt5.QtCore import QObject, QThread, pyqtSignal
import Autograder




class settings(Autograder.settings):
    def __init__(self, file=None,**kwargs):
        super().__init__(file=file,**kwargs)
    
    def empty(self,**kwargs):
        if len(kwargs) == 0: return
        self.io=None
        self.SubroutineName=kwargs.get("subroutine_name")
        self.PromptGrade=kwargs.get("PromptGrade",0)
        self.TestGrade=kwargs.get("TestGrade",0)
        self.ECTestGrade=kwargs.get("ECTestGrade",self.TestGrade)
        self.MessageToStudent=kwargs.get("MessageToStudent","")
        self.JsonStyle = kwargs.get("JsonStyle")
        self.ShowLevel = Autograder.Show(kwargs.get("ShowLevel"))
        self.BareMode = kwargs.get("BareMode")
        self.RequiresUserInput = kwargs.get("RequiresUserInput")
        self.Shuffle = kwargs.get("Shuffle",False)
        self.AllTests = []

    def AddTest(self,test):
        self.AllTests.append(test)

    def GetJSON(self):
        js=self.ToDict()
        js=json.dumps(js,indent=4)
        return js

class Test(Autograder.Test):
    def __init__(self,parent,testjs=None,testNumber=0):
        super().__init__(parent,testjs,testNumber)

    def head_init(self,**kwargs):
        self.ShowLevel = max(Autograder.Show(kwargs.get("ShowLevel",0)),self.parent.ShowLevel)
        self.testName   = kwargs.get("testName","Test")
        self.ExtraCredit= kwargs.get("ExtraCredit",False) 
        self.OutOf      = kwargs.get("OutOf", 0)
        if self.OutOf==0:self.OutOf=self.parent.ECTestGrade if self.ExtraCredit else self.parent.TestGrade
        
        self.UserInput  = []
        self.MemInputs=[]
        self.RegInputs=[]
        self.Output=[]
    def AddPromptRegex(self,**kwargs):
        self.PromptRegex.append(kwargs.get("PromptRegex") )
    def AddUserInput(self, **kwargs):
        self.UserInput.append(kwargs.get("UserInput") )
    def AddMemInput(self, **kwargs):
        reg=kwargs.get("reg",None)
        if reg is not None:
            reg=self.__RegInput__(reg=kwargs.get('reg'), value=kwargs.get('addr'),memPointer=True)
            self.RegInputs.append(reg)
            kwargs['reg']=reg

        self.MemInputs.append(self.__MemInput__(**kwargs))
    def AddRegInput(self, **kwargs):
        self.RegInputs.append(self.__RegInput__(**kwargs))
    def AddOutput(self, **kwargs):
        self.Output.append(self.__Output__(**kwargs))

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
            if self.reg is not None: 
                d["reg"]=self.reg.reg.replace("$","")
            return d
    
    class __Output__:
        def __init__(self,type,CorrectAnswer,reg=None,addr=None):
            if reg is None and addr is None: raise Exception("reg or addr must be given a value")
            if reg is not None: self.reg = '$'+reg.replace('$','')
            else:self.reg=reg
            self.type = type
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
                

if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0])) # ensures proper initial directory
    tt = settings("settings.json")
    d=tt.ToDict()
    j=json.dumps(d,indent=4)
    print(j)


class settingsWorker(QObject):
    finished    = pyqtSignal(object)
    def __init__(self, file=None, **kwargs):
        super().__init__()
        self.file=file
        self.kwargs=kwargs
    def get(self):
        self.settings=settings(file=self.file,**self.kwargs)
        self.finished.emit(self.settings)
    def getJSON(self):
        self.settings=settings(file=self.file,**self.kwargs)
        self.finished.emit(json.dumps(self.settings.ToDict()))