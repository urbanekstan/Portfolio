#################################################################
#  File: TestLinkedList.py

#  Description: Creates the class linked list and test different functions

#  Student Name: Stanley Urbanek

#  Course Name: CS 313E

#  Date Created: 4/12/15

#####################################################################

class Link (object):
  # initialize Link 
  def __init__(self, data, next = None):
      self.data = data
      self.next = next

  
class LinkedList (object):
  # initialize data
  def __init__(self):
      self.first = None
      
  # get number of links 
  def getNumLinks (self):
    current = self.first
    # create a counter
    num = 0
    if current == None:
      print (num)
    while (current != None):
      current = current.next
      num += 1
    print (num) 
  
  # Add data at the beginning of the list
  def addFirst (self, data):
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink
    
  # Add data at the end of a list
  def addLast (self, data):
    newLink = Link(data)
    current = self.first
    if (current == None):
      self.first = newLink
      return
    while (current.next != None):
      current = current.next
    current.next = newLink

  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
    newLink = Link(data)
    current = self.first
    if current == None:
      self.first = newLink
      return
    # see if the data is smaller than the first link
    if data < current.data:
      self.addFirst(data)
      return 
    while current.data < data:
      # create a placeholder
      previous = current  
      current = current.next
      #check to see if youve hit the end of the linked list
      if current == None:
        self.addLast(current.data)
        return
    #add the link and connect to rest of linked list
    previous.next = newLink
    newLink.next = current
    return 


  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
    current = self.first
    if current == None:
      return None
    # run through the list until you find the data point you want 
    while current.data != data:
      # if no point found return none
      if current.next == None:
        return None
      else:
        current = current.next
    # return location of the link
    return current 

  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
    current = self.first
    if current == None:\
      return None
    # run through the list until the data point is found
    while current.data != data:
      # if at end of list return none
      if current.next == None:
        return None
      # if a data point is found larger than the one you were searching for
      # return non
      elif current.data > data:
        return None
      else:
        current = current.next
    # return location of the point 
    return current 
      
  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    current = self.first
    previous = self.first
    # if empty list return none
    if current == None:
      return None
    # run through the list until you find data point
    while current.data != data:
      # if at end of list return none
      if current.next == None:
        return None
      else:
        previous = current
        current = current.next
    # delete the point from linked list
    if current == self.first:
      self.first = self.first.next
    else:
      previous.next = current.next
    # return location of data point
    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__(self):
    current = self.first
    counter = 0
    result = ''
    if current == None:
      return result
    # print only 10 on each line 
    while current != None:
      counter += 1
      if counter < 10:
        result += (str(current.data) + '  ' )
      if counter == 10:
        if current.next != None:
          result += (str(current.data) + '  \n')
          counter = 0
        else:
          result += (str(current.data) + '  ')
          counter = 0 
      current = current.next
    return result 
  
  # Copy the contents of a list and return new list
  def copyList (self):
    # create a new linked List
    copyLL = LinkedList()
    current = self.first
    if current == None:
      return copyLL
    # run through current link list and add to new Link List 
    while current != None:
      copyLL.addLast(current.data)
      current = current.next
    # return copied list
    return copyLL

  # Reverse the contents of a list and return new list
  def reverseList (self):
    # create new link list
    reverseLL = LinkedList()
    current = self.first
    if current == None:
      return reverseLL
    # add from the front to create a reversed list
    while current != None:
      reverseLL.addFirst(current.data)
      current = current.next
    # return the reverse list
    return reverseLL
  
    
  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
    # create new list
    sortLL = LinkedList()
    current = self.first
    if current == None:
      return sortLL
    # add in order to the new list to sort the link list 
    while current != None:
      sortLL.addInOrder(current.data)
      current = current.next
    return sortLL       

  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
    current = self.first
    if current == None:
      return False
    while current.next != None:
      # if the next data point is less than the current point its wrong 
      if current.data > current.next.data:
        return False
      current = current.next
    return True 

  # Return True if a list is empty or False otherwise
  def isEmpty (self):
    # check if list is empty
    if self.first == None:
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
    # create new list
    MLL = LinkedList()
    # if both lists empty return empty list
    if self.first == None and b.first == None:
      return MLL
    # if first list is empty return second and vice versa
    elif self.first == None:
      return b
    elif b.first == None:
      return self
    currentSelf = self.first
    currentB = b.first
    # run through lists until both are empty
    while currentSelf != None or currentB != None:
      # if both arent empty see which one has smaller data first and then add
      # to new list
      if currentSelf != None and currentB != None:
        if currentSelf.data <= currentB.data:
          MLL.addLast(currentSelf.data)
          currentSelf = currentSelf.next
        else:
          MLL.addLast(currentB.data)
          currentB = currentB.next
      # if first list is empty just add the links from the second list
      # vice versa for second list
      elif(currentSelf != None):
        MLL.addLast(currentSelf.data)
        currentSelf = currentSelf.next
      elif(currentB != None):
        MLL.addLast(currentB.data)
        currentB = currentB.next
    # return merged list
    return MLL
  
     
     
  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
    current = self.first
    currentB = b. first
    # if both empty return true
    if current == None and currentB == None:
      return True
    # if one is empty and the other is not return false
    elif current == None and currentB != None:
      return False
    elif current != None and currentB == None:
      return False
    # check to make sure both arent empty
    while current != None or currentB != None:
      # if both arent empty see if there links are equal
      # if not return False
      if current != None and currentB != None:
        if current.data != currentB.data:
          return False
      else:
        return False 
      current = current.next
      currentB = currentB.next
    return True 

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
    # create a list to keep track of seen data points
    dupNum = []
    current = self.first
    if current == None:
      NoDupLL = LinkedList()
      # if list is empty return an empty list
      return NoDupLL
    while current != None:
      # check to see if the data point is in the list already
      # if yes then delete from Linked List
      if current.data in dupNum:
        self.delete(current.data)
      #if not then add to list and continue through Linked List
      else:
        dupNum.append(current.data)
      current = current.next
    # copy the original list and return 
    NoDupLL = self.copyList()
    return NoDupLL 

def main():
  # Test methods addFirst() and __str__() by adding more than
  # 10 items to a list and printing it.
  array_list1 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
  LL1 = LinkedList()
  
  for item in array_list1:
    LL1.addFirst(item)
  print(str(LL1))
  
    
  # Test method addLast()
  
  array_list2 = [19,15,13,11,17]
  LL2 = LinkedList()
  for item in array_list2:
    LL2.addLast(item)
  print(str(LL2))


  #Test method addInOrder()
  LL1.addInOrder(3)
  print (str(LL1))

  LL1.addInOrder(13)
  print(str(LL1))

  # Test method getNumLinks()
  LL1.getNumLinks()

  LL2.getNumLinks()

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there
  print(LL2.findUnordered(11))
  print(LL2.findUnordered(12))

  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there
  print(LL1.findOrdered(18))
  print(LL1.findOrdered(19))

  # Test method delete()
  # Consider two cases - item is there, item is not there
  print(LL1.delete(14))
  print(LL1.delete(15))
  print(LL2.delete(15))

  print(str(LL1))
  print(str(LL2))

  # Test method copyList()
  print(LL1.copyList())
  

  # Test method reverseList()
  print(LL2.reverseList())

  # Test method sortList()
  LL3 = LL2.sortList()
  print(str(LL3))

  print(str(LL1))
  print(str(LL2))
  print(str(LL3))

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print(LL1.isSorted())
  print(LL2.isSorted())
  print(LL3.isSorted())

  # Test method isEmpty()
  print(LL1.isEmpty())
  print(LL2.isEmpty())
  print(LL3.isEmpty())

  # Test method mergeList()
  LL4 = LL1.mergeList(LL3)
  print(str(LL4))
  

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print(LL1.isEqual(LL4))
  print(LL1.isEqual(LL2))
  print(LL1.isEqual(LL1))

  # Test removeDuplicates()
  print(str(LL4))
  print(LL4.removeDuplicates())
main()
