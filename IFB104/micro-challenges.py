# Program to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

# Program to calculate the area of a rectangle given its length and width.
def area_of_rectangle():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(area)

# Program to calculate the volume of a cube given its side length.
def volume_of_cube():
    side_length = float(input("Enter side length: "))
    volume = side_length ** 3
    print(volume)

# Program to calculate the sum of the first 'n' natural numbers.
def sum_of_natural_numbers():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)

# Program to check if a given number is even or odd.
def even_or_odd():
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Program to find the maximum of two given numbers.
def maximum_of_two_numbers():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    if a > b:
        print(a)
    else:
        print(b)

# Program to calculate the factorial of a non-negative integer. 8. Program to calculate the average of three given numbers.
def average_of_three_numbers():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    average = (a + b + c) / 3
    print(average)

# Program to determine if a given year is a leap year or not.
def leap_year():
    year = int(input("Enter year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")

# Program to convert a given number of minutes into hours and minutes.
def minutes_to_hours_and_minutes():
    minutes = int(input("Enter minutes: "))
    hours = minutes // 60
    minutes = minutes % 60
    print(hours, "hours and", minutes, "minutes")