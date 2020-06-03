class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0


#reverse given stack function:
def reverse_stack(stack):
        """
        Reverse a given input stack

        Args:
        stack(stack): Input stack to be reversed
        Returns:
       stack: Reversed Stack
        """
        holder_stack = Stack()
        while not stack.is_empty():
            popped_element = stack.pop()
            holder_stack.push(popped_element)
            _reverse_stack_recursion(stack, holder_stack)


def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)