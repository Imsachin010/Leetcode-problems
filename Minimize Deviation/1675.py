class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        