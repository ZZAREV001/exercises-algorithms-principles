# Ransom note
from collections import defaultdict

# Write a function that returns a boolean if we can spell a word depending on received strings.
# Entry: word / Magazine: array of characters.
class Solution3(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)    # initialize hash map
        for char in magazine:         # traverse and count occurrence in magazine array
            letters[char] += 1

        for char in note:                # traverse the given word
            if letters[char] <= 0:
                return False          # can't spell
            letters[char] -= 1           # decrement the word by 1

        return True                   # can spell


print(Solution3().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# expect true

print(Solution3().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# expect false


