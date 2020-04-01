  
# This class represents a directed graph using adjacency 
# list representation 
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printPreorder(root):
    if root == None:
        return
    print (root.data)
    printPreorder(root.left)
    printPreorder(root.right)

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print (root.data)
    printInorder(root.right)
def printPostorder(root):
    if root == None:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print (root.data)


if __name__=="__main__":
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 
    print ("Preorder traversal of binary tree is")
    printPostorder(root) 
