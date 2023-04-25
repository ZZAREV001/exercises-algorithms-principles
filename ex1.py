# Write a function that checks if a binary tree is valid according to its property

# Establish the data structure (here the binary tree)
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if ((val > low and val < high) and
                self._isValidBSTHelper(n.left, low, n.val) and
                self._isValidBSTHelper(n.right, n.val, high)):
            return True
        return False

    def _isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))


#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution()._isValidBST(node))

#   45
#  /  \
# 89   23
node = Node(45)
node.left = Node(89)
node.right = Node(23)
print(Solution()._isValidBST(node))
