# Number of cousins in a tree
class Node(object): # do not confuse by creating a tree class. We need the node class.
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def _nodes_at_height(self, node, height, exclude):
        if node == None or node == exclude:
            return []
        if height == 0:
            return [node.value]
        return (self._nodes_at_height(node.left, height - 1, exclude)
                + self._nodes_at_height(node.right, height - 1, exclude))


    def _find_node(self, node, target, parent, height=0):
        if not node:  # we don't find the node
            return False
        if node == target:
            return (height, parent)
        return (self._find_node(node.left, target, node, height + 1)
                or self._find_node(node.right, target, node, height + 1))

    def list_cousins(self, node, target):
        height, parent = self._find_node(node, target, None, 0)
        return self._nodes_at_height(node, height, parent)


#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, root.right.right))