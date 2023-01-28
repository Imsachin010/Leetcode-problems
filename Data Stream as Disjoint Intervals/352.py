from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.sl = SortedList()
        
    def addNum(self, value: int) -> None:
        self.sl.add((value, value))

    def getIntervals(self) -> List[List[int]]:
        r = list(self.sl)
        N = len(r)
        self.sl = SortedList()
        
        stack = []
        for s, e in r:
            if len(stack) >0 and stack[-1][1] + 1 >= s:
                ps, pe = stack.pop()
                stack.append((min(ps, s), max(pe, e)))
            else:
                stack.append((s, e))
        
        for s,e in stack:
            self.sl.add((s, e))
        return stack


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
