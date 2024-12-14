RUN_TESTS = False

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
        {"symbol": "&",  "name": "AND", "desc": "A & B"},
        {"symbol": "!&",  "name": "NAND", "desc": "!(A & B)"},

        {"symbol": "+", "name": "OR", "desc": "A + B"},
        {"symbol": "+", "name": "NOR", "desc": "!(A + B)"},

        {"symbol": "^", "name": "XOR", "desc": "A ^ B"},
        {"symbol": "^", "name": "XNOR", "desc": "!(A ^ B)"},

        {"symbol": "!", "name": "NOT", "desc": "!A"},        
    ]

    a = int(input("Input a bit: "), 2)
    b = int(input("Input another bit: "), 2)

    print("Choose a logic gate. The not gate only applies to the first bit you input.\nGate\t\tSymbol\tDescription")
    for info in gates:
        print(f"{info["name"]}\t\t[{info["symbol"]}]\t{info["desc"]}")
    
    choice = input("Choose: ").upper()
    result = 0

    match choice:
        case "AND" | "&":
            result = LOGICAL_AND(a, b)
        case "NAND" | "!&" :
            result = LOGICAL_NAND(a, b)
        case "OR" | "+":
            result = LOGICAL_OR(a, b)
        case "NOR" | "!+":
            result = LOGICAL_NOR(a, b)
        case "XOR" | "^":
            result = LOGICAL_XOR(a, b)
        case "XNOR" | "!^":
            result = LOGICAL_XNOR(a, b)
        case "NOT" | "!":
            result = LOGICAL_NOT(a)
            
    print("Result: " + str(result))
    
if RUN_TESTS:
    run_tests()
else:
    main()