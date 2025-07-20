class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertEnd(head, data):
    newNode = Node(data)
    traversal = head
    while(traversal.next != None):
        traversal = traversal.next
    traversal.next = newNode
    newNode.prev = traversal
    return(head)

def insertBeginning(head, data):
    newNode = Node(data)
    newNode.next = head
    if head:
        head.prev = newNode
    return(newNode)

def displayList(head):
    traversal = head
    while(traversal != None):
        print(traversal.data, end = ' ')
        traversal = traversal.next    
    print()

def displayReverse(head):
    traversal = head
    while(traversal.next != None):
        traversal = traversal.next
    while(traversal != None):
        print(traversal.data, end = ' ')
        traversal = traversal.prev
    print()

def delete(head, deleteElement):
    traversal = head
    while traversal:
        if traversal.data == deleteElement:
            if traversal == head:
                traversal = traversal.next
                traversal.prev = None
                head.next = None
                return(traversal)
            
            prevNode = traversal.prev
            nextNode = traversal.next
            prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
            return(head)

        traversal = traversal.next
    return(head)

val = Node(10)
val = insertBeginning(val, 20)
val = insertBeginning(val, 80)
val = insertBeginning(val, 90)
val = insertEnd(val, 30)
val = insertEnd(val, 50)

val = delete(val, 80)

val = insertEnd(val, 60)
val = insertEnd(val, 70)

print("Display the DLL: ")
displayList(val)
print("Display the DLL in reverse: ")
displayReverse(val)

