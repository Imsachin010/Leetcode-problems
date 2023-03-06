class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)

        def good(x):
            return arr[x] - x - 1>=k
        
        while left < right :
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left= mid + 1
        missing = arr[left-1] - left 
        offset = k -missing
        return arr[left -1] + offset
                