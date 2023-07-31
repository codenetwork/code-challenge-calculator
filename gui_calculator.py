from tkinter import *
from tkinter.ttk import Radiobutton, Style

# Back end

# Front end
# Set up calculator window
calc_window = Tk()
calc_window.title("Smart Calculator")

margin = 5
operator = StringVar()

display_section = Frame(calc_window, width=320,
                        height=100, background="black")
display_section.grid(row=0, column=0, columnspan=4, sticky="NEWS")

# First row
clear_button = Button(calc_window, width=10, height=3,
                      text="C", background="gray").grid(row=1, column=0)

plus_minus_button = Button(calc_window, width=10, height=3,
                           text="+/-", background="gray").grid(row=1, column=1)

percent_button = Button(calc_window, width=10, height=3,
                        text="%", background="gray").grid(row=1, column=2)

divide_button = Button(calc_window, width=10, height=3,
                       text="÷", background="gray", ).grid(row=1, column=3)

# Second row
seven_button = Button(calc_window, width=10, height=3,
                      text="7", background="gray").grid(row=2, column=0)

eight_button = Button(calc_window, width=10, height=3,
                      text="8", background="gray").grid(row=2, column=1)

nine_button = Button(calc_window, width=10, height=3,
                     text="9", background="gray").grid(row=2, column=2)

multiply_button = Button(calc_window, width=10, height=3,
                         text="x", background="gray").grid(row=2, column=3)

# Third row
four_button = Button(calc_window, width=10, height=3,
                     text="4", background="gray").grid(row=3, column=0)

five_button = Button(calc_window, width=10, height=3,
                     text="5", background="gray").grid(row=3, column=1)

six_button = Button(calc_window, width=10, height=3,
                    text="6", background="gray").grid(row=3, column=2)

minus_button = Button(calc_window, width=10, height=3,
                      text="-", background="gray").grid(row=3, column=3)

# Forth row
one_button = Button(calc_window, width=10, height=3,
                    text="1", background="gray").grid(row=4, column=0)

two_button = Button(calc_window, width=10, height=3,
                    text="2", background="gray").grid(row=4, column=1)

three_button = Button(calc_window, width=10, height=3,
                      text="3", background="gray").grid(row=4, column=2)

plus_button = Button(calc_window, width=10, height=3,
                     text="+", background="gray").grid(row=4, column=3)

# Five row
zero_button = Button(calc_window, width=10, height=3,
                     text="0", background="gray").grid(row=5, column=0, columnspan=2, sticky="WE")

dot_button = Button(calc_window, width=10, height=3,
                    text=".", background="gray").grid(row=5, column=2)

equal_button = Button(calc_window, width=10, height=3,
                      text="=", background="gray").grid(row=5, column=3)


# Lock window resizef
calc_window.resizable(0, 0)

# Start the event loop
calc_window.mainloop()
