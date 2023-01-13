# You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

# You are also given a string s of length n, where s[i] is the character assigned to node i.

# Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        N = len(s)
        adj_list = collections.defaultdict(list)

        for u, v in enumerate(parent):
            if p == -1:
                continue
            if s[u] == s[p]:
                continue
        
            adj_list[u].append(v)
            adj_list[v].append(u)
        seen =[False]*N
        bestpath = 0
        def longestPath(node, parent):
            seen[node] = True

            longest = []
            for child in adj_list[node]:
                if child != parent:
                    longest.append(longestPath(child, node))            
                if len(longest) >=3 and longest[2] >longest[1]:
                    longest[1], longest[2]=longest[2], longest[1]
                if len(longest) >=2 and longest[1] >longest[0] :
                    longest[0], longest[1]=longest[1], longest[0]
                
                if len(longest) >= 3:
                    longest.pop()

            nonlocal bestpath
            bestpath = max(bestpath, sum(longest) + 1)
            return max(longest,default=0) + 1
        
        for i in range(N):
            if not seen[i]:
                longestPath(i, -1)
        return bestpath





        