class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = collections.deque()
        best = [[None]* N for _ in range(N)]
        def enqueue(x, y, d):
            best[x][y] = d
            q.append((x,y))
        
        for x in range(N):
            for y in range(N):
                if grid[x][y] ==1:
                    enqueue(x,y,0)
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while len(q)>0:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y +dy

                if 0 <= nx < N and 0 <= ny < N and best[nx][ny] is None:
                    enqueue(nx, ny, best[x][y] + 1)
        
        ans = -1
        for x in range(N):
            for y in range(N):
                if best [x][y] is None:
                    return -1
                if grid[x][y] ==0:
                    ans = max(ans, best[x][y])
        return ans