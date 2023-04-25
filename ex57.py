# Rotate linked list
# define the linked list data structure
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  # representation function for seeing the linked list:
  def __repr__(self):
    return f"({self.value}, {self.next})"


def rotate(node, n):
    length = 0                 # rotate linked list by the modulo of its length:
    current = node
    while current != None:
        current = current.next
        length += 1
    n = n % length

    slow, fast = node,node
    for i in range(n):
        fast = fast.next

    while fast.next != None:    # stop before the end of the linked list (reduce time complexity)
        slow = slow.next
        fast = fast.next

    fast.next = node
    head = slow.next
    slow.next = None

    return head


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(rotate(node, 2))