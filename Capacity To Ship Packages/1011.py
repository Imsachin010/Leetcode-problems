class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 5 * (10**4) * 500

        def good(target):
            current = target
            used_days = 1

            for x in weights:
                if current < x:
                    current = target
                    used_days +=1
                
                current -=x
                if current <0:
                    return False
            
            return used_days <= days
        
        while left<right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid +1

        return left