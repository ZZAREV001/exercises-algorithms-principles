import heapq

# Quickselect (iterative)

# Brute force approach:
def findKthLargest(arr, k):
    for i in range(0, k):
        (max_value, max_index) = (arr[0], 0)
        for j in range(0, len(arr)):
            if max_value < arr[j]:
                (max_value, max_index) = arr[j], j
        arr = arr[:max_index] + arr[max_index + 1:]
    for j in range(0, len(arr)):
        if max_value < arr[j]:
            (max_value, max_index) = arr[j], j
    return max_value

# Sorted version approach:
def findKthLargest2(arr, k):
    return sorted(arr)[-k]

# Heap data structure approach:
def findKthLargest2(arr, k):
    arr = list(map(lambda x: -x, arr))
    heapq.heapify(arr)
    for i in range(0, k):
        heapq.heappop(arr)
    return -arr[k]

# Quickselect algorithm approach:
def partition(arr, low, high):   # parameters: array composite type, low / high integer primitive types
  pivot = arr[high]    # primitive integer type stored in pivot variable: take index at value high
  i = low              # primitive integer type stored in i variable
  for j in range(low, high):       # traverse set that begins to low and end to high
    if arr[j] <= pivot:            # operation on the set of the indices of the array: as soon as index is equal to high index do this:
      arr[i], arr[j] = arr[j], arr[i]    # traverse set of values of array by using j and assigning value of low.
      i += 1                             # increment i in order to advance.
  arr[i], arr[high] = arr[high], arr[i]  # increment the set of values of array and assign the value at index high.
  return i                               # return the index that make the partition in the set of values of the array.

def quickselect(arr, k):    # parameters: array composite type, k integer primitive type.
  k = len(arr) - k        # integer primitive type: number of items in the composite type array minus k the integer.
  left = 0                # integer primitive type sets to 0.
  right = len(arr) - 1    # integer primitive type: number of items in the composite type minus 1.

  while left <= right:      # compare values stored in the primitive types
    pivotIndex = partition(arr, left, right)  # composite type: function partition() is a mapping the partition index from the set of indices of the array arr
    if pivotIndex == k:                       # conditional operation: if the partition index is equal to parameter k (primitive integer type), do this:
      return arr[pivotIndex]        # return values (primitive integer type) from the set of values of variable arr.
    elif pivotIndex > k:            # conditional operation: if the partition index is superior to parameter k, do this:
      right = pivotIndex - 1             # assign the partition index minus 1 to right variable (primitive integer type).
    else:                           # conditional operation else:
      left = pivotIndex + 1              # assign partition index minus 1 to left variable (primitive integer type).
  return -1                         # no cases operations between sets produced, so return -1. Algorithm stops.


print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))
print(findKthLargest2([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))
print(findKthLargest2([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 4))
print(quickselect([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))