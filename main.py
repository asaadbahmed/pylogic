RUN_TESTS = False

def LOGICAL_AND(a, b):
    return a & b

def LOGICAL_XOR(a, b):
    #if a == 1 and b == 0
    if a & (not b):
        return 1
    elif (not a) & b:
        return 1
    else:
        return 0

def LOGICAL_OR(a, b):
    return a | b

def LOGICAL_NOT(a):
    return abs(a - 1)
    
def is_equal(expected, actual, test):
    if (expected == actual or expected is actual):
        print("Test passed: " + test)
    else:
        print("Test failed: " + test)

def run_tests():
    is_equal(1, LOGICAL_AND(1, 1), "LOGICAL_AND (both 1)")
    is_equal(0, LOGICAL_AND(1, 0), "LOGICAL_AND (both 0)")
    
    is_equal(1, LOGICAL_OR(1, 0), "LOGICAL_OR (one is true)")
    is_equal(0, LOGICAL_OR(0, 0), "LOGICAL_OR (both are false)")

    is_equal(0, LOGICAL_XOR(1, 1), "LOGICAL_XOR (both are true)")
    is_equal(0, LOGICAL_XOR(0, 0), "LOGICAL_XOR (both are false)")
    is_equal(1, LOGICAL_XOR(1, 0), "LOGICAL_XOR (one is true)")

    is_equal(0, LOGICAL_NOT(1), "LOGICAL_NOT (1 -> 0)")
    is_equal(1, LOGICAL_NOT(0), "LOGICAL_NOT (0 -> 1)")
    
def main():
    valid_symbols = set({'1', '0', '&', '+', '!', '^', '(', ')', ' '})
    gates = [
        {"symbol": "&",  "name": "AND", "desc": "A & B", "func": LOGICAL_AND},
        {"symbol": "+", "name": "OR", "desc": "A + B", "func": LOGICAL_OR},
        {"symbol": "!", "name": "NOT", "desc": "!A", "func": LOGICAL_NOT},
        {"symbol": "^", "name": "XOR", "desc": "A ^ B", "func": LOGICAL_XOR},
    ]

    a = int(input("Input a bit: "), 2)
    b = int(input("Input another bit: "), 2)

    print("Choose a logic gate.\nGate\t\tSymbol\tDescription")
    for info in gates:
        print(f"{info["name"]}\t\t[{info["symbol"]}]\t{info["desc"]}")
    
    choice = input("Choose: ").upper()
    for gateInfo in gates:
        if gateInfo["name"] == choice:
            print("Result: " + str(gateInfo["func"](a, b)))
            break

if RUN_TESTS:
    run_tests()
else:
    main()