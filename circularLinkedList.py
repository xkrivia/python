# CHRIS FELLI, 2019
# Detect if there is a loop in linked list

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    def setNext(self, next_node = None):
        self.next = next_node

def has_cycle(head):
    if head == None:
        return False
    tortoise = hare = head
    while(tortoise or hare or hare.next):
        if hare.next == None:
            return False
        if tortoise == hare.next or tortoise == hare.next.next:
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    return False

# Testcases
n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n4)

# Create loop
n2.setNext(n4)

m1 = Node(1, None)
m2 = Node(2, m1)
m3 = Node(3, m2)
m4 = Node(4, m3)
m5 = Node(5, m4)

print(has_cycle(n5))
print(has_cycle(m5))
