class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_balanced(root, height):
    lh = 0
    rh = 0
    