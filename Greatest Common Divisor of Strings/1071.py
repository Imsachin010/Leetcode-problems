class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N = len(str1)
        M = len(str2)

        for L in range(N, 0, -1):
            if N % L !=0:
                continue

            s = str[:L]
            copies = N//L
            if s * copies != str1:
                continue

            copies = M//L
            if s * copies != str2:
                continue
            return s
        
        return ""