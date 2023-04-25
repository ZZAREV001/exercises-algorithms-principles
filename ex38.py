# Minimum subarray length (dynamic programming approach. Brute force approach has a catastrophic O(n^3) time).
class Solution(object):
    def minSub(self, k, numbers):
        leftIndex = rightIndex = 0
        sum = 0
        minLen = float('inf')    # minimum length start at float infinity

        while rightIndex < len(numbers):
            sum += numbers[rightIndex]   # calculate current sum that we have
            while sum >= k:
                minLen = min(minLen, rightIndex - leftIndex + 1)
                leftIndex += 1
                sum -= numbers[leftIndex]
            rightIndex += 1

        if minLen == float('inf'):     # additional checking statement for big length or empty array
            return 0
        return minLen


print(Solution().minSub(7, [2, 3, 1, 2, 4, 3]))
# expect length of 2