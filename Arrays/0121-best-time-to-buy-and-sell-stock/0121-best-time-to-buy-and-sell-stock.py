class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        min_buy = prices[0]
        ans = 0

        for i in range(1, n):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                ans = max(ans, prices[i]-min_buy)
        return ans
