# cli calculator in python
# prompts user for input and performs calculation repeatedly until user quits with 'q'
# supports +, -, *, /, and ^ operators
# input should be of the form 'number operator number'
# whitespace is ignored
# handles errors gracefully

import re

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
        # split the input into two parts, the operands and the operator
        parts = re.split('(\+|\-|\*|\/|\^)', parts)
        # remove whitespace
        parts = [part.strip() for part in parts]
        # remove empty strings
        parts = [part for part in parts if part != '']
        # if there are more than two parts, the input is invalid
        if len(parts) == 3 and parts[0].isnumeric() and parts[2].isnumeric():
            # if the operands are both numeric, convert them to floats
            return [float(parts[0]), parts[1], float(parts[2])]
        else:
            # otherwise, the input is invalid
            print("Invalid input. Please try again.")
            return get_input()

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
                print("Invalid operator. Please try again.")

run()
