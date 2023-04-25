# Remove zero sum consecutive nodes in a linked list
import collections

class Node(object):        # definition of the data structure
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):    # representation of the linked list
        n = self
        ret = ''
        while n:
            ret += str(n.val)
            n = n.next
        return ret


class Solution:

    @staticmethod
    def removeZeroSumSublists(node):
        sumToNode = collections.OrderedDict()
        sum = 0
        dummy = Node(0)  # creation of a dummy object in order to initialize the head of the linked list
        dummy.next = node
        n = dummy
        while n:
            sum += n.val
            if sum not in sumToNode:
                sumToNode[sum] = n
            else:
                prev = sumToNode[sum]
                prev.next = n.next
                while list(sumToNode.keys())[-1] != sum:
                    sumToNode.popitem()
            n = n.next
        return dummy.next


# linked list: 3 -> 1 -> 2 -> -1 -> -2 -> 4 -> 1
n = Node(3)
n.next = Node(1)
n.next.next = Node(2)
n.next.next.next = Node(-1)
n.next.next.next.next = Node(-2)
n.next.next.next.next.next = Node(4)
n.next.next.next.next.next.next = Node(1)

print(Solution().removeZeroSumSublists(n))
# expect this cleaned linked list: 3 -> 4 -> 1