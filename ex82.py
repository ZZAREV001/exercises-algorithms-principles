# Consecutive Bit ones
class Solution(object):

    @staticmethod
    def longest_run(n):
        longest_run = 0
        current_run = 0
        BITMASK = 1

        while n != 0:
            if n & BITMASK == 0:
                longest_run = max(longest_run, current_run)
                current_run = 0
            else:
                current_run += 1
            n = n >> 1
        longest_run = max(longest_run, current_run)
        return longest_run


print(Solution().longest_run(242))
# expect 4 because 242 integer is 11110010 in binary and has a sequence of 4 consecutive 1.