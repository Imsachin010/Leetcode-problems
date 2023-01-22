class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        def recurse(index, current):
            if index == N:
                ans.append(current[:])
                return
            
            for i in range(index, N):
                c =s[index: i+1]
                if c == c[::-1]:
                    current.append(c)
                    recurse(i + 1,current)
                    current.pop()
        
        recurse(0, [])
        return ans