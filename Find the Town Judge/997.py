class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_someone = [False] * n
        trusted_by = [0] * n

        for u,v in trust:
            u -=1
            v -=1
            trust_someone[u] = True
            trusted_by[v]+=1

        for i in range(n):
            if not trust_someone[i] and trusted_by[i] == n-1:
                return i+1
        return -1