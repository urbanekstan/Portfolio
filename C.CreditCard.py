#  File: CreditCard.py

#  Description: Determines the validity of a given credit card number using Luhn's Test.

#  Student Name: Stanley Urbanek

#  Student UT EID: su964

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: 7/16/2014

#  Date Last Modified: 7/18/2014

#####################################################################

#This function checks if a credit card has the correct number of digits
def is_valid(cc_num):
  if ( (len(str(cc_num)) == 15) or (len(str(cc_num)) == 16) ):
    return False 
    #False because of how it is used in main()
  return True

#This function checks the credit card type
def cc_type(cc_num):
  if ( (cc_num[0:2] == str(34)) or (cc_num[0:2] == str(37)) ):
    return ('American Express')
  elif ( (cc_num[0:4] == str(6011)) or (cc_num[0:3] == str(644)) or (cc_num[0:2] == str(65)) ):
    return ('Discover')
  elif ( (cc_num[0:2] == str(50)) or (cc_num[0:2] == str(51)) or (cc_num[0:2] == str(52)) or \
         (cc_num[0:2] == str(53)) or (cc_num[0:2] == str(54)) or (cc_num[0:2] == str(55)) ):
    return ('Mastercard')
  elif (cc_num[0] == str(4)):
    return ('Visa')
  else:
    return ('\b')

#This function executes Luhn's Test
def Luhn(cc_num):

  length = len(cc_num)
  
  #first executing for length 15
  if (length == 15):
    sum = 0
    for i in range (0,16,2):
      x = 2 * eval(cc_num[i])
      if (len(str(x)) == 2):
        x = str(x)
        x = eval(x[0]) + eval(x[1])
      sum +=x
    #sum evens for 15
    sum2 = 0
    for i in range(1,15,2):
      sum2 += int(cc_num[i])

  #now for length 16
  elif (length == 16):
    sum = 0
    for i in range(0,16,2):
      x = 2 * eval(cc_num[i])
      if (len(str(x)) == 2):
        x = str(x)
        x = eval(x[0]) + eval(x[1])
      sum += x
    #sum evens for 16
    sum2 = 0
    for i in range(1,17,2):
      sum2 += int(cc_num[i])
 
  #check if sum is divisible by 10 FINISH
  sumTotal = sum + sum2
  if (sumTotal % 10 == 0):
    return True
  else: 
    return False

#Main function determines validity and type of credit card number
def main():
  cc_num = eval(input('Enter 15 or 16-digit credit card number: '))
  if (is_valid(cc_num) == True):
    print('\nNot a 15 or 16-digit number')
    return
  else:
    pass
  x = cc_type(str(cc_num))
  if (Luhn(str(cc_num))):
    print('\nValid', x, 'credit card number')
  else:
    print('\nInvalid credit card number')

main()