# Optimized list sum
class ListFastSum(object):
    def __init__(self, nums):
        self.pre = [0]

        sum = 0
        for num in nums:
            sum += num
            self.pre.append(sum)

    def sum(self, start, end):
        return self.pre[end] - self.pre[start]


print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))