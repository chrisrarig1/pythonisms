class LinkedList:
    def __init__(self, list=None):
        self.head = None
        if list:
            for i in reversed(list):
                self.insert(i)
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __iter__(self):
        def gen():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return gen()
    
    def __eq__(self, other):
        return list(self) == list(other)

    # def __bool__(self):
    #     return self.head

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

if __name__== "__main__":
    pass