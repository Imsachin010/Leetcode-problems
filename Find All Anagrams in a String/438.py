class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = collections.Counter(p)
        scount = collections.Counter()
        M = len(p)

        ans = []
        for index, c in enumerate(s):
            scount[c] +=1

            if index >= M:
                scount[s[index - M]] -= 1

            if index >= M - 1 and pcount == scount:
                ans.append(index - M + 1)
        return ans
