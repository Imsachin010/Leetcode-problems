class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        best = 0
        mx = 0
        for i in range(N -1, -1, -1):
            best = max(best,mx- prices[i])
            mx = max(prices[i], mx)
        
        return best