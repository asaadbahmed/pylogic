def LOGICAL_AND(a, b):
    return a == 1 and b == 1

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
    isEqual(True, LOGICAL_AND(1, 1), "LOGICAL_AND (both 1)")
    isEqual(False, LOGICAL_AND(1, 0), "LOGICAL_AND (both 0)")
    isEqual(0, LOGICAL_NOT(1), "LOGICAL_NOT (1 -> 0)")
    isEqual(1, LOGICAL_NOT(0), "LOGICAL_NOT (0 -> 1)")
    
run_tests()