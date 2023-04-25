# Reverse linked list
class Node(object):
    def __init__(self, val, next = None):  # Do not create the entire linked list. Only the node.
        self.val = val
        self.next = next
    def __repr__(self):        # Representation class: return the object representation in string format.
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res

class Solution(object):
    def reverse(self, node):
        current = node       # start at the head
        previous = None

        while current != None:     # Pointer manipulation that is O(k) space
            temp = current.next    # these operations reverse pointer direction of the linked list
            current.next = previous
            previous = current
            current = temp
        return previous

# Pass node value to the linked list and apply the function
node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(Solution().reverse(node))