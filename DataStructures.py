# CHRIS FELLI, 2019
# Common data structure implementations in Python

# STACK: Append and pop list as a stack (LIFO):

s = []

s.append('eat')
s.append('sleep')
s.append('code')

s
#['eat', 'sleep', 'code']

s.pop()
'code'
s.pop()
'sleep'
s.pop()
'eat'

# ARRAY: Add multiple iterms at once, if same datatype

import array as arr
numbers = arr.array('i', [1, 2, 3, 4])
numbers.extend([5, 6, 7])
#array('i', [1, 2, 3, 4, 5, 6, 7])

# QUEUE: collections.deque as a stack (LIFO):

from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

q
deque(['eat', 'sleep', 'code'])

q.pop()
'code'
q.pop()
'sleep'
q.pop()
'eat'

#q.pop()
IndexError: "pop from an empty deque"

# QUEUE: How to use collections.deque as a FIFO queue:

from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

q
deque(['eat', 'sleep', 'code'])

q.popleft()
'eat'
q.popleft()
'sleep'
q.popleft()
'code'

#q.popleft()
#IndexError: "pop from an empty deque"

# QUEUE: How to use queue.LifoQueue as a stack:
# Synchronizes and locks files, useful at scale

from queue import LifoQueue
s = LifoQueue()

s.put('eat')
s.put('sleep')
s.put('code')

s
#<queue.LifoQueue object at 0x098257092>

s.get()
'code'
s.get()
'sleep'
s.get()
'eat'

#s.get_nowait()
#queue.Empty

#s.get()
# Blocks / waits forever...

# QUEUE: How to use multiprocessing.Queue as a FIFO queue:
# (Useful for batching jobs as an async)

from multiprocessing import Queue
q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

q
#<multiprocessing.queues.Queue object at 0x1081c12b0>

q.get()
'eat'
q.get()
'sleep'
q.get()
'code'

#q.get()
# Blocks / waits forever...

# LINKED LIST:

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    # O(1)
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # O(N)
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # O(N), worst case
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    # O(N), worst case
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# DOUBLY LINKED LIST

# A complete working Python program to demonstrate all 
# insertion methods 

# A linked list node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

# Class to create a Doubly Linked List 
class DoublyLinkedList: 

	# Constructor for empty Doubly Linked List 
	def __init__(self): 
		self.head = None

	# Given a reference to the head of a list and an 
	# integer, inserts a new node on the front of list 
	def push(self, new_data): 

		# 1. Allocates node 
		# 2. Put the data in it 
		new_node = Node(new_data) 

		# 3. Make next of new node as head and 
		# previous as None (already None) 
		new_node.next = self.head 

		# 4. change prev of head node to new_node 
		if self.head is not None: 
			self.head.prev = new_node 

		# 5. move the head to point to the new node 
		self.head = new_node 

	# Given a node as prev_node, insert a new node after 
	# the given node 
	def insertAfter(self, prev_node, new_data): 

		# 1. Check if the given prev_node is None 
		if prev_node is None: 
			print("the given previous node cannot be NULL")
			return

		# 2. allocate new node 
		# 3. put in the data 
		new_node = Node(new_data) 

		# 4. Make net of new node as next of prev node 
		new_node.next = prev_node.next

		# 5. Make prev_node as previous of new_node 
		prev_node.next = new_node 

		# 6. Make prev_node ass previous of new_node 
		new_node.prev = prev_node 

		# 7. Change previous of new_nodes's next node 
		if new_node.next is not None: 
			new_node.next.prev = new_node 

	# Given a reference to the head of DLL and integer, 
	# appends a new node at the end 
	def append(self, new_data): 

		# 1. Allocates node 
		# 2. Put in the data 
		new_node = Node(new_data) 

		# 3. This new node is going to be the last node, 
		# so make next of it as None 
		new_node.next = None

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			new_node.prev = None
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while(last.next is not None): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 

		# 7. Make last node as previous of new node 
		new_node.prev = last 

		return

	# This function prints contents of linked list 
	# starting from the given node 
	def printList(self, node): 

		print("\nTraversal in forward direction")
		while(node is not None): 
			#print(" % d")%(node.data), 
			last = node 
			node = node.next

		print("\nTraversal in reverse direction")
		while(last is not None): 
			#print(" % d")%(last.data), 
			last = last.prev 

# Driver program to test above functions 

# Start with empty list 
llist = DoublyLinkedList() 

# Insert 6. So the list becomes 6->None 
llist.append(6) 

# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 

# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 

# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 

# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 

print("Created DLL is: "), 
llist.printList(llist.head) 
