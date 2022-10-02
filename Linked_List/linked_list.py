

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def add_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, node):
        pass

    def add_tail(self, node):
        pass
