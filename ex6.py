# Permutations: given an array of random numbers, find all of the potential permutations of this
class Solution(object):
    # private helper function: solution of the sub problem (start is the start index of the nums array
    def _permuteHelper(self, nums, start = 0):
        # edge case
        if start == len(nums) - 1:
           return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]      # swap here
            result += self._permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]      # swap here
        return result

    def permute(self, nums):
        return self._permuteHelper(nums)

    # Other solution to permute and avoid previous swap operation (recursive approach)
    def permute2(self, nums, values = []):
       if not nums:
           return [values]
       result = []
       for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i + 1:], values + [nums[i]])
       return result


print(Solution().permute([1, 2, 3]))

print(Solution().permute2([1, 2, 3]))
