class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r, mx = 0, 1, 0
        while r <= len(prices) - 1:
            mx = max(mx, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return mx