class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10 ** 15
        def good(target):
            hours = 0
            for x in piles:
                hours += ((x + target -1) // target)
            return hours <= h
        
        while left < right:

            mid = (left + right) // 2

            if good(mid):
                right = mid 
            else:
                left = mid + 1
        return left 