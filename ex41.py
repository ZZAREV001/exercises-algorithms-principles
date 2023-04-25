# Merge list of numbers into ranges
class Solution(object):

    def findRanges(self, nums):
        # edge case:
        if not nums:
            return []

        ranges = []
        low = nums[0]
        high = nums[0]
        for n in nums:
            if high + 1 < n:
                ranges.append(self._makeRange(low, high))
                low = n
            high = n
        ranges.append(self._makeRange(low, high))
        return ranges

    def _makeRange(self, low, high):
        return str(low) + '-' + str(high)


print(Solution().findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))







