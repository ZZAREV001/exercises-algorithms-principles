# Longest increasing subsequence (dynamic programming approach):
class Solution(object):
    def longestIncreasingSubsequence(self, array):
        cache = [1] * len(array)
        for i in range(1, len(array)):   # iterate from 1 to the end of the array (it's length)
            for j in range(i):           # iterate the indices in the input array
                if array[i] < array[j]:
                    cache[i] = max(cache[i], cache[j] + 1)     # assign the value according to the comparison
        return max(cache)


array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]
print(Solution().longestIncreasingSubsequence(array))
# expect a length of 5 here
