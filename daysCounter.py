from pyfiglet import figlet_format
from time import ctime

project = figlet_format("Days Calculator")
print(project)

def takingUserAge():
    for i in range(3):
        birthDate = input("Enter you birth date in the formate like: (dd/mm/yyyy) ---> ")
        try:
            day , month, year = birthDate.split("/")
            return day, month, year
        except:
            print("Incorrect Value.")

def takingCurrentDate():
    currntCondition = ctime()
    # Fri Feb 23 01:30:44 2024 (this is the output formate of the ctime in the form of string)
    curDay, curMonth, curDate, curTime, curYear = currntCondition.split(" ")
    
    monthYear = {
        "jan" : 1,
        "feb" : 2,
        "mar" : 3,
        "apr" : 4,
        "may" : 5,
        "jun" : 6,
        "jul" : 7,
        "aug" : 8,
        "sep" : 9,
        "oct" : 10,
        "nov" : 11, 
        "dec" : 12,
    }
    curMonth = monthYear[curMonth.lower()]

    return curDate, curMonth, curYear

def calCurrentAge(day, month, year, curDate, curMonth, curYear):
    # Converting all the dates into integers
    day = int(day)
    month = int(month)
    year = int(year)
    curDate = int(curDate)
    curMonth = int(curMonth)
    curYear = int(curYear)

    # Calculating the days
    for _ in range(2):
        if day >= curDate:
            ageDate = day - curDate
        else:
            day += 30
            curMonth -= 1

    # Calculating the Months
    for _ in range(2):
        if curMonth >= month:
            ageMonth = curMonth - month
        else:
            curMonth += 12
            curYear -= 1

    # Calculating the year
    ageYear = curYear - year

    # Calculating the days and months accordingly
    if ageDate > 31:
        ageDate = 0
        ageMonth += 1
    elif ageMonth > 12:
        ageMonth = 0
        ageYear += 1

    return ageDate, ageMonth, ageYear
                                                                                    
dateBirth, monthBirth, yearBirth = takingUserAge()
currentDate, currentMonth, currentYear = takingCurrentDate()
ageDay, ageMonth, ageYear = calCurrentAge(dateBirth, monthBirth, yearBirth, currentDate, currentMonth, currentYear)

print(f"You are {ageYear} years {ageMonth} months {ageDay} days old till, {currentDate}/{currentMonth}/{currentYear}")