class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        
        res = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit >= 0:
                res = max(profit, res)
                r += 1
            else:
                l = r
                r += 1
        return res
