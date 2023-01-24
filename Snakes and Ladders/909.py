class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        mboard = []
        for index, row in enumerate(board[::-1]):
            if index % 2== 1 :
                mboard.extend(row[::-1])
            else:
                mboard.extend(row)
            
        q = collections.deque()
        best = [None] * (N * N)
            
        q.append(0)
        best[0] = 0

        while len(q) > 0:
            current = q.popleft()

            for i in range(1, 7):
                nx = current+ i
                if mboard[nx] != -1:
                        nx = mboard[nx]-1
                    
                if nx ==N*N -1:
                    return best[current] +1

                if best[nx] is None:
                    q.append(nx)
                    best[nx] = best[current] + 1
            
        return -1