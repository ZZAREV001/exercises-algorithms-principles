# Swap every nodes value in a linked list
# Define the data structure of a linked list and its representation:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_node(node):
    current = node
    while current != None and current.next != None:
        current.value, current.next.value = current.next.value, current.value
        current = current.next.next
    return node


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_node(node))
# expect 2, 1, 4, 3, 5