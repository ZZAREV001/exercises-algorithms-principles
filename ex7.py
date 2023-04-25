# Given an unsorted array of integers, we have to sort it with 3 unique numbers
class Solution7():
    # iterative approach with hashmap data structure incorporation. O(n) space and O(n) time
    def sortNums(self, nums):
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        return ([1] * counts.get(1, 0) +      # Return the 3 unique numbers 1, 2 and 3
                [2] * counts.get(2, 0) +
                [3] * counts.get(3, 0))

    # iterative approach with swaps index according to the value of each unique numbers
    # advantage of this approach: O(k) space but O(n) time.
    def sortNums2(self, nums):
        one_index = 0
        three_index = len(nums) - 1
        index = 0
        while index <= three_index:
            if nums[index] == 1:
                nums[index], nums[one_index] = nums[one_index], nums[index]    # swap here
                one_index += 1
                index += 1
            if nums[index] == 2:
                index += 1
            if nums[index] == 3:
                nums[index], nums[three_index] = nums[three_index], nums[index]   # swap here
                three_index -= 1
        return nums


print(Solution7().sortNums([3, 3, 2, 1, 3, 2, 1]))
print(Solution7().sortNums2([3, 3, 2, 1, 3, 2, 1]))