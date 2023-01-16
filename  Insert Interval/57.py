# Inseting interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        ans = []

        added = False

        currentS = currentE = None
        for s,e in intervals:
            if not added and ne< s:
                if currentS is not None and currentE is not None:
                    ans.append([currentS, currentE])
                else:
                    ans.append(newInterval)
                added = True

            overlap = False
            if s <= ns <= e and currentS is None:
                currentS = s
                overlap= True
            
            if s<= ne <= e:
                currentE = e
                overlap = True
            if ns<= s <= ne and currentS is None:
                currentS = ns
                overlap = True
            if ns <= e <= ne:
                currentE = ne
                overlap = True
            if not overlap:
                ans.append([s,e])

        if not added:
            if currentS is not None:
                ans.append([currentS, currentE])
            else:
                ans.append(newInterval)
        
        return ans
