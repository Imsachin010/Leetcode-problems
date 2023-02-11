class Solution:
    def shortestAlternatingPaths(self, N: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def parse(edges):
            e = collections.defaultdict(list)
            for u, v in edges:
                e[u].append(v)
            return e
        edges = [parse(redEdges), parse(blueEdges)]
        q = collections.deque()
        INF = 10 ** 20
        best = [[INF] * N for _ in range(2) ]

        def enqueue(distance, node, colour):
            q.append((distance, node, colour))
            best[colour][node] = distance

        for c in range(2):
            enqueue(0,0, c)

        while len(q) > 0:
            distance, node, colour = q.popleft()

            for v in edges[colour][node]:
                new_colour = 1 - colour

                if best[new_colour][v] == INF:
                    enqueue(distance + 1, v, new_colour)

        ans = []
        for i in range(N):
            m = min(best[0][i], best[1][i])
            if m == INF:
                m = -1
            ans.append(m)
        return ans