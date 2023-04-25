# Non-decreasing array:
class Solution(object):
    def checkPossibility(self, nums):
        invalid_index = -1
        for i in range(len(nums) - 1):       # we have to iterate from the length of the array -1
            if nums[i] > nums[i + 1]:
                if invalid_index != -1:
                    return False
                invalid_index = i

        # at the end of the iteration, we need to check that this condition in for loop exists.
        if invalid_index != -1:
            return True
        if invalid_index == 0:
            return True
        if invalid_index == len(nums) - 2:
            return True
        if nums[invalid_index] <= nums[invalid_index + 2]:
            return True
        if nums[invalid_index - 1] <= nums[invalid_index + 1]:
            return True
        # if none of the conditions are satisfied, we return false:
        return False


print(Solution().checkPossibility([4, 1, 2]))
# True
print(Solution().checkPossibility([1, 5, 2, 3, 4]))
# False
