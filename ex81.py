# Fixed point
# Recursive approach
def find_fixed_points_helper(low, high, nums):
    if low == high:
        return None

    mid = int((low + high) / 2)
    if nums[mid] == mid:
        return mid
    if nums[mid] < mid:
        return find_fixed_points_helper(mid+1, high, nums)
    else:
        return find_fixed_points_helper(low, mid, nums)


def find_fixed_points(nums):
    return find_fixed_points_helper(0, len(nums), nums)


print(find_fixed_points([-5, 1, 3, 4]))
# expect 1 (1 value is equal to its index)


def find_fixed_points_iterative(nums): # we have O(ln(2)) time due to binary search sorting which subdivided
    low = 0
    high = len(nums)

    while (low != high):
        mid = int((low + high) / 2)
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            low = mid + 1
        else:
            high = mid

    return None


print(find_fixed_points_iterative([-5, 1, 3, 4]))
# expect 1 (1 value is equal to its index)