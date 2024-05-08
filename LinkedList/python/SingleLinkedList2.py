class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, data):
    node = Node(data)
    node.next = head
    head = node
    return head

def printList(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print()
    
def findMiddleNode(head):
    node = head
    if not node:
        return None
    
    slow = node
    fast = node.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.data
    

def reverse_linked_list(head):
    perv_node = None
    current_node = head
    
    while current_node:
        next_node = current_node.next
        current_node.next = perv_node
        perv_node = current_node
        current_node= next_node
    
    return perv_node

head = None
printList(head)

head = insertAtFront(head, 66)
printList(head)
print(findMiddleNode(head))

head = insertAtFront(head, 45)
printList(head)
print(findMiddleNode(head))

head = insertAtFront(head, 72)
printList(head)
print(findMiddleNode(head))

head = insertAtFront(head, 35)
printList(head)
print(findMiddleNode(head))

head = insertAtFront(head, 97)
printList(head)
print(findMiddleNode(head))

head = reverse_linked_list(head)
printList(head)