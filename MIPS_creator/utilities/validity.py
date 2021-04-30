

validRegisters=[
        'at',
        'v0','v1',
        'a0','a1','a2','a3',
        't0','t1','t2','t3','t4','t5','t6','t7','t8','t9'
        's0','s1','s2','s3','s4','s5','s6','s7',
        'gp','sp','fp','ra',
        '1','2','3','3','5','6','7','8','9','10','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','28','29','30','31'
        'f0','f1','f2','f3','f3','f5','f6','f7','f8','f9','f10','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26','f27','f28','f29','f30','f31'
    ]

def isReg(reg):
    reg=reg.replace('$','')
    return reg in validRegisters

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

            
