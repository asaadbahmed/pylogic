RUN_TESTS = False
BINARY_VALUES = {0, 1}

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

def DECIMAL_TO_BINARY(value):
    if value == 1 or value == 0: return value
    
    binary_values = []
    while value != 0:
        if value % 2 == 0:
            binary_values.append(1)
        else:
            binary_values.append(0)
        value = value // 2

    # since in decimal -> binary conversion, you go from the least significant bit to the most significant bit
    binary_values.reverse()
    print(binary_values)

    return binary_values

def is_equal(expected, actual, test):
    if (expected == actual):
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
    if RUN_TESTS:
        run_tests()

    operations = [
        {"symbol": "&",  "name": "AND", "desc": "A & B"},
        {"symbol": "+", "name": "OR", "desc": "A + B"},
        {"symbol": "!", "name": "NOT", "desc": "!A"},
        {"symbol": "^", "name": "XOR", "desc": "A ^ B"},
    ]

    print("This is a list of the available operations.\nOperation\tSymbol\tDescription")
    for info in operations:
        print(f"{info["name"]}\t\t[{info["symbol"]}]\t{info["desc"]}")
    


main()