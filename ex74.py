# Filter Leaves of a Binary Tree
# definition of the data structure
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value}, ({self.left.__repr__()}, ({self.right.__repr__()})"


def filter(node, n):
  if not node:
    return None

  node.left = filter(node.left, n)
  node.right = filter(node.right, n)

  if node.value != n and not node.left and not node.right:
    return None

  return node


#      1
#    /  \
#   2    1
#  /    /
# 2    1
n1 = Node(1, Node(2, Node(2), Node(1, Node(1))))
print(filter(n1, 2))