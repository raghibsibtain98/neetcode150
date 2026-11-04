class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_buy = prices[0]
        
        for i in range(1,len(prices)):
            max_profit = max((prices[i]-min_buy),max_profit)
            min_buy = min(min_buy,prices[i])
        
        return max_profit if max_profit >= 0 else 0