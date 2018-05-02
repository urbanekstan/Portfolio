##################################################################
#  File: TestBinaryTree.py

#  Description: Creates a binary trees and test different functions

#  Student Name: Stanley Urbanek

#  Course Name: CS 313E

##################################################################


class Node (object):
  # node constructor
  def __init__(self,data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # tree constructor
  def __init__(self):
    self.root = None

  #search for a node with a key
  def find(self,key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in the tree
  def insert(self, val):
    newNode = Node (val)
    if (self.root == None):
      self.root = newNode
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
    if (val < parent.data):
      parent.lchild = newNode
      return 
    else:
      parent.rchild = newNode
      return 


  # pre order traversal - center, left, right
  def postOrder( self, aNode,nodes):
    if (aNode != None):
      self.postOrder(aNode.lchild,nodes)
      self.postOrder(aNode.rchild,nodes)
      #append the nodes to a list 
      nodes.append(aNode.data)

  
  # Returns true if two binary trees are similar
  def isSimilar (self, pNode):
    # create a list of the nodes from first tree
    nodes1 = []
    # puts the nodes in order in the list
    self.postOrder(self.root, nodes1)
    # create a list of the nodes from the second tree
    nodes2 = []
    # puts the nodes in order in the list 
    pNode.postOrder(pNode.root, nodes2)
    # if the two lists are equal then the trees are similar
    return nodes1 == nodes2


  # Prints out all nodes at the given level
  def printLevel (self,aNode, level,lev):
    # if the node exists continue
    if (aNode != None):
      # if the current level doesnt equal the level youre looking for continue
      if (lev != level):
        # increase youre level
        lev+= 1
        #then move to right and left leaf on next level
        self.printLevel(aNode.lchild,level,lev)
        self.printLevel(aNode.rchild,level,lev)
      # when you reach your level print out the data 
      else:
        if aNode != None:
          print(aNode.data , " ", end='') 
    return

  # Returns the height of the tree
  def getHeight (self, aNode):
    # if there are no nodes then height is zero
    if (aNode == None):
      return 0
    # recursively count high by going down left subtree and right subtree
    # get max value from each subtree and thats max height 
    else:
      return max(self.getHeight(aNode.lchild), self.getHeight(aNode.rchild)) + 1

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self, aNode):
    # if node doesnt exist return 0
    if aNode == None:
      return 0
    # recursively count nodes on each side of the tree
    else:
      return self.numNodes(aNode.rchild) + self.numNodes(aNode.lchild) + 1

def main():
  # Read in the file and create two trees
  tree1 = Tree()
  tree2 = Tree()
  change = 0
  inFile = open('input.txt', 'r')
  for line in inFile:
    line = line.rstrip('\n')
    if line == '':
      change = 1
    else:
      if change == 1:
        tree2.insert(int(line))
      else:
        tree1.insert(int(line))
  inFile.close()

  
  # Test your method isSimilar()
  print (tree1.isSimilar(tree2), "\n")

  # Print levels 1,3,5 of tree 1
  print("level 1: ", end='')
  tree1.printLevel(tree1.root, 1 ,1)
  print('')

  print ("level 3: ", end='')
  tree1.printLevel(tree1.root, 3 ,1)
  print('')

  print ("level 5: ", end='')
  tree1.printLevel(tree1.root, 5 ,1)
  print('\n')

  
  #print levels 2,4,6 of tree 2
  print ("level 2: ", end='')
  tree2.printLevel(tree2.root, 2 ,1)
  print('')

  print ("level 4: ", end='')
  tree2.printLevel(tree2.root, 4 ,1)
  print('')

  print ("level 6: ", end='')
  tree2.printLevel(tree2.root, 6 ,1)
  print('\n')
  
  # Get the height and  number of nodes of tree1
  print(tree1.getHeight(tree1.root))
  print(tree1.numNodes(tree1.root), "\n")

  # get the height and  number of nodes of tree2
  print(tree2.getHeight(tree2.root))
  print(tree2.numNodes(tree2.root))
main()
