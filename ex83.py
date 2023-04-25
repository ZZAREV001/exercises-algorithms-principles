# Partition a list
# Iterative approach: O(n) time with n size of the input. O(1) constant space (only two simple variables low and high).
def partition(nums, k):
    low = 0
    high = len(nums) - 1
    i = 0

    while i < high:
        n = nums[i]
        if n > k:
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1
        if n < k:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        if n == k:
            i += 1

    return nums

# Brute force approach
def partition_0(nums, k):
    return sorted(nums)

# Iterative approach (linear time and linear space)
def partition_1(nums, k):
    a = []
    b = []
    for n in nums:
        if n < k:
            a.append(n)
        else:
            b.append(n)
    return a + b


print(partition([99, 8, 9, 9, 2, 4, 1, 0, 77], 3))
print(partition_0([99, 8, 9, 9, 2, 4, 1, 0, 77], 3))
print(partition_1([99, 8, 9, 9, 2, 4, 1, 0, 77], 3))