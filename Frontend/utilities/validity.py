from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


addressRegex=QRegExp("^((0[xX][a-fA-F0-9]{0,8})|([-+]?[0-9]{0,10}))$")
registerRegex=QRegExp("^\$?(at|v0?1?|a[0123]|t[0-9]|s[0-7]|gp|sp|fp|ra|f?([0-2]?[0-9]|3[0-1]))$")
byteRegex=QRegExp("^((0[xX][[0-9a-fA-F]{1,2})|(\+?([0-1]?[0-9]{1,2}|2([0-4][0-9]|5[0-5])))|(-(0?[[0-9]{0,2}|1([0-1][0-9]|2[0-8]))))$")
wordRegex=QRegExp("^(0[xX][[0-9a-fA-F]{1,8}|[+-]?[0-9]{0,10})$")
asciiRegex=QRegExp(".*")
addressRegexValidator=QRegExpValidator(addressRegex)
registerRegexValidator=QRegExpValidator(registerRegex)
byteRegexValidator=QRegExpValidator(byteRegex)
wordRegexValidator=QRegExpValidator(wordRegex)
asciiRegexValidator=QRegExpValidator(wordRegex)
def isReg(reg):
    return 

def isInt(var):
    try:
        int(var)
        return True
    except:
        return False

def isHex(var:str):
    try: 
        int(var) # Hex strings need the ',0' for casting to work
        return False
    except:pass
    try:
        int(var,0)
        return True
    except:
        return False

'''
ensure the value fits in 32bits
'''
def validRegisterValue(var:str):
    minV=-2147483648
    maxV=4294967295
    if isHex(var) or isInt(var):
        var=int(var,0)
        return (minV<=var) and (var<=maxV)



legalAddresses = [("0x10000000","0x10008000"),("0x10010000,0x10040000"),("0x90000300,0x90010000")]
def validAddress(var:str):
    if validRegisterValue:
        for minA,maxA in legalAddresses:
            addr=int(var,0)
            minA=int(minA,0)
            maxA=int(maxA,0)
            if (minA<=addr) and (addr<maxA): return True
    return False

            
