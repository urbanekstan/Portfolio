#  File: Hailstone.py

#  Description: Given a range of natural numbers, the program determines the 
#               longest cycle to return one, given Collatz's conjecture and procedure.

#  Student Name: Stanley Urbanek

#  Student UT EID: su964

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created:7/8/2014

#  Date Last Modified: 7/8/2014

###########################################

def main():

  #gets range of values and checks validity
  a = eval(input('Enter starting number of the range: '))
  z = eval(input('Enter ending number of the range: '))
  while ( (a <= 0) or (z <= 0) or (a >= z) ):
    a = eval(input('Enter starting number of the range: '))
    z = eval(input('Enter ending number of the range: '))

  #sets initial parameters
  cycleTotal = 0
  mostIter = a
  
  #begins Collatz procedure, with nested loops
  for n in range (a, z+1):
    t = n
    count = 0
    while (n != 1):
      if (n % 2 == 0):
        n = n // 2
      else:
        n = 3 * n + 1
      count += 1
    if (count > cycleTotal):
      mostIter = t
      cycleTotal = count 
    else:
      pass

  #displays end result
  print('The number', mostIter, 'has the longest cycle length of', cycleTotal, '\b.')


main()