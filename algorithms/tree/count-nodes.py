class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def count(node, level, givenLevel):
    if node==None:
        return 0
    if level==givenLevel:
        return 1
    return (count(node.left, level+1, givenLevel) +
    count(node.right, level+1, givenLevel))

if __name__=="__main__":
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 
    print ("Preorder traversal of binary tree is")
    print(count(root,0,2)) 