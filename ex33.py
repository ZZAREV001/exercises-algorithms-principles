# Depth of a binary tree:
class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    # Obtain a string representation of the result (see the current value in string format):
    def __repr__(self):
        return self.val


# Recursive approach
def deepest(node, depth=0):
    if not node:
        return 0

    return depth + 1 + max(deepest(node.left), deepest(node.right))


# Recursive approach: more detailed version
def deepest2(node, depth=0):
    if not node:
        return depth + 0

    if not node.left and not node.right:
        return depth + 1

    if not node.left:
        return deepest2(node.right, depth + 1)

    if not node.right:
        return deepest2(node.left, depth + 1)

    return max(deepest2(node.left, depth + 1), deepest2(node.right, depth + 1))


# tree looks like:
#    a
#   / \
#  b   c
# /
# d
#  \
#   e
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('e')
root.right = Node('c')

print(deepest(root))
# expect a depth equals to 4
