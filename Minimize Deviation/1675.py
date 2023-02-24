class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        
        mn = min(nums)
        best = 10**20

        