# Distribute bonuses
class Solution(object):
    def getBonues(self, performances):
        count = len(performances)
        bonuses = [1] * count

        for i in range(1, count):
            if performances[i - 1] < performances[i]:  # scanning from left to right
                bonuses[i] = bonuses[i] + 1

        for i in range(count - 2, -1, -1):     # scanning from right to left (inclusive)
            if performances[i + 1] < performances[i]:
                bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

        return bonuses


print(Solution().getBonues([1, 2, 3, 4, 3, 1]))
# expect [1, 2, 3, 4, 2, 1]