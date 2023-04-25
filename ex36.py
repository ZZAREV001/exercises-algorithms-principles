# Maximum depth of a tree
# Definition of the tree data structure:
class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    # iterative approach (best approach in linear time and linear space):
    def maxDepth(self, n):
        stack = [(1, n)]     # put nodes in this stack

        max_depth = 0
        while len(stack) > 0:
            depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return max_depth

    # recursive approach (avoid because if the tree is big, the call stack will be overflow)
    def maxDepthRecursive(self, n):
        if not n:
            return 0
        return max(self.maxDepthRecursive(n.left) + 1,
                   self.maxDepthRecursive(n.right) + 1)


n = Node(1)  # root node
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)

print(Solution().maxDepth(n))
print(Solution().maxDepthRecursive(n))
# expect value 3

