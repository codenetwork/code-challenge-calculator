# cli calculator in python
# first prompts the user for the type of calculation they want to perform, or press 'q' to quit
# then to provide the operands
# supports the following operations:
# add two numbers
# subtract two numbers
# multiply two numbers
# divide two numbers
# calculate one number to the power of another
# handles errors gracefully
# does not use any functions
# repeats indefinitely until user inputs 'q' to quit

import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    else:
        return a / b

def exponentiate(a, b):
    return a ** b

def main():
    # list user options and get input in the form of the option number
    while True:
        selected_option = input("Select an option or enter 'q' to quit:\n\n1. Add two numbers\n2. Subtract two numbers\n3. Multiply two numbers\n4. Divide two numbers\n5. Calculate one number to the power of another\n\nYour choice: ")
        # if the user selects 'q', quit
        if selected_option == 'q':
            print('Thanks for playing! :)')
            break
        # otherwise, prompt the user for the operands
        else:
            if selected_option not in ['1', '2', '3', '4', '5']:
                print("Invalid option. Please try again.")
                continue
            first_operand = input("Enter the first number: ")
            second_operand = input("Enter the second number: ")
            # if the operands are both numeric, convert them to floats
            if first_operand.isnumeric() and second_operand.isnumeric():
                first_operand = int(first_operand)
                second_operand = int(second_operand)
                # perform the selected operation
                if selected_option == '1':
                    print(add(first_operand, second_operand))
                elif selected_option == '2':
                    print(subtract(first_operand, second_operand))
                elif selected_option == '3':
                    print(multiply(first_operand, second_operand))
                elif selected_option == '4':
                    try:
                        print(divide(first_operand, second_operand))
                    except ZeroDivisionError as e:
                        print("Error:", e)
                elif selected_option == '5':
                    print(exponentiate(first_operand, second_operand))
            else:
                print("Invalid input. Please try again.")

main()


        