class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def solve(arr):
            M = len(arr)
            minx = collections.deque()
            maxx = collections.deque()

            for i in range(M):
                if arr[i] == minK:
                    minx.append(i)
                if arr[i] == maxK:
                    maxx.append(i)
            
            total = 0
            for i in range(M):
                while len(minx) > 0 and minx[0] < i:
                    minx.popleft()
                while len(maxx) > 0 and maxx[0] < i:
                    maxx.popleft()
                if len(minx) == 0 or len(maxx) == 0:
                    break

                nx = max(minx[0], maxx[0])
                total += M -nx
            return total 

        