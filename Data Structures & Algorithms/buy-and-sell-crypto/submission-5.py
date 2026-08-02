class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mini = min(prices)
        # maxi = max(prices)
        # if prices.index(mini) == (len(prices)-1):
        #     return 0
        # else:
        #     prices = prices[mini:]
        #     if prices:
        #         maxi = max(prices)
        #         if prices and maxi and (maxi > mini):
        #             return maxi-mini
        #         else:
        #             return 0
        #     else:
        #         return 0


        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        return max_profit
    