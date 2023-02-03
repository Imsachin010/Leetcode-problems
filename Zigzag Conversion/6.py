class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        
        rows = [[] for _ in range(numRows)]

        row = 0
        direction = 1
        for c in s:
            rows[row].append(c) 
            row += direction

            if row ==0 or row ==numRows - 1:
                direction *= 1

        ans = ["".join(row) for row in rows]
        return "".join(ans)