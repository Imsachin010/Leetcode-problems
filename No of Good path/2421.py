class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        N = len(vals)

        parents = [i for i in range(N)]
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def union(a,b):
            ua = ufind(a)
            ub = ufind(b)

            parents[ua] = ub

        val_lookup = collections.defaultdict(list)
        for index, x in enumerate(vals):
            val_lookup[x].append(index)
        
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        ans = 0
        keys = sorted(val_lookup.keys())
        for x in keys:
            nodes = val_lookup[x]

            for u in nodes:
                for v in adj_list[u]:
                    if x >= vals[v]:
                        union(u,v)
                
            lookup = collections.Counter()
            for u in nodes:
                ans += lookup[ufind(u)]
                lookup[ufind(u)] += 1
        ans += N
        return ans
