class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        lookup = set(words)
        
        def is_good(word):
            L = len(word)
            dp = [False] * (L + 1)

            lookup.remove(word)

            dp[0] = True
            for i in range(L):
                if dp[i]:
                    for j in range(i, L):
                        if word[i:j+1] in lookup:
                            dp[j + 1] |= dp[i]

            lookup.add(word)
            return dp[L]

        ans = []
        for word in words:
            if is_good(word):
                ans.append(word)

        return ans 