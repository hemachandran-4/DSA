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

