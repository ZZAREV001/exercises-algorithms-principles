# Inorder successor
class Node:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


class Solution(object):

    @staticmethod
    def in_order_successor(node):
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        curr = node
        parent = curr.parent
        while parent and parent.left != curr:
            curr = parent
            parent = parent.parent      # end of the while loop gives us the solution
        return parent





tree = Node(4)
tree.left = Node(2)
tree.right = Node(8)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(7)
tree.right.right.parent = tree.right
tree.right.left = Node(5)
tree.right.left.parent = tree.right
tree.right.left.right = Node(7)
tree.right.left.right.parent = tree.right.left
tree.right.right = Node(9)
tree.right.right.parent = tree.right
#     4
#    / \
#   2   8
#  /   / \
# 1   5   9
#      \
#       7
print(Solution().in_order_successor(tree.right))
# expect 9
print(Solution().in_order_successor(tree.left))
# expect 4
print(Solution().in_order_successor(tree.right.left.right))
# expect 8