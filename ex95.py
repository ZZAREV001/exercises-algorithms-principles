# Group words that are anagrams
import collections


class Solution(object):
    def groupAnagramWords(self, strs):
        groups = collections.defaultdict(list)   # hashmap is here
        for s in strs:
            groups[self.hashKey(s)].append(s)
        return groups.values()

    # More efficient version of the hashing function
    def hashKey_2(self, str):
        array = [0] * 26  # create the array with 26 characters of the alphabet
        for c in str:
            array[ord(c) - ord('a')] = 1
        return tuple(array)

    # Brute force approach of the hashing function (sort every incoming string)
    def hashKey(self, str):
        return ''.join(sorted(str))


print(Solution().groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# expect matrix [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]