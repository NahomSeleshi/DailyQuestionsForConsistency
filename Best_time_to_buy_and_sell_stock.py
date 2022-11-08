class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min, max_profit = prices[0], 0
        for each in prices:
            if each < cur_min:
                cur_min = each
            else:
                max_profit = max(max_profit, each-cur_min)
        return max_profit