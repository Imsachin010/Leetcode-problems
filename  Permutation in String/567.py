class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.Counter(s1)
        current = collections.Counter()
        N = len(s1)
        for index, c in enumerate(s2):
            current[c]+=1
            if index - N >=0:
                current[s2[index - N]] -=1
            
            if index + 1 >=N:
                if current == count:
                    return True
                

        return False