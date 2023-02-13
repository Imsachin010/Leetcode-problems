class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def f(x):
            if x <= 0:
                return 0
            
            return (x+1)//2
        return f(high) - f(low-1)