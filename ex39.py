# Search value in a matrix (idea: apply binary search to matrix)
class Solution(object):

    def searchMatrix(self, mat, value):
        # we need the dimension
        if len(mat) == 0:
            return False
        rows = len(mat)
        cols = len(mat[0])

        # initialize constants and compute the middle point in the matrix:
        low = 0
        high = rows * cols
        while low < high:
            mid = (low + high) // 2
            mid_value = mat[mid // cols][mid % cols]

            if mid_value == value:
               return True
            # otherwise, bisect the array:
            if mid_value < value:
                low = mid + 1
            else:
                high = mid
        return False


mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31]
]
print(Solution().searchMatrix(mat, 4))
# expect false
print(Solution().searchMatrix(mat, 10))
# expect true