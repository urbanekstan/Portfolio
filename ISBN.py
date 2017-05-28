#  File: ISBN.py

#  Description: Determines validity of a given ISBN number.

#  Student Name: Stanley Urbanek

#  Student UT EID: su964

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: 7/30/14

#  Date Last Modified: 7/30/14

#######################################


#Determines validity of ISBN number
def check_validity(isbn):
  if (isbn.find(' ') != -1):
    return False
  isbn = isbn.replace('-','')
  if len(isbn) != 10:
    return False
  if (isbn[9] != 'X') and (isbn[9] != 'x'):
    return False
  for i in range(9):
    if (isbn[i] < '0' or isbn[i] > '9'):
      return False
  return True

#Cumulative sum of ISBN
def cumSum(st):
  st = st.replace('-','')
  
  #save each digit to place in array
  list = []
  for i in range(9):
    list.append(int(st[i]))
  list.append(10)
  
  #cumulative sum1
  s1 = []
  s1.append(list[0])
  for i in range(9):
    s1.append(s1[i] + list[i+1])
  
  #cumulative sum2
  s2 = []
  s2.append(s1[0])
  for i in range(9):
    s2.append(s2[i] + s1[i+1])
  return s2[9]

def main():
  #opening files
  readfile = open('isbn.txt','r')
  writefile = open('isbnOut.txt','w')

  #loop to get all isbn numbers in file
  for line in readfile:
    isbn = line 

  #validity check alongside cumulative sum
    if (check_validity(isbn)):
      new = cumSum(isbn)
      if (new % 11 == 0):
        writefile.write(isbn + ' valid\n')
      else: 
        writefile.write(isbn + ' invalid\n')
    else:
      writefile.write(isbn + ' invalid\n')

  #saving files
  writefile.close()
  readfile.close()
  
main()