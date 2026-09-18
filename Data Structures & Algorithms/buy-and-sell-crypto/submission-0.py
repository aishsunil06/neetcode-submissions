class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = 101
        max_profit = 0
        for i in range(len(prices)):
            sp = prices[i]
            if bp < sp:
                profit = sp - bp
                max_profit = max(max_profit, profit)
            else:
                bp = sp
        return max_profit