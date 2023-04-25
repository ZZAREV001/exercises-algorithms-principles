# Product of array except self
class Solution:

    def productExceptSelf(self, nums):
        right = [1] * len(nums)
        prod = 1                                  # start product at 1.
        for i in range(len(nums) -2, -1, -1):     # range -1 with -2 steps. With this we can advance in right part in the products of each values.
            prod *= nums[i + 1]
            right[i] = prod            # store in pre-computed array

        prod = 1
        for i in range(1, len(nums)):            # left side with range from index 1 to the length of nums array
            prod *= nums[i - 1]
            right[i] *= prod

        return right                  # return right array


print(Solution().productExceptSelf([1, 2, 3, 4]))