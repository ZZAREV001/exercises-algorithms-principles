# Number of 1 bits: give number of bits of any decimal number
class Solution(object):
    def oneBits(self, number):
        count = 0
        while number > 0:
            if number & 1:
                count = count + 1
            number = number >> 1
        return count


print(Solution().oneBits(23))
# expect 0b10111


