# Array intersection (arrays are called nums1 and nums2):
class Solution:
    # Brute force approach:
    @staticmethod
    def intersection1(nums1, nums2):
        results = {}
        for num in nums1:
            if num in nums2 and num not in results:
                results[num] = 1
        return list(results.keys())   # return the keys of the hashmap

    # Iterative approach with Python built-in (avoid this in coding interview):
    @staticmethod
    def intersection2(nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]

    # Iterative approach with two hashmaps (linear time, more efficient solution):
    @staticmethod
    def intersection3(nums1, nums2):
        storingHashmap = {}
        duplicates = {}
        for i in nums1:
            storingHashmap[i] = 1
        for i in nums2:
            if i in storingHashmap:
               duplicates[i] = 1

        return tuple(duplicates.keys())


print(Solution().intersection1([4, 9, 5], [9, 4, 9, 8, 4]))
print(Solution().intersection2([4, 9, 5], [9, 4, 9, 8, 4]))
print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
