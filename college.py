def main():
    print(fahrenheit_coverter(0))
    print(celcius_converter(32))
    print(area_of_triangle(18, 10, 14))


# Python program to convert the temperature in degree centigrade to Fahrenheit


def fahrenheit_coverter(celcius):
    return (celcius * (9 / 5)) + 32


# Python program to convert the temperature in degree centigrade to Fahrenheit


def celcius_converter(temp):
    return (temp - 32) * (5 / 9)


# Python program to find the area of a triangle whose sides are given


def area_of_triangle(a, b, c):
    first = (a + b + c) / 2
    process = first * (first - a) * (first - b) * (first - c)
    return (process) ** (1 / 2)


# write a python program to find the circumference and area with a given radius


def circum_area(radius):
    finding_area = 2 * 3.14 * radius
    finding_ciucum = 3.14 * radius * radius
    print(f"The area of the circle formed from the radius {radius} is {finding_area}")
    print(
        f"The circumference of the circle formed from the radius {radius} is {finding_ciucum}"
    )


# find the geometric mean of n numbers


def geometric_mean():
    pre = []
    asking = int(input("How much numbers you are expecting to add:  "))
    for i in range(asking):
        pre.append(int(input("Enter the numbers:  ")))
    print(multiplying_list(pre) ** (1 / asking))


# Multiplication of list using the for Loop


def multiplying_list(anylist):
    count = 1
    for j in anylist:
        count = count * j
    return count


# Addition of list using the for Loop


def adding_list(anylist):
    count = 0
    for j in anylist:
        count = count + j
    return count


#  Python program to display the sum of n numbers using a list


def sum_using_list():
    anylist = []
    asking = int(input("Enter the Numbers you want to add:  "))
    for i in range(asking):
        anylist.append(int(input("Enter the Numbers:  ")))
    print(adding_list(anylist))


# Python program to fnd out the average of a set of integers


def average():
    empty_list = []
    asking = int(
        input("Enter the Number of elements you want to find the average of:  ")
    )
    for i in range(asking):
        empty_list.append(int(input("Enter the Numbers of the set:  ")))
    print(sum(empty_list) // asking)


# finding the number that it's even or odd:


def even_odd(number):
    if number == 0:
        print(f"{number} is Neither Odd nor Even.")
    elif number % 2 == 0:
        print(f"{number} is a Even Number.")
    else:
        print(f"{number} is an Odd Number.")


# Taking proper intiger input


def taking_input_inlist():
    empty_list = []
    elements_number = int(input("How Many Number you want to Calculate:  "))
    for i in range(elements_number):
        empty_list.append(int(input("Enter the Numbers:  ")))


# find the product of set of real numbers


def real_multiplication():
    empty_list = []
    elements_number = int(input("Enter the Numbers you want to calculate:  "))
    for i in range(elements_number):
        empty_list.append(int(input("Enter the Numbers:")))
    print(multiplying_list(empty_list))


# To check weathere a number is a multiple of 5 or not


def multiple_5():
    asking = int(input("Enter the Number you want to check:  "))
    if asking % 5 == 0:
        print(f"{asking} is a Multiple of 5.")
    else:
        print(f"{asking} is not a Multiple of 5.")


# Checking weather the number is the multiple of both 5 and 7 .


def multiple_5_7():
    asking = int(input("Enter the Number you want to check:  "))
    if asking % 5 == 0 and asking % 7 == 0:
        print(f"{asking} is the Multiple of both 5 and 7.")
    else:
        print(f"{asking} is not the Multiple of both 5 and 7.")


# finding the average of numbers using the while loop


def average_WhileLoop():
    asking = int(input("For how many Numbers Do you want to find the average of:  "))
    empty_list = []
    count = 0
    while True:
        empty_list.append(int(input("Enter the Numbers:  ")))
        count += 1
        if count == asking:
            break
    print(f"The average of Your Data is {sum(empty_list)//asking}.")



# Testing for prime Numbers


def prime_orNot():
    asking = int(input("Eneter the Number:  "))

    count = False
    if asking == 1:
        print(f"{asking} is not a Prime Number.")
    elif asking > 2:
        for i in range(2, asking):
            if asking % i == 0:
                count = True
                break
    if count == True:
        print(f"{asking} is not a Prime Number.")
    else:
        print(f"{asking} is a Prime Number.")



# To find the largest Number in a list without using the Built in functions
        

def largest_number():
    asking = int(input("Enter the Numbers of Elements of the list:  "))
    anylist = []
    flag = True
    count = 0
    negative = []
    for i in range(asking):
        anylist.append(int(input("Enter the Numbers:  ")))
        for j in anylist:
            if j > count:
                count = j
                flag = False
            elif (-j) < negative:
                negative =  j
            
    if flag == True:
        return f"{negative} is the Largest Number of the List."    
    else:
        return f"{count} is the largest in the list."
    

# write a python program to insert element at any position in the list
    
def insert_in_list():
    asking = int(input("Enter the Numbers of Elements of the list:  "))
    anylist = []
    flag = True
    count = 0
    negative = 0
    for i in range(asking):
        anylist.append(int(input("Enter the Numbers:  ")))
    print(anylist)
    modify = input("If you want to modify the list press ('m') or else ('n')")
    work = input("What do you want to do: Add(a), Remove(r)  ")
    if modify == "m":
        if work == "a":
            element = int(input("What do you want to Add:  "))
            position = int(input("At what position in the List you want to Insert the Number:  "))
            anylist.insert((position - 1), element)
            print(anylist)
        elif work == "r":
            pass


# checking a string is a palidrome or not
        
def palidrome_orNot(statement):
    anylist = []
    opp_anylist =[]
    for i in statement:
        anylist.append(i)
    for j in reversed(anylist):
        opp_anylist.append(j)

    if anylist == opp_anylist:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Finding the given year is a Leap year no Not
        


def leap_year():
    year = int(input("Enter the YeaR:  "))
    if year % 400:
        if year % 4 == 0 and year % 100 != 0 :
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else:
        print(f"{year} is not Leap Year.")


if __name__ == "__main__":
    main()
