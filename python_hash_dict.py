class Node:
    def __init__(self, key_data, value_data):
        self.k = key_data
        self.v = value_data
        self.next = None

    def getKey(self):
        return self.k

    def getValue(self):
        return self.v

    def getNext(self):
        return self.next

    def setData(self, key_data, value_data):
        self.k = key_data
        self.v = value_data

    def setNext(self, newnext):
        self.next = newnext


class PythonList:

    def __init__(self):
        self.head = None

    def add(self, key_data, value_data):
        temp = Node(key_data, value_data)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getKey() == item:
                found = True
            else:
                current = current.getNext()
        return current


def hash_function(data, array_size):
    #import ipdb; ipdb.set_trace(    )
    hash_code = 0
    for lit in data:
        hash_code += ord(lit)
    hash_code = hash_code % array_size
    return hash_code

hash_bucket = [None] * 11

def make_hash_table(python_dict):
    for k, v in python_dict.items():
        hash_code = hash_function(k, 11)
        if hash_bucket[hash_code] is None:
            value_list = PythonList()
            value_list.add(k, v)
            hash_bucket[hash_code] = value_list
        else:
            hash_bucket[hash_code].add(k, v)

def get_dict_value_from_hash(key):
    hash_code = hash_function(key, 11)
    bucket = hash_bucket[hash_code]
    node = bucket.search(key)
    return node.v


python_dict = {'mod': 12, 'dom': 13, 'pramod': 0}
make_hash_table(python_dict)
print get_dict_value_from_hash('mod')
print get_dict_value_from_hash('dom')
print get_dict_value_from_hash('pramod')