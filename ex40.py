# Frequent subtree sum (recursive approach)
# Represent the binary tree with its nodes:
from collections import defaultdict


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def most_frequent_subtree_sum(self, root):
        # create the frequencies hashmap
        frequencies = defaultdict(int)
        self._helper_build_frequencies(root, frequencies)

        # second pass and check the maximum value (most common sum is equal to current value):
        most_common_sum = 0
        for k in list(frequencies):
            if frequencies[k] > frequencies[most_common_sum]:
                most_common_sum = k
        return most_common_sum

    # this is the recursive helper function
    def _helper_build_frequencies(self, root, frequencies):
        if root == None:
            return 0

        sum = root.value + self._helper_build_frequencies(root.left, frequencies) \
              + self._helper_build_frequencies(root.right, frequencies)
        frequencies[sum] += 1
        return sum


# Construct our binary tree:
root = Node(3, Node(1), Node(-3))
print(Solution().most_frequent_subtree_sum(root))