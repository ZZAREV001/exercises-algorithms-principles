# Two sum numbers exercise
class Solution(object):
    # Brute force solution: O(n.n) = O(n^2) time and O(1) space
    def twoSum(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]
        return []

    # Other simple iterative approach: O(n) time and O(n) space
    def twoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []


print(Solution().twoSumB([2, 7, 11, 15], 18))