class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next_right = None

class Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def ()