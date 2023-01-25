class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        INF = 10 ** 20
        def bfs(start):
            distances = [INF] * N
            q = collections.deque()
        
            distances[start] = 0
            q.append(start)

            while len(q) >0:
                x = q.popleft()
                d = distances[x]

                if edges[x] != -1 and distances[edges[x]] == INF:
                    distances[edges[x]] = d+1
                    q.append(edges[x])

            return distances
        
        d1 =bfs(node1)
        d2 = bfs(node2)
        best = INF
        besti = -1
        
        for index, (x,y) in enumerate(zip(d1,d2)):
            d = max(x,y)

            if d != INF and best >d:
                best = d
                besti = index

        return besti