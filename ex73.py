# Checking balanced binary tree
# definition of binary tree data structure:
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def tree_height(node):
    if node is None:
        return 0

    heightLeft = tree_height(node.left)
    heightRight = tree_height(node.right)

    if heightLeft >= 0 and heightRight >= 0 and abs(heightLeft - heightRight) <= 1:
        return max(heightLeft, heightRight) + 1
    return -1

def is_tree_balanced(node):
    return tree_height(node) != -1


n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)
#     1
#    / \
#   2   3
#  /
# 4
print(is_tree_balanced(n1))
# Expected True

n4 = Node(4)
n2 = Node(2, n4)
n1 = Node(1, n2, None)
#     1
#    /
#   2
#  /
# 4
print(is_tree_balanced(n1))
# Expected False
