# Autocompletion (trie data structure solves the problem)
class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord  # it is dictionary like { 'a': Node, 'b': Node, ...}
        self.children = children


class Solution():
    def build(self, words):
        trie = Node(False, {})  # construct the trie
        for word in words:
            current = trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node(False, {})
                current = current.children[char]
            current.isWord = True
        self.trie = trie

    def autocomplete(self, word):
        current = self.trie
        for char in word:
            if not char in current.children:
                return []
            current = current.children[char]
        # after this, we do the DFS (crucial step). We may call iterative or recursive version.
        words = []
        self.dfs(current, word, words)
        return words

    # recursive version of Depth First Search algorithm:
    def dfs(self, node, prefix, words):
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            self.dfs_iterative(node.children[char], prefix + char, words)

    # iterative version of Depth First Search algorithm (careful because iterative way needs to keep track two variables)
    def dfs_iterative(self, node, prefix, words):
        stack = [(node, prefix)]
        while len(stack):
            (node, prefix) = stack.pop()
            if node.isWord:
                words.append(prefix)
            for char in node.children:
                child = node.children[char]
                stack.append((child, prefix + char))



s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))

