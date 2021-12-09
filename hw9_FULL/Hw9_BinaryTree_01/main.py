#Name: Alejandra Hernandez
#Date: 11/18/2020
#Desc: shows tree traversal inorder, preorder, postorder
#      with a queue
#https://www.learnsteps.com/binary-tree-traversal-using-python/

class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def preOrder(root):
   if root:
       print (root.data)
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print (root.data)

#making the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("INORDER: ")
inOrder(root)
print()
#4 2 5 1 3
print("PREORDER: ")
preOrder(root)
print()
#1 2 4 5 3
print("POSTORDER: ")
postOrder(root)
print()