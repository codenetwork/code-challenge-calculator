from tkinter import *
from tkinter.ttk import Style

# Back end
expression = ""


def add_expression(item):
    global expression
    expression = expression + str(item)
    display.delete(0.0, END)
    display.insert(END, expression)


def clear_display():
    global expression
    expression = ""
    display.delete(0.0, END)
    display.insert(END, "")


def calculate():
    global expression
    try:
        expression = str(eval(expression))
        print(expression)
        display.delete(0.0, END)
        display.insert(END, expression)
    except ZeroDivisionError:
        display.delete(0.0, END)
        display.insert(END, "Undefined")
    except:
        print(expression)
        display.delete(0.0, END)
        display.insert(END, "Error")


# Front end
# Set up calculator window
calc_window = Tk()
calc_window.title("Smart Calculator")

# Declare necessary variables
margin = 5
operator = StringVar()
text_font = ('TkTextFont', 20)

display = Text(
    calc_window,
    width=18,
    height=2,
    font=text_font,
    background="black",
    foreground="white",
    insertbackground='white')
display.grid(row=0, column=0, columnspan=4, sticky="NEWS", padx=5, pady=2)

# First row
clear_btn = Button(calc_window, width=10, height=3,
                   text="C", background="gray", command=clear_display)
clear_btn.grid(row=1, column=0, columnspan=2, sticky="WE")


percent_btn = Button(calc_window, width=10, height=3,
                     text="%", background="gray", command=lambda: add_expression("%"))
percent_btn.grid(row=1, column=2)

divide_btn = Button(calc_window, width=10, height=3,
                    text="÷", background="gray", command=lambda: add_expression("/"))
divide_btn.grid(row=1, column=3)

# Second row
seven_btn = Button(calc_window, width=10, height=3,
                   text="7", background="gray", command=lambda: add_expression("7"))
seven_btn.grid(row=2, column=0)

eight_btn = Button(calc_window, width=10, height=3,
                   text="8", background="gray", command=lambda: add_expression("8"))
eight_btn.grid(row=2, column=1)

nine_btn = Button(calc_window, width=10, height=3,
                  text="9", background="gray", command=lambda: add_expression("9"))
nine_btn.grid(row=2, column=2)

multiply_btn = Button(calc_window, width=10, height=3,
                      text="x", background="gray", command=lambda: add_expression("*"))
multiply_btn.grid(row=2, column=3)

# Third row
four_btn = Button(calc_window, width=10, height=3,
                  text="4", background="gray", command=lambda: add_expression("4"))
four_btn.grid(row=3, column=0)

five_btn = Button(calc_window, width=10, height=3,
                  text="5", background="gray", command=lambda: add_expression("5"))
five_btn.grid(row=3, column=1)

six_btn = Button(calc_window, width=10, height=3,
                 text="6", background="gray", command=lambda: add_expression("6"))
six_btn.grid(row=3, column=2)

minus_btn = Button(calc_window, width=10, height=3,
                   text="-", background="gray", command=lambda: add_expression("-"))
minus_btn.grid(row=3, column=3)

# Forth row
one_btn = Button(calc_window, width=10, height=3,
                 text="1", background="gray", command=lambda: add_expression("1"))
one_btn.grid(row=4, column=0)

two_btn = Button(calc_window, width=10, height=3,
                 text="2", background="gray", command=lambda: add_expression("2"))
two_btn.grid(row=4, column=1)

three_btn = Button(calc_window, width=10, height=3,
                   text="3", background="gray", command=lambda: add_expression("3"))
three_btn.grid(row=4, column=2)

plus_btn = Button(calc_window, width=10, height=3,
                  text="+", background="gray", command=lambda: add_expression("+"))
plus_btn.grid(row=4, column=3)

# Fifth row
zero_btn = Button(calc_window, width=10, height=3,
                  text="0", background="gray", command=lambda: add_expression("0"))
zero_btn.grid(row=5, column=0, columnspan=2, sticky="WE")

decimal_btn = Button(calc_window, width=10, height=3,
                     text=".", background="gray", command=lambda: add_expression("."))
decimal_btn.grid(row=5, column=2)

equal_btn = Button(calc_window, width=10, height=3,
                   text="=", background="gray", command=calculate)
equal_btn.grid(row=5, column=3)


# Lock window resizef
# calc_window.resizable(0, 0)

# Start the event loop
calc_window.mainloop()
