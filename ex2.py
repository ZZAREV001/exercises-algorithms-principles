# Write a function that add two number as a linked list

# Represent partially a linked list with value of the node and its pointer.
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersRecursive(l1, l2, 0)

    def addTwoNumbersRecursive(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next)
        elif c:
            ret.next = Node(c)
        return ret



l1 = Node(1)
l1.next = Node(2)
l1.next = Node(2)

l2 = Node(1)
l2.next = Node(2)
l2.next = Node(2)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val, end = '')
    answer = answer.next