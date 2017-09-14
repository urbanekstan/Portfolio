#  File: Day.py

#  Description: Given the day, month, and year within a 2 century period
#		(1900-2100 incl.), the program returns the day of the week.

#  Student Name: Stanley Urbanek	

#  Student UT EID: su964

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: 7/2/2014

#  Date Last Modified: 7/3/2014

#########################################


def main():
  #check year
    year = eval(input('Enter year: '))
    while ( (year < 1900) or (year > 2100)):
      year = eval(input('Enter year: '))
  #check month
    month = eval(input('Enter month: '))
    while ( (month < 1) or (month > 12)):
      month = eval(input('Enter month: '))
  #get day
    day = eval(input('Enter day: '))
  #check validity of day, depending on month
  ##first with 31 day months
    if ( (month == 1) or (month == 3) or (month == 5) or\
    (month == 7) or (month == 8) or (month == 10) or (month == 12)):
      while ( (day < 1) or (day > 31)):
        day = eval(input('Enter day: '))
  ##now with 30 day months
    elif ( (month == 4) or (month == 6) or (month == 9) or (month == 11)):
      while ( (day < 1) or (day > 30)):
        day = eval(input('Enter day: '))
  ##now check if february is a leap year
    elif ( (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)) ):
      while ( (day < 1) or (day > 29) ):
        day = eval(input('Enter day: '))
    else:
      while ( (day < 1) or (day > 28) ):
        day = eval(input('Enter day: '))
  #changing calendar months (and year if necessary) for algorithm
    a = month - 2
    if (a < 1):
      a += 12
      year -= 1
    else:
      pass
  ##assigning rest of variables for algorithm
    b = day
  ##splitting year into two variables, c and d
    d = year // 100
    c = year - d * 100
  #now doing Rev. Zeller's algorithm
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7
  #converting r into day of the week, and printing result
    if (r == 0):
      print('\nThe day is Sunday.')
    elif (r == 1):
      print('\nThe day is Monday.')
    elif (r == 2):
      print('\nThe day is Tuesday.')
    elif (r == 3):
      print('\nThe day is Wednesday.')
    elif (r == 4):
      print('\nThe day is Thursday.')
    elif (r == 5):
      print('\nThe day is Friday.')
    else:
      print('\nThe day is Saturday.')


main()


