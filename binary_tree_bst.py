class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(node, left_node, right_node):
    if node is None:
        return True
    if (left_node is not None and node.data < left_node.data):
        return False
    if (right_node is not None and node.data > right_node.data):
        return False
    return (
        isBST(node.left, node.left.left, node.left.right) and
        isBST(node.right, node.right.left, node.right.right)
    )
# Time Complexity: O(n)
# Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)