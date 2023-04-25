# Unique path: with recursive approach and then dynamic programming approach:
class Solution(object):
    # recursive approach is O(2^m*n) time complexity
    def uniquePath(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePath(m - 1, n) + self.uniquePath(m, n - 1)

    # dynamic programming is O(m*n) time complexity
    def uniquePathDP(self, m, n):
        cache = [[0] * n] * m    # create the cache and initialize it to 0 (2D matrix will have 0 everywhere)
        for i in range(m):
            cache[i][0] = 1
        for j in range(n):
            cache[0][j] = 1

        for c in range(1, m):
            for r in range(1, n):
                cache[c][r] = cache[r][r - 1] + cache[c - 1][r]
        return cache[-1][-1]


print(Solution().uniquePath(5, 3))
print(Solution().uniquePathDP(5, 3))
# expected result is 15 in both case
