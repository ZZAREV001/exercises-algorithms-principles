# First and Last Indices of an Element in a Sorted Array
class Solution:
    def getRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearch(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    # Recursive approach to solve the sub problem
    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid     # check is that midpoint value equal to the target number that we're looking for.
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid + 1, target, findFirst)
        else:
            if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
                return mid     # check is that midpoint value equal to the target number that we're looking for.
            if target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

    # Iterative approach to solve the subproblem
    def binarySearchIterative(self, arr, low, high, target, findFirst):
      while True:
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid     # check is that midpoint value equal to the target number that we're looking for.
            if target > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
                return mid     # check is that midpoint value equal to the target number that we're looking for.
            if target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1


arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
x = 9
print(Solution().getRange(arr, 9))
