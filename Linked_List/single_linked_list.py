

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def add_next(self, next_node):
        self.next = next_node


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def add_tail(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
