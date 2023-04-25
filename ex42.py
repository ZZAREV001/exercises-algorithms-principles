# Balanced binary tree
# Define the binary tree data structure (how it looks like):
class Node(object):
    def __int__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, n):
        return self._isBalancedHelper(n)[0]

    # return value (isBalanced, height)
    def _isBalancedHelper(self, n):
        if not n:
            return (True, 0)

        lBalanced, lHeight = self._isBalancedHelper(n.left)
        rBalanced, rHeight = self._isBalancedHelper(n.right)
        return (lBalanced and rBalanced and abs(lHeight - rHeight <= 1,
                                                max(lHeight, rHeight) + 1))


n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
#     1
#    / \
#   2   3
#  /
# 4
print(Solution().isBalanced(n))
