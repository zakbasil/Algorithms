class SLL:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def display(head):
    traversal = head
    while traversal:
        print(traversal.data, end = ' ')
        traversal = traversal.next
    print()

def displayReverse():
    pass

def addBeginning(head,data):
    newNode = SLL(data)
    newNode.next = head
    return(newNode)


def appendNode(head, data):
    newNode = SLL(data)
    traversal = head
    
    while traversal.next != None:
        traversal = traversal.next
    traversal.next = newNode

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

value = SLL(5)
appendNode(value, 4)
appendNode(value, 3)
appendNode(value, 2)
appendNode(value, 1)

value = addBeginning(value, 0)
value = addBeginning(value, 23)
value = addBeginning(value, 34)

display(value)

value = delete(value, 0)
value = delete(value, 34)
value = delete(value, 1)

display(value)