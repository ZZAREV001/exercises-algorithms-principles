# Jump to the end: give the minimum number of hops.
class Solution(object):
    @staticmethod
    def jumpToEnd(nums):
        hops = [float('inf')] * len(nums)
        hops[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, n + 1):
                if i + j < len(hops):
                    hops[i + j] = min(hops[i + j], hops[i] + 1)
                else:
                    break
        return hops[-1]


print(Solution().jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
