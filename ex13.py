# Given an array of integers, find the Pythagorian triplets
class Solution():

    # Brute force: O(n^3) time and O(1) space
    def findPythagorianTriplet(self, nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if a * a + b * b == c * c:
                        return True
        return False

    # Set data structure utilization:
    # space complexity is O(n) bcause we ar creating a set
    # and the size of the set is equal to the length of the input array
    def findPythagorianTriplet2(self, nums):
        squares = set([n * n for n in nums])

        for a in nums:
            for b in nums:
                if a * a + b * b in squares:
                    return True
        return False


print(Solution().findPythagorianTriplet([3, 5, 12, 5, 13]))
print(Solution().findPythagorianTriplet2([3, 5, 12, 5, 13]))