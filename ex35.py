# Get all values at a certain height in a binary tree
# always define the data structure (here the binary tree):
class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def valueAtLevel(self, node, depth):
        if not node:
            return []
        if depth == 1:
            return [node.value]

        return self.valueAtLevel(node.left, depth - 1) + self.valueAtLevel(node.right, depth + 1)


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)

print(Solution().valueAtLevel(node, 3))
# expected answer [4, 5, 7] array
