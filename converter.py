#  fahrenheit to celsius =(32°F − 32) × 5/9 = 0°C
# celsius to fahrenheit = (32°F − 32) × 5/9 = 0°C

# inch to centimeter = multiply the length value by 2.54
# centimeter to ince = divide the length value by 2.54

import sys
from pyfiglet import figlet_format as textEnhancer

def fahrenheit_celcius(some_temp):
    return (f"The fahrenheit conversion of the {some_temp} is {(some_temp - 32) * (5/9)}°C")

def celsius_fahrenheit(some_temp):
    return (f"The celcius conversion of the {some_temp} is {(some_temp * 9/5) + 32}°F")

def inch_centimeter(measurement):
    return (f"The Inch conversion of the {measurement} is {measurement*2.54}cm .")

def centimeter_inch(measurement):
    return (f"The centimeter conversion of {measurement} is {measurement/2.54} inches")

user_options = ["a", "b", "c", "d"]

project = textEnhancer("Mathematical Converter")
print(project)


print("What you want to use:   ")

print("(a)  Fahrenheit to celsius converter.")
print("(b)  Celcius to fahrenheit converter.")
print("(c)  Inches to centimeter converter.")
print("(d)  Centimeter to inches converter.")


user = input("Choose between (a), (b), (c), (d)  : ")


for i in user_options:
    if user in user_options:
        if user == "a":
            tem = float(input("Enter the temperature in fahrenheit without the '°F' symbol:  "))
            sys.exit(fahrenheit_celcius(tem))
        elif user =="b":
            tem = float(input("Enter the temperature in celcius without the '°C' symbol:  "))
            sys.exit(celsius_fahrenheit(tem))
        elif user == "c":
            meas = float(input("Enter the measurement in Inches:  "))
            sys.exit(inch_centimeter(meas))
        elif user == "d":
            meas = float(input("Enter the measuremnet in the Centimeter:  "))
            sys.exit(centimeter_inch(meas))

    else:
        print("\n Seems like you have Choosen the wrong option, please choose the correct one: \n")
        user = input("Choose between (a), (b), (c), (d)  : ")
    







