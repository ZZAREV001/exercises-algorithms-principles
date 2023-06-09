# Find subtree (backtracking solution)
# Define tree data structure:
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


n = Node(1)
n.left = Node(4)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(2)
n.right.left = Node(4)
n.right.right = Node(1)

b = Node(4)
b.left = Node(3)
b.right = Node(2)

def pre_order(n):
    if not n:
        return 'null'
    return '-' + str(n.value) + '-' + pre_order(n.left) + '-' + pre_order(n.right)


def find_subtree(a, b):
    return pre_order(b) in pre_order(a)

def find_subtree_2(a, b):
    if not a:
        return False

    is_match = a.value == b.value

    if is_match:
        is_match_left = (not a.left or not b.left) or find_subtree_2(a.left, b.left)
        if is_match_left:
            is_match_right = (not a.right or not b.right) or find_subtree_2(a.right, b.right)
            if is_match_right:
                return True

    return find_subtree_2(a.left, b) or find_subtree_2(a.right, b)


print(find_subtree(n, b))