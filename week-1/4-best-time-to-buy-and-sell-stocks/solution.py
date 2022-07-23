class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 2**31
        
        max_profit = 0
        for price in prices:
            cur_min = min(cur_min, price)
            max_profit = max(max_profit, price-cur_min)
        
        return max_profit