def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def NAND(a, b):
    return ~(a & b) & 1

def NOR(a, b):
    return ~(a | b) & 1

def XNOR(a, b):
    return ~(a ^ b) & 1

def NOT(a):
    return 1 - a

# Implement ADD, SUB, DIV, MUL