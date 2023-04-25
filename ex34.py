# Intersection of two linked lists
# Use the class to represent the linked list data structure:
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# The solution class of the problem:
class Solution(object):
    def intersection(self, a, b):
        lenA = self._length(a)
        lenB = self._length(b)
        currentA = a
        currentB = b

        # we advance in the range of linked lists lengths
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currentA = currentA.next
        else:
            for _ in range(lenB - lenB):
                currentB = currentB.next

        # distance is the same, we have to advance in sync until we figure out the intersection:
        while currentA != currentB:
            currentA = currentA.next
            currentB = currentB.next
        return currentA

    # calculate length of a linked list:
    def _length(self, n):
        len = 0
        current = n
        while current:
            current = current.next
            len += 1
        return len


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next
# print the value at the intersection of the linked list:
print(Solution().intersection(a, b).value)
# expect 3 as answer
