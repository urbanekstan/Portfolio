###################################################
#  File: Josephus.py

#  Description: Determines which soldier goes free

#  Student Name: Stanley Urbanek

#  Course Name: CS 313E

#  Date Created: 4/5/2015
######################################################

class Link(object):
  # initialize link
  def __init__(self,data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return (str(self.data))

class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.head = None

  # Insert an element in the list
  def insert ( self, item ):
      # initialize the link
      NewLink = Link(item)
      if self.head == None:
          self.head = NewLink
          NewLink.next = NewLink
      else:
          NewLink.next = self.head.next
          self.head.next = NewLink
          self.head = NewLink          
      return 
      

  # Find the link with the given key
  def find ( self, key ):
      current = self.head.next
      start = self.head
      if current == None:
          return None
      # traverse through list until you find key
      while current.data != start.data:
          if current.data == key:
              return current
          else:
              current = current.next
      if current.data == key:
          return current
      return None 

  # Delete a link with a given key
  def delete ( self, key ):
      last = self.head
      current = self.head.next
      # check if list is empty
      if last == None:
          return None
      # traverse through the list until you find your link
      while current.data != self.head.data:
          if current.data == key:
              #delete link and return deleted link
              last.next = current.next
              return current
          else:
              last = current
              current = current.next
      # if last is the matching link then delte and intitalize new last
      if current.data == key:
          last.next = current.next
          self.head = last
          # return deleted link
          return current 
              
    
  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):
      cur = self.find(start)
      if cur == None:
          return None 
      counter = 1
      # run through link until youve hit n
      while counter != n:
          cur = cur.next
          counter += 1
      # delete nth link
      cur=self.delete(cur.data)
      # print deleted link
      print(cur.data)
      # return next link 
      return cur.next
          
  # Return a string representation of a Circular List
  def __str__ ( self ):
      
      current = self.head.next
      counter = 0
      result = ''
      if current == None:
        return result
      # print only 10 on each line 
      while current.data != self.head.data:
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
      result  += str(current.data) + '  '
      return result 
    
          
def main():
  # open the file
  inFile = open('josephus.txt', 'r')
  # read in the first line and get the soldier count
  line1 = inFile.readline()
  line1 = line1.split()
  numSold = int(line1[0])
  # read in the second line and get the starting soldier
  line2 = inFile.readline()
  line2 = line2.split()
  start = int(line2[0])
  # read in the third line and get the shift 
  line3 = inFile.readline()
  line3 = line3.split()
  shift = int(line3[0])
  # close the file
  inFile.close()

  # create the linked list
  Soldiers = CircularList()
  #add soldiers to the list
  for i in range (1,numSold + 1):
    Soldiers.insert(i)
  # create a counter for dead people
  dead = 0
  #run through until you get the last person
  while dead < numSold - 1:
      if dead == 0:
        start = Soldiers.deleteAfter(start, shift)
      else:
        start = Soldiers.deleteAfter(start.data,shift)
      dead += 1
  # print last person
  print (start)
 

main()
