# Word concatenation (dynamic programming approach)
class Solution(object):
    def findAllConcatenatedWord(self, words):
        wordsDict = set(words)
        cache = {}  # here is the set for memorization
        return [word for word in words if self._canForm(word, wordsDict, cache)]

    def _canForm(self, word, wordDict, cache):
        if word in cache:
            return cache[word]
        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in wordDict:
                if suffix in wordDict or self._canForm(suffix, wordDict, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False


input = ["cat", "cats", "dog", "catsdog"]
print(Solution().findAllConcatenatedWord(input))
# expect answer ["catsdog]