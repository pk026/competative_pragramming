# Flattening a Linked List
# Given a linked list where every node represents a linked list and contains two pointers of its type:
# (i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
# (ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
# All linked lists are sorted. See the following example

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data, v_head):
        new_node = Node(data)
        new_node.right = self.head
        self.head = new_node
        new_node.down = v_head
        v_head = new_node

def merge_node(node_a, node_b):
    if node_a is None:
        return node_b

    if node_b is None:
        return node_a

    result = Node()
    if node_a.data < node_b.data:
        result = node_a
        result.down = merge_node(node_a.down, node_b)
    else:
        result = node_b
        result.down = merge_node(node_a, node_b.down)
    return result

def flatten(root):
    if (root is None) or (root.right is None):
        return root
    return merge_node(root, flatten(root.right))