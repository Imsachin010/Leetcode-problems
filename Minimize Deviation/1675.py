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

        while heap[0] %2 ==0:
            mx = -heapq.heappop(heap)

            best = min(best, mx-mn)

            heapq.heappush(heap, -(mx//2))
            mn = min(mn,mx//2)
        mx = -heap[0]
        best = min(best, mx-mn)
        return best