# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list= collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        ans = [None]*n

        def traverse(node,parent):  
            current_f = [0]*26
            for child in adj_list[node]:
                if child != parent:
                    f= traverse(child,node)
                    for i in range(26):
                        current_f[i] += f[i]
            current_f[ord(labels[node])-ord('a')] +=1            
            ans[node] = current_f[ord(labels[node])-ord('a')]
            return current_f


        traverse(0, -1)
        return ans