# Count number of unival subtrees
# definition of the data structure:
class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def count_unival_subtrees(node):
    count, is_unival = count_unival_subtrees_helper(node)
    return count

def count_unival_subtrees_helper(node):
    if not node:
        return 0, True  # if left node doesn't exist, we should consider the unival tree

    left_count, is_left_unival = count_unival_subtrees_helper(node.left)
    right_count, is_right_unival = count_unival_subtrees_helper(node.right)

    if is_left_unival and is_right_unival and (not node.left or node.val == node.left.val) \
            and (not node.right or node.val == node.right.val):
        return left_count + right_count + 1, True

    return left_count + right_count, False  # otherwise we return them with false because it is not an unival tree


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# expected 5 subtrees