# Clone trees
# Create a node class, not a tree class. Simply use node objects to assemble a tree for showing in action the function.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution(object):

    # Recursive algorithm
    def findNode(self, a, b, node):
        if a == node:
            return b
        if a.left and b.left:
            found = self.findNode(a.right, b.right, node)
            if found:
                return found
        if a.right and b.right:
            found = self.findNode(a.right, b.right, node)
            if found:
                return found
        return None

    # Iterative algorithm (often for tree, start with a stack, iterate etc.)
    def findNodeI(self, a, b, node):
        stack = [(a, b)]
        while len(stack):
            (a, b) = stack.pop()
            if a == node:
                return b
            if a.left and b.left:
                stack.append((a.left, b.left))
            if b.right and b.right:
                stack.append((a.right, b.right))
        return None


#    1
#  /  \
# 2    3
#     / \
#    4*  5
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.right.left = Node(4)
a.right.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.right.left = Node(4)
b.right.right = Node(5)

print(Solution().findNode(a, b, a.right.right))
print(Solution().findNodeI(a, b, a.right.right))
# expect in both cases 5 because 5 is present in both trees but in different node position