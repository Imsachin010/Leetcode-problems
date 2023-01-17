class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        zeroes = 0
        ones = s.count("1")
        best = ones

        for i in range (N - 1, -1, -1):
            if s[i] == "0":
                zeroes += 1
            else:
                s[i] == "1"
                ones -= 1
            best = min(zeroes + ones,best)
        return best
            