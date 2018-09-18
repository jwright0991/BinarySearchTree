#@author Josh Wright
#Tree Node Object Representation
#Each node has a parent node, except the root of a tree who's parent is null.
#Each node may have 0-2 children(left and right)
#Data is an integer value
#isEvenSum is a boolean value asserting whether the sum of all the node's
#children's data and the node's data results in an even integer.
class TreeNode:
    #default constructor
    #paramater data is the integer value that represents the node
    def __init__(self,data):
        self.parent = None
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.isEvenSum = (data % 2 == 0)
        self.size = 1;
        self.isEven = (data % 2 == 0)
    #Returns the string representation of the node and it's children (recursive)
    def __str__(self):
        stringRep = "EMPTY"
        if self.data == None:
            return "NONE"
        elif self.leftChild != None and self.rightChild != None:
            stringRep = str(self.data) + "(" + str(self.leftChild) + ", " + str(self.rightChild) + ")"
            return stringRep
        elif self.leftChild == None and self.rightChild != None:
            stringRep = str(self.data) + "(EMPTY, " + str(self.rightChild) + ")"
            return stringRep
        elif self.leftChild != None and self.rightChild == None:
            stringRep = str(self.data) + "(" + str(self.leftChild) + ",EMPTY)"
            return stringRep
        elif self.leftChild == None and self.rightChild == None:
            stringRep = str(self.data) + "(EMPTY, EMPTY)"
            return stringRep
