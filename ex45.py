# Invert a binary tree
# define the binary tree data structure:
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

   # print properly the left and right nodes of the binary tree (help debugging faster):
    def __repr__(self):
        result = self.val
        result += f"{self.left}" if self.left else ''
        result += f"{self.right}" if self.right else ''
        return result

class Solution(object):
   def invertTree(self, n):
       if not n:
           return None
       left = self.invertTree(n.left)
       right = self.invertTree(n.right)
       n.right = left
       n.left = right
       return n

   def invertTreeIterativeSol(self, root):
       stack = [root]
       while stack:
           n = stack.pop()
           if n:
               n.right, n.left = n.left, n.right
               stack.extend([n.left, n.right])
       return root


n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')
#      a
#    /   \
#   b     c
#  / \   /
# d   e f
print(n)
print(Solution().invertTree(n))
print(Solution().invertTreeIterativeSol(n))
#      a
#    /   \
#   c     b
#   \   /  \
#    f e    d


