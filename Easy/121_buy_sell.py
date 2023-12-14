"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

"""
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        buy_pointer, sell_pointer = 0, 1
        max_profit = 0

        while sell_pointer < len(prices):
            current_profit = prices[buy_pointer] - prices[sell_pointer]
            if current_profit > 0:
                max_profit = max(current_profit, max_profit)
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1

        return max_profit

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            current_profit = i - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        local_max, global_max = 0, 0

        for i in range(1, len(prices)):
            # If prices[i] - prices[i-1] > 0, add to local_max to reflect increased profit
            # Else reset local_max to 0
            local_max = max(0, local_max + prices[i] - prices[i-1])
            global_max = max(local_max, global_max)

        return global_max

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))