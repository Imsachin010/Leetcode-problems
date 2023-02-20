class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid +1

        ans = left 
        return ans