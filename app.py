import operations

# wrapper of the built-in bin function to get rid of the b0 prefix
def binWithoutPrefix(integer):
    return bin(integer)[2:]

def main():
    # operations = ["AND (&)", "NAND (!&)", "OR (+)", "NOR (!+)", "XOR (^)", "XNOR (!^)", "NOT (!)", "ADD (++)", "SUB (--)", "MUL (**)", "DIV (//)"]
    symbols = set({"&", "!&", "+", "!+", "^", "!^", "!", "++", "--", "**", "//"})
    operationMap = {
        "AND": "&",
        "NAND": "!&",
        "OR": "+",
        "NOR": "!+",
        "XOR": "^",
        "XNOR": "!^",
        "NOT": "!",
        "ADD": "++",
        "SUB": "--",
        "MUL": "**",
        "DIV": "//",
    }

    print("List of Operations:")
    for op, symbol in operationMap.items():
        print(f"{op} ({symbol})")

    choice = input("Enter the desired operation: ")
    op = None

    # two cases: the choice was in alphabetical format, or symbol format, either way, we want the alphabetical format
    if choice.isalpha():
        choice = operationMap.get(choice.upper())
    
    if choice and choice in symbols:
        for key, val in operationMap.items():
            if val == choice:
                op = key
                break            

    if not op:
        print("Invalid operation.")
        return 0

    # since NOT only takes one parameter, we only prompt once
    inputs = []
    if op == "NOT":
        inputs.append(int(input("Input a bit: "), 2))
    else:
        inputs.append(int(input("Input a bit: "), 2))
        inputs.append(int(input("Input a bit: "), 2))

    func = getattr(operations, op) # since operations.py contains raw-functions, and not a dictionary of them, we have to access it like this
    result = None # func(*inputs)

    try:
        result = func(*inputs)
    except:
        raise Exception("Something went wrong. Did you provide the correct number of arguments? If so, the issue may lie with the operator function itself.")
    else:        
        expression = binWithoutPrefix(inputs[0]) # initialize the expression with the first input, so it doesn't have whitespace in the start
        for i in inputs[1:]: # skip the first index since the expression is initialized with it
            expression += " " + op + " " + binWithoutPrefix(i)
        print(f"{expression} => {binWithoutPrefix(result)}")
    finally:
        print("Successfully executed.")
        return 0

main()