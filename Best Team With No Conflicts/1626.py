class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(sorted((a, s) for s, a in zip(scores,ages)))
        N = len(players)

        cache = [None] * (N+1)
        hasCache = [False] * (N+1)

        def getBest(index):
            if index == N:
                return 0
            
            if hasCache[index]:
                return cache[index]


            best = players[index][1]
            for j in range(index+1, N):
                if players[j][1] >= players[index][1]:
                    best = max(best, getBest(j) + players[index][1])
                
            hasCache[index] = True
            cache[index] = best
            return best
        
        return max(getBest(x) for x in range(N))
