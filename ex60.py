# Remove duplicate from linked list
# Definition of the linked list:
class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_duplicates(node):
    current = node

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next


node = Node(1, Node(2, Node(2, Node(3, Node(3)))))
print(remove_duplicates(node))