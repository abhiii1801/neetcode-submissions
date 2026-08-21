# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def max_len(node):
            if not node:
                return 0

            left = max_len(node.left)
            right = max_len(node.right)

            nonlocal ans
            ans = max(ans, left + right)

            return 1 + max(left, right)

        max_len(root)
        return ans




