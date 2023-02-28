# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        P = 27292996856087
        B = 51341

        seen = set()
        ans = collections.defaultdict(list)

        def dfs(node):
            if node is None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            v = ((node.val + 200) + left * B + right * right * B * B) % P
            if v in seen:
                ans[v] = node
            seen.add(v)
            return v
        dfs(root)
        return list(ans.values())
