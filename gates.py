def LOGICAL_AND(a, b):
    return a & b

def LOGICAL_OR(a, b):
    return a | b

def LOGICAL_XOR(a, b):
    return a ^ b

def LOGICAL_NAND(a, b):
    return ~(a & b) & 1

def LOGICAL_NOR(a, b):
    return ~(a | b) & 1

def LOGICAL_XNOR(a, b):
    return ~(a ^ b) & 1

def LOGICAL_NOT(a):
    return 1 - a