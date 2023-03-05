class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        q = collections.deque()
        INF = 10 ** 20
        best =[INF] * N

        lookup = collections.defaultdict(list)

        for i in range(N):
            lookup[arr[i]].append(i)
        
        q.append(0)
        best[0] = 0
        done = set()

        while len(q) >0:
            current = q.popleft()
            if current == N - 1:
                return best[current]
            
            for x in [current -1, current +1]:
                if 0 <= x < N and best[current] +1 < best[x]:
                    q.append(x)
                    best[x] = best[current] +1
            
            if arr[current] not in done:
                done.add(arr[current])
                
                for x in lookup[arr[current]]:
                    if best[current] +1 < best[x]:
                        q.append(x)
                        best[x] = best[current] + 1
        return -1