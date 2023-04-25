# Climbing stairs (dynamic programming: solved by underlying existence of Fibonacci sequence)
class Solution(object):
    # Recursive approach:
    def stairecase(self, n):
        if n <= 1:
            return 1
        return self.stairecase(n - 1) + self.stairecase(n - 2)

    # Iterative approach:
    def staircase_2(self, n):
        prev = 1
        prevPrev = 1
        current = 1

        for i in range(2, n + 1):
            current = prev + prevPrev
            prevPrev = prev
            prev = current
        return current


print(Solution().stairecase(5))
# expect 8
print(Solution().staircase_2(5))
# expect 8