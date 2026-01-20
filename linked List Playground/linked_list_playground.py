class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node

class LinkedList():
    def __init__(self, node):
        self.head = node
        self.next = None


my_node = Node("a")
my_node2 = Node("b")

my_node.set_next(my_node2)

print(f"testing: {my_node.value}")
print(f"testing: {my_node.next.value}")

