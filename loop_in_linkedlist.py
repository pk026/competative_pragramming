class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return 1

    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node
         
        # Count the number of nodes in loop
        k = 1
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1
 
        # Fix one pointer to head
        ptr1 = self.head
         
        # And the other pointer to k nodes after head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next
 
        # Move both pointers at the same place
        # they will meet at loop starting node
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
 
        # Get pointer to the last node
        ptr2 = ptr2.next
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next
 
        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next