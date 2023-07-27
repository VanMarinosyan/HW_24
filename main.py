import math
import datetime

# HW_1________________________________________________________________

def sector_area(r, alpha):
    angle_radians = math.radians(alpha)
    area = (math.pi * r ** 2) * angle_radians / (2 * math.pi)
    print(r, alpha, area)
radius = 5
angle_degrees = 60
sector_area(radius, angle_degrees)

# HW_2__________________________________________________________________

def get_day_of_week(year, month, day):
    try:
        date_object = datetime.date(year, month, day)
        day_of_week = date_object.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_name = days[day_of_week]

        print(f"The day of the week for {year}-{month:02d}-{day:02d} is {day_name}.")
    except ValueError:
        print("Invalid date.")

year = 2023
month = 7
day = 27
get_day_of_week(year, month, day)

# HW_3_______________________________________________________________________

def arabic_to_roman(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer greater than 0.")

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral

try:
    number = int(input("Enter an Arabic natural number (greater than 0): "))
    roman_numeral = arabic_to_roman(number)
    print(f"The Roman numeral equivalent of {number} is: {roman_numeral}")
except ValueError:
    print("Invalid input. Please enter a positive integer greater than 0.")

