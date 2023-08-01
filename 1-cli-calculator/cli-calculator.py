# cli calculator in python
# prompts user for input and performs calculation repeatedly until user quits with 'q'
# supports +, -, *, /, and ^ operators
# input should be of the form 'number operator number'
# whitespace is ignored
# handles errors gracefully

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponentiate(a, b):
    return a ** b

def get_input():
    parts = input("Enter an equation or 'q' to quit: ")
    if parts == 'q':
        return 'q'
    else:
        parts = parts.replace(' ', '')
        operator = parts.strip('0123456789.')
        operands = parts.split('+-*/^')
        if len(parts) != 2:
            print("Invalid input. Please try again.")
            return get_input()
        else:
            return [float(operands[0]), operator, float(operands[1])]

def run():
    while True:
        input = get_input()
        if input == 'q':
            break
        else:
            if input[1] == '+':
                print(add(input[0], input[2]))
            elif input[1] == '-':
                print(subtract(input[0], input[2]))
            elif input[1] == '*':
                print(multiply(input[0], input[2]))
            elif input[1] == '/':
                print(divide(input[0], input[2]))
            elif input[1] == '^':
                print(exponentiate(input[0], input[2]))
            else:
                print("Invalid input. Please try again.")

run()
