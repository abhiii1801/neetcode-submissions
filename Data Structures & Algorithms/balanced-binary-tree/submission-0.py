# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def balanced(node):
            if not node:
                return 0

            left = balanced(node.left)
            right = balanced(node.right)

            if abs(left - right) > 1:
                nonlocal ans
                ans = False

            return 1 + max(left, right)

        balanced(root)
        return ans

