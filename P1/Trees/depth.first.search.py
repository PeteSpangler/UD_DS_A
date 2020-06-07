class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s
"""
So to traverse/search the Binary Tree, if you do not keep track of what nodes you have checked
(in this they are tracked by the State class) then it would just keep pumping down the left most
branch over and over until the loop breaks or if you did not mark a break point, like 
after setting the count to 0 and then looping unti its == 7 or whatever you set the break point at
it would infinitely run just pumping into that leftmost leaf (as how it was in the example of going to dates over and over again)
but when you include the state class, it keeps track and does not visit nodes repeatedly
"""
def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order

def pre_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_value())
            
            # traverse left subtree
            traverse(node.get_left_child())
            
            # traverse right subtree
            traverse(node.get_right_child())
    
    traverse(tree.get_root())
    
    return visit_order
"""
so these two are the same (traversing a pre-order binary tree)
but the 2nd is done with recursion
"""
def in_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # visit node
            visit_order.append(node.get_value())
            
            # traverse right sub-tree
            traverse(node.get_right_child())
    
    traverse(tree.get_root())
    
    return visit_order

def post_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # traverse right subtree
            traverse(node.get_right_child())
            
            # visit node
            visit_order.append(node.get_value())
    
    traverse(tree.get_root())
    
    return visit_order
"""
then these two (in_order and post_order) are traversal using recursion
"""