# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def getMax(node, current):
            if node is None:
                return 0
            
            return max(
                getMax(node.left, current*2 +1),
                getMax(node.right, current*2 +2),
                current
            )
        
        mx = getMax(root, 0)
        def findGap(node, current):
            if node is None:
                if current < mx:
                    return True
                return False
            
            return findGap(node.left, current*2+1) or findGap(node.right, current*2+2)
        return not findGap(root, 0)