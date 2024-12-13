def LOGICAL_AND(a, b):
    return a == 1 and b == 1

def LOGICAL_XOR(a, b):
    if a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 1
    else:
        return 0

def LOGICAL_OR(a, b):
    return a == 1 or b == 1

def LOGICAL_NOT(a):
    if a == 1:
        return 0
    elif a == 0:
        return 1

def isEqual(expected, actual, test):
    if (expected == actual):
        print("Test passed: " + test)
    else:
        print("Test failed: " + test)

def run_tests():
    isEqual(1, LOGICAL_AND(1, 1), "LOGICAL_AND (both 1)")
    isEqual(0, LOGICAL_AND(1, 0), "LOGICAL_AND (both 0)")
    
    isEqual(1, LOGICAL_OR(1, 0), "LOGICAL_OR (one is true)")
    isEqual(0, LOGICAL_OR(0, 0), "LOGICAL_OR (both are false)")

    isEqual(0, LOGICAL_XOR(1, 1), "LOGICAL_XOR (both are true)")
    isEqual(0, LOGICAL_XOR(0, 0), "LOGICAL_XOR (both are false)")
    isEqual(1, LOGICAL_XOR(1, 0), "LOGICAL_XOR (one is true)")

    isEqual(0, LOGICAL_NOT(1), "LOGICAL_NOT (1 -> 0)")
    isEqual(1, LOGICAL_NOT(0), "LOGICAL_NOT (0 -> 1)")
    
run_tests()