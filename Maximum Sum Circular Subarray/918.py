class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        best=max(nums)
        s = sum(nums)
        def kadane(nums):
            best = max(nums)
            current = 0
            for i in range(N):
                current += nums[i]
                best = max(best, current)
                if current < 0:
                    current = 0
            return best
        best = max(best,kadane(nums))
        if any(x >= 0 for x in nums):
            bestnegative = -kadane(list(-x for x in nums))
            best = max(best,s- bestnegative)
        return best
        