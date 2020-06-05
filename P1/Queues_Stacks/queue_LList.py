class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1

    def dequeue(self, value):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

"""
Time Complexity:

So what's the time complexity of adding or removing things from our queue here?

Well, when we use enqueue, we simply create a new node and add it to the tail of the list. And when we dequeue an item, we simply get the value from the head of the list and then shift the head variable so that it refers to the next node over.

Both of these operations happen in constant time—that is, they have a time-complexity of O(1).
"""