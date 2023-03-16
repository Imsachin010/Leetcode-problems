# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_lookup = {}
        for index, x in enumerate(inorder):
            inorder_lookup[x] = index

        poststack = postorder[:]
        def construct(left, right):
            if left > right:
                return None
            current = poststack.pop()
            index = inorder_lookup[current]

            node = TreeNode(current)
            node.right = construct(index+1, right)
            node.left = construct(left, index-1)

            return node
        return construct(0, len(inorder)-1)