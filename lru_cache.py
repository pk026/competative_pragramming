class Node:

    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.next = None
        self.previous = None


class Queue:

    def __init__(self, length):
        self.front = Node()
        self.rear = self.front
        for i in xrange(length-1):
            self.rear.next = Node()
            self.rear.next.previous = self.rear
            self.rear = self.rear.next

    def print_nodes(self):
        temp = self.front
        while temp:
            # if temp.previous:
            #     print "previous_data", temp.previous.key
            print "data", temp.key
            # if temp.next:
            #     print "next_data", temp.next.key
            temp = temp.next

    def remove_from_rear(self):
        self.rear = self.rear.previous
        self.rear.next = None

    def add_to_front(self, temp_node):
        self.front.previous = temp_node
        temp_node.next = self.front
        self.front = temp_node

    def move_to_front(self, value_node):
        value_node.previous.next = value_node.next
        value_node.next.previous = value_node.previous
        self.front.previous = value_node
        value_node.next = self.front
        self.front = value_node

class Cache:

    def __init__(self, length):
        self.q = Queue(length)
        self.data_store = dict()

    def print_cache_state(self):
        self.q.print_nodes()

    def put(self, key, value):
        value_node = self.data_store.get(key)
        if value_node:
            value_node.data = value
            self.q.move_to_front(value_node)
        else:
            temp_node = Node(key, value)
            self.data_store[key] = temp_node
            self.q.add_to_front(temp_node)
            if self.q.rear.key:
                del self.data_store[self.q.rear.key]
            self.q.remove_from_rear()

    def get(self, key):
        value_node = self.data_store.get(key)
        if value_node:
            if value_node!=self.q.front:
                self.q.move_to_front(value_node)
            return value_node.data
        return -1

if __name__ == "__main__":
    cache = Cache(5)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(1, 10)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(2, 20)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(3, 30)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 3", cache.get(3)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(4, 40)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 1", cache.get(1)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 2", cache.get(2)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(5, 50)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(6, 60)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    cache.put(7, 70)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 3", cache.get(3)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 6", cache.get(6)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"
    print "get data with key 10", cache.get(10)
    cache.print_cache_state()
    print ">>>>>>>>>>>>>>>>test"