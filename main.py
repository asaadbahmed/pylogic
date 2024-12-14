import gates
# TODO - add expression evaluating & minimizing (convert to NANDS using DeMorgans for least possible transistors)

def HANDLE_GATE(a, b, gates):
    print("Choose a logic gate. The not gate only applies to the first bit you input.\nGate\t\tSymbol\tDescription")
    for info in gates:
        print(f"{info["name"]}\t\t[{info["symbol"]}]\t{info["desc"]}")
    
    choice = input("Choose: ").upper()
    result = 0

    match choice:
        case "AND" | "&":
            result = gates.LOGICAL_AND(a, b)
        case "NAND" | "!&" :
            result = gates.LOGICAL_NAND(a, b)
        case "OR" | "+":
            result = gates.LOGICAL_OR(a, b)
        case "NOR" | "!+":
            result = gates.LOGICAL_NOR(a, b)
        case "XOR" | "^":
            result = gates.LOGICAL_XOR(a, b)
        case "XNOR" | "!^":
            result = gates.LOGICAL_XNOR(a, b)
        case "NOT" | "!":
            result = gates.LOGICAL_NOT(a)
        case _:
            result = None
            raise RuntimeError("Gate does not exist!")
            
    print("Gate Result: " + str(result))

def HANDLE_TRUTH_TABLE():
    print("Binary\tDecimal")
    for i in range(8):
        print(f"\t{i}")

    for i in range(7, -1, -1):
        print(f"\t-{i}")

def HANDLE_OPERATION(a, b, ops):
    print(123)

def main():
    gates = [
        {"symbol": "&",  "name": "AND", "desc": "A & B"},
        {"symbol": "!&",  "name": "NAND", "desc": "!(A & B)"},

        {"symbol": "+", "name": "OR", "desc": "A + B"},
        {"symbol": "+", "name": "NOR", "desc": "!(A + B)"},

        {"symbol": "^", "name": "XOR", "desc": "A ^ B"},
        {"symbol": "^", "name": "XNOR", "desc": "!(A ^ B)"},

        {"symbol": "!", "name": "NOT", "desc": "!A"},        
    ]

    operations = [
        {"symbol": "ADD", "name": "ADD", "desc": "Adds two bits (4 bit signed)."}
    ]

    a = int(input("Input a 4 bit signed binary value: "), 2)
    b = int(input("Input another 4 bit signed binary value: "), 2)
    choice = input("Would you like to run an operation, gate, or view the truth table? Type \"op\" or \"gate\" or \"tt\": ")
    
    match choice:
        case "gate":
            HANDLE_GATE(a, b, gates)
        case "op":
            HANDLE_OPERATION(a, b, operations)
        case "tt":
            HANDLE_TRUTH_TABLE()
        case _:
            raise RuntimeError("Invalid choice!")
    

main()