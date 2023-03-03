class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        P = 71755440315342536873
        B = 27

        needle_hash = 0
        for c in needle:
            needle_hash *=B
            needle_hash += (ord(c) - ord('a') + 1)
            needle_hash %= P

        M = len(needle)
        N = len(haystack)

        BM = pow(B, M, P)

        rolling_hash = 0
        for i in range(N):
            rolling_hash *= B
            rolling_hash += ord(haystack[i]) - ord('a') + 1
            if i - M >=0:
                rolling_hash -= (ord(haystack[i - M]) - ord('a')+ 1) * BM
            rolling_hash %=P

            if i + 1 >= M and rolling_hash == needle_hash:
                return i - M + 1
        return -1