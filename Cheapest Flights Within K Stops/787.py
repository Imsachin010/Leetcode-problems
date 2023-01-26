class Solution:
    def findCheapestPrice(self, k: int, flights: List[List[int]], src: int, dst: int, maxK: int) -> int:
        maxK +=1
        adj_list = collections.defaultdict(list)

        for u,v, price in flights:
            adj_list[u].append((v, price))

        distances = {}
        h = []
        def maybe_enqueue(node, k, d):
            if k <= maxK and ((node, k) not in distances or distances[(node,k)] > d):
                distances[(node,k)]= d
                heapq.heappush(h,(d,k,node))

        maybe_enqueue(src, 0, 0)

        while len(h) > 0:
            d, k , node = heapq.heappop(h)

            if node ==dst:
                return d
            if distances[(node, k)]<d:
                continue

            for v, p in adj_list[node]:
                maybe_enqueue(v, k+1, d+p)
        
        return -1