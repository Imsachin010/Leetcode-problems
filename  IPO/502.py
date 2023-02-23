class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = projects = collections.deque(sorted(list(zip(profits,capital))))
        selectable = []

        N = len(projects)
        k = min(k, N)
        current = w
        for _  in range(k):
            while len(projects) > 0 and projects[0][1]<= current:
                heapq.heappush(selectable, -projects[0][0])
                projects.poplleft()
            
            if len(selectable) > 0:
                current += -heapq.heappop(selectable)
        
        return current