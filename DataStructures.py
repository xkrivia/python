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

class DNode: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data

    # Adding a node at the front of the list 
    def push(self, new_data): 
        # 1 & 2: Allocate the Node & Put in the data
        new_node = DNode(data = new_data) 
    
        # 3. Make next of new node as head and previous as NULL 
        new_node.next = self.head 
        new_node.prev = None
    
        # 4. change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new_node 
    
        # 5. move the head to point to the new node 
        self.head = new_node  