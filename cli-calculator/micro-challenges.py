# Ten short programs that take input in the parameters and return the output.
# Each program is followed by unit tests that test the program.

# Program to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# tests
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert celsius_to_fahrenheit(-40) == -40
assert celsius_to_fahrenheit(12) == 53.6

# Program to calculate the area of a rectangle given its length and width.
def area_of_rectangle(length, width):
    return length * width

# tests
assert area_of_rectangle(2, 4) == 8
assert area_of_rectangle(5, 10) == 50
assert area_of_rectangle(3, 3) == 9
assert area_of_rectangle(0, 0) == 0

# Program to calculate the volume of a cube given its side length.
def volume_of_cube(side_length):
    return side_length ** 3

# tests
assert volume_of_cube(2) == 8
assert volume_of_cube(5) == 125
assert volume_of_cube(3) == 27
assert volume_of_cube(0) == 0

# Program to calculate the sum of the first 'n' natural numbers.
def sum_of_natural_numbers(n):
    return n * (n + 1) / 2

# tests
assert sum_of_natural_numbers(5) == 15
assert sum_of_natural_numbers(10) == 55
assert sum_of_natural_numbers(0) == 0
assert sum_of_natural_numbers(100) == 5050

# Program to check if a given number is even or odd.
def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# tests
assert is_even_or_odd(4) == "Even"
assert is_even_or_odd(7) == "Odd"
assert is_even_or_odd(0) == "Even"
assert is_even_or_odd(-5) == "Odd"

# Program to find the maximum of two given numbers.
def max_of_two_numbers(num1, num2):
    return max(num1, num2)

# tests
assert max_of_two_numbers(5, 10) == 10
assert max_of_two_numbers(-3, -10) == -3
assert max_of_two_numbers(0, 0) == 0
assert max_of_two_numbers(100, 1000) == 1000

# Program to calculate the factorial of a non-negative integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# tests
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800

# Program to calculate the average of three given numbers.
def average_of_three_numbers(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# tests
assert average_of_three_numbers(5, 10, 15) == 10
assert average_of_three_numbers(0, 0, 0) == 0
assert average_of_three_numbers(1, 2, 3) == 2
assert average_of_three_numbers(-5, -10, -15) == -10

# Program to determine if a given year is a leap year or not.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
        return False

# tests
assert is_leap_year(2000) == True
assert is_leap_year(2020) == True
assert is_leap_year(2100) == False
assert is_leap_year(2023) == False

# Program to convert a given number of minutes into hours and minutes.
def convert_to_hours_and_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

# tests
assert convert_to_hours_and_minutes(120) == (2, 0)
assert convert_to_hours_and_minutes(135) == (2, 15)
assert convert_to_hours_and_minutes(60) == (1, 0)
assert convert_to_hours_and_minutes(30) == (0, 30)