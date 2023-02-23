class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

def printInorder(node):
    if node:
        printInorder(node.left)
        print(node.data, end = ' ')
        printInorder(node.right)

def printPreorder(node):
    if node:
        print(node.data, end=' ')
        printPreorder(node.left)
        printPreorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print(node.data, end=' ')


def printInorderWithoutRecursion(node):
    current = node
    stack = []

    while(True):
        if(current is not None):
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data,end=' ')
            current = current.right
        else:
            break

def printPostorderWithoutRecursion(node):
    current = node
    stack = []
    stack.append(current)
    while(len(stack) > 0):         
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

        current = stack.pop()
        print (current.data, end=' ')
        
def printPreorderWithoutRecursion(node):
    current = node
    stack = []
    stack.append(current)
    while(len(stack) > 0):
         
        current = stack.pop()
        print (current.data, end=' ')
         
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

query = list(map(str,input("Enter the Data: ").rstrip().split(' ')))

root = Node(query[0])
for i in query[1:]:
    root.insert(i)

print("\nIn-Order Traversal  :", end=' ')
printInorder(root)
print("\nPre-Order Traversal :", end=' ')
printPreorder(root)
print("\nPost-Order Traversal:", end=' ')
printPostorder(root)


print("\nIn-Order Traversal without recursion  :", end=' ')
printInorderWithoutRecursion(root)
print("\nPre-Order Traversal without recursion :", end=' ')
printPreorderWithoutRecursion(root)
print("\nPost-Order Traversal without recursion:", end=' ')
printPostorderWithoutRecursion(root)