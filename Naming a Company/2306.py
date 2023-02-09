class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        s = set(ideas)
        good = [[0]* 26 for _ in range(26)]
        orda= ord('a')

        for idea in ideas:
            ai = ord(idea[0]) - orda

            for bi, f in enumerate(string.ascii_lowercase):
                new_idea = f +idea[1:]
                
                if new_idea not in s:
                    good[ai][bi] +=1

        total = 0
        for ai in range(26):
            for bi in range(26):
                total += good[ai][bi] * good[bi][ai]
        return total
