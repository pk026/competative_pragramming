class LinkListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = LinkListNode(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def traverse(self):
        current = self.head
        while current != None:
            print current.data
            current = current.getNext()
L1 = LinkedList()
L1.add(9)
L1.add(9)
L1.add(9)
L1.add(9)
L1.add(9)
L1.add(9)

L2 = LinkedList()
L2.add(8)
L2.add(8)
L2.add(8)
L2.add(8)
L2.add(8)
L2.add(8)

def add_numbers_in_linked_list(L1, L2):
    L3 = LinkedList()
    carry_over = 0
    l1_current_node = L1.head
    l2_current_node = L2.head
    while l1_current_node or l2_current_node or carry_over:
        sum_value = carry_over
        if l2_current_node:
            sum_value += l2_current_node.data
        if l1_current_node:
            sum_value += l2_current_node.data
        L3.add(sum_value % 10)
        carry_over = sum_value//10
        if l1_current_node:
            l1_current_node = l1_current_node.getNext()
        if l2_current_node:
            l2_current_node = l2_current_node.getNext()
    return L3