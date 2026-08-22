# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def recc(node, curr_max):
            if not node:
                return
            nonlocal count
            if node.val >= curr_max:
                count += 1

            curr_max = max(curr_max, node.val)

            recc(node.left, curr_max)
            recc(node.right, curr_max)

        recc(root,float("-inf"))
        return count
            



