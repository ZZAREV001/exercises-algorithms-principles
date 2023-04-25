# Find the K-th largest element in a list:
import heapq
import random


class Solution(object):
    # Brute force solution O(n.log(n)):
    def findKithLargest(self, nums, k):
        return sorted(nums)[len(nums) - k]

    # Heap data structure solution for this problem O(k.log(n)) where k is an integer:
    def findKithLargest2(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # Quick - select algorithm (partitioning). It is O(n) time:
    def findKithLargest3(self, nums, k):
        def select(list, left, right, index):
            def select(list, left, right, index):
                if left == right:
                    return list[left]
                pivot_index = random.randint(left, right)
                # move pivot to the beginning of list
                list[left], list[pivot_index] = list[pivot_index], list[left]
                # partition
                i = left
                for j in range(left + 1, right + 1):
                    if list[j] < list[left]:
                        i += 1
                        list[i], list[j] = list[j], list[i]
                # move pivot to the correct location
                list[i], list[left] = list[left], list[i]
                # recursively partition one side
                if index == i:
                    return list[i]
                elif index < i:
                    return select(list, left, i - 1, index)
                else:
                    return select(list, i + 1, right, index)

            return select(nums, 0, len(nums) - 1, len(nums) - k)

        return select(nums, 0, len(nums) - 1, k)


print(Solution().findKithLargest([3, 5, 2, 4, 6, 8], 3))
print(Solution().findKithLargest2([3, 5, 2, 4, 6, 8], 3))
print(Solution().findKithLargest3([3, 5, 2, 4, 6, 8], 3))