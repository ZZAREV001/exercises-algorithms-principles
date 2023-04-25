# Anagrams in a string
from collections import defaultdict


class Solution:
    def find_anagrams(self, a, b):
        char_map = defaultdict(int)

        for c in b:
            char_map[c] += 1

        results = []
        for i in range(len(a)):
            c = a[i]

            if i >= len(b):
                c_old = a[i - len(b)]
                char_map[c_old] += 1
                if char_map[c_old] == 0:
                    del char_map[c_old]

            char_map[c] -= 1
            if char_map[c] == 0:
                del char_map[c]

            if i + 1 >= len(b) and len(char_map) == 0:
                results.append(i - len(b) + 1)

        return results


print(Solution().find_anagrams('acdbacdacb', 'abc'))
# expect [3, 7]