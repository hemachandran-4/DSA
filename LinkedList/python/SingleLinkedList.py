class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertAtFront(head, data):
    node = Node(data)
    node.next = head
    head = node
    return head

def insertAtEnd(head, data):
    node = head
    while node.next is not None:
        node = node.next
    newNode = Node(data)
    node.next = newNode
    return head

def printList(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print()

def removeFirstNode(node):
    if not node:
        return None
    return node.next

def removeLastNode(head):
    if head is None or head.next is None:
        return None
    node = head
    while node.next.next is not None:
        node = node.next
    node.next = None
    return head

def insertAtNthPosition(head, data, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    
    for _ in range(n-1):
        slow = slow.next
    
    newNode = Node(data)
    newNode.next = slow.next
    slow.next = newNode
    
    return dummy.next

def deletingFromNthPosition(head, n):
    dummy = Node(0)
    dummy.next = head
    
    slow = dummy
    
    for _ in range(n-1):
        slow = slow.next
    
    slow.next = slow.next.next
    
    return dummy.next

def updateNthValue(head, data, n):
    dummy = Node(n)
    dummy.next = head
    slow = dummy
    
    for _ in range(n-1):
        slow = slow.next
        
    slow.next.data = data

    return dummy.next

#Creating a Linked List
head = None

#Inserting at beginning of Linked List
head = insertAtFront(head, 5)
head = insertAtFront(head, 4)
head = insertAtFront(head, 3)
head = insertAtFront(head, 2)
head = insertAtFront(head, 1)
printList(head)

#Inserting at the end of LinkedList
head = insertAtEnd(head, 6)
head = insertAtEnd(head, 7)
head = insertAtEnd(head, 8)
head = insertAtEnd(head, 9)
head = insertAtEnd(head, 10)

#Traversing a Linked List
printList(head)

#Removing the first node
head = removeFirstNode(head)
printList(head)

#Removeing the last node
head = removeLastNode(head)
printList(head)

#Inserting at a specific point in a linked List
head = insertAtNthPosition(head, 1, 1)
printList(head)
head = insertAtNthPosition(head, 10, 10)
printList(head)

head = insertAtNthPosition(head, 7, 7)
printList(head)



#Deleting from a specific point in a linked list
head = deletingFromNthPosition(head, 7)
printList(head)
head = deletingFromNthPosition(head, 10)
printList(head)
head = deletingFromNthPosition(head, 9)
printList(head)
head = deletingFromNthPosition(head, 8)
printList(head)
head = deletingFromNthPosition(head, 1)
printList(head)


#update a node's value
head = updateNthValue(head, 100, 1)
printList(head)
head = updateNthValue(head, 200, 2)
printList(head)
head = updateNthValue(head, 400, 4)
printList(head)
head = updateNthValue(head, 600, 6)
printList(head)
