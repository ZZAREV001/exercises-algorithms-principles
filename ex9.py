# Find the non-duplicate number in an array
class Solution(object):
    # First solution: iterative approach
    def singleNumber(self, nums):
        occurrence = {}   # create the hash map

        for n in nums:
            occurrence[n] = occurrence.get(n, 0) + 1   # insert the occurrence in the hash map

        for key, value in occurrence.items():      # iterate in the hash map
            if value == 1:
                return key   # return the value

    # Second solution: iterative approach with XOR operator (reduce space complexity to O(1))
    def singleNumber2(self, nums):
        unique = 0   # create a variable for storing the unique number
        for n in nums:
            unique ^= n 
        return unique    


Solution().singleNumber([4, 3, 2, 4, 1, 3, 2])
Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2])
