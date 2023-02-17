# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        INF = 10**20
        prev = -INF
        ans = INF

        def traverse(node):
            if node is None:
                return
            
            left = traverse(node.left)
            nonlocal ans
            nonlocal prev
            ans = min(ans, node.val - prev)
            prev = node.val

            right = traverse(node.right)
        
        traverse(root)
        return ans