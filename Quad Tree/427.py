class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N =len(grid)

        def construct_helper(left, top, right, bottom):
            if left == right:
                return Node(grid[top][left], True, None, None, None, None)
            
            mid_x = (top+bottom) // 2
            mid_y = (left + right) // 2

            topleft = construct_helper(left, top, mid_y,mid_x)
            topright = construct_helper(mid_y+1, top, right,mid_x)
            bottomleft = construct_helper(left, mid_x+1, mid_y,bottom)
            bottomright = construct_helper(mid_y+1, mid_x+1, right,bottom)

            if(topleft.val == topright.val == bottomleft.val == bottomright.val) and \
                topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf:

                return Node(topleft.val, True, None, None, None, None)
            
            return Node(0, False, topleft, topright, bottomleft, bottomright)
        
        return construct_helper(0,0, N -1, N-1)
