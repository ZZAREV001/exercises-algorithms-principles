# Max profit calculation for stocks (at which price should we buy a stock to maximize profit?)
class Solution(object):

    # brute force approach:
    def buy_and_sell(self, arr):
        max_profit = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                max_profit = max(max_profit, arr[j] - arr[i])
        return max_profit

    # Iterative approach more efficient: O(n) with n number of iterations
    def buy_and_sellI(self, arr):
        max_current_price = 0
        max_profit = 0

        for price in arr[::-1]:
            max_current_price = max(max_current_price, price)
            max_profit = max(max_profit, max_current_price - price)
        return max_profit


print(Solution().buy_and_sell([9, 11, 8, 5, 7, 10]))
print(Solution().buy_and_sellI([9, 11, 8, 5, 7, 10]))