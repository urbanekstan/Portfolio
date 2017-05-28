#  File: Books.py

#  Description: Compiles and compares the dictionaries of two different books.

#  Student Name: Stanley Urbanek

#  Student UT EID: su964

#  Course Name: CS 303E

#  Unique Number: 90110

#  Date Created: 8/12/2014

#  Date Last Modified: 8/13/2014

##########################################################

# Removes the puncuation from each word
def filter_string (st):
  s = ''
  index = 0
  
  # determines if given character is acceptable
  for ch in st:
    if ((ch >= 'a') and (ch <= 'z')):
      s += ch
      index += 1
    elif ch == "'" and (st[index - 1] == '"' or st[index - 1] == ' '):
      s += ''
      index += 1
    elif (index + 1) < len(st) and ((ch == "'" and st[index + 1] == "s") or (ch == "s" and st[index - 1] == "'")):
      s += ''
      index += 1
    elif (index + 1) < len(st) and ch == "'" and st[index + 1] != 's':
      s += ch
      index += 1
    else:
      s += ' '
      index += 1

  # returns filtered string
  return s

# Determines the total number of words as well as unique words
def book_word_stats(file):
  # open empty dictionary and the book
  word_dict = {}
  book = open(file, 'r')
  scrabble = open('words.txt','r')

  # total number of words
  total_words = 0

  # read book line by line
  for line in book:
    # remove leading and trailing spaces
    line = line.strip()

    # make everything lower case
    line = line.lower()

    # filter the line
    line = filter_string (line)

    # get the words in the line
    word_list = line.split()

    # add words to the dictionary
    for word in word_list:
      total_words += 1
      if word in word_dict:
        word_dict[word] = word_dict[word] + 1
      else:
        word_dict[word] = 1

  # close the book
  book.close()
  
  # print
  print("Total distinct words = " + str(len(word_dict)))
  print("Total words (including duplicates) = " + str(total_words))
  a = round(100 * len(word_dict) / total_words, 10)
  print("Ratio (% of total distinct words to total words) = " + str(a))

  # returns what I will need in future computations
  return word_dict, total_words

# Returns total number of unique words used
def unique(a, book_dict1, book_dict2):
  #get total number of unique words used
  unique = 0
  for word in a:
    if word not in book_dict2:
      unique += book_dict1[word]
  return unique


# Determines and prints relative statistics of the books
def rel_stats(book_dict1, book_dict2, total1, total2, author1, author2):
  # assigns exclusive differences
  a1 = set(book_dict1)
  a2 = set(book_dict2)
  A = a2 - a1
  B = a1 - a2
  
  # prints out the second half, relative statistics
  print('\n' + author1 + ' used ' + str(len(B)) + ' words that ' + author2 + ' did not use.')
  asdf = unique(a1, book_dict1, book_dict2)
  print('Relative frequency of words used by ' + author1 + ' not in common with ' + author2 + ' = ' + str(round(asdf* 100 / total1, 10)))

  print()
  print(author2 + ' used ' + str(len(A)) + ' words that ' + author1 + ' did not use.')
  print('Relative frequency of words used by ' + author2 + ' not in common with ' + author1 + ' = ' + str(round(unique(a2, book_dict2, book_dict1)* 100 / total1, 10)))

# The main function that calls the subfunctions
def main():
  # open text
  file1 = input("Enter name of first book: ")
  file2 = input("Enter name of second book: ")
  print()

  # choose author names
  author1 = input("Enter last name of first author: ")
  author2 = input("Enter last name of second author: ")

  # print the author and individual book stats
  print('\n' + str(author1))
  book_dict1, total1 = book_word_stats(file1)
  
  print('\n' + str(author2))
  book_dict2, total2 = book_word_stats(file2)

  # call rel_stats function
  rel_stats(book_dict1, book_dict2, total1, total2, author1, author2)

main()