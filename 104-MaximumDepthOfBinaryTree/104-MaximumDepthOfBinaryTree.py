# Last updated: 7/23/2025, 11:18:10 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.counter_depth = 0
        self.max_depth = 0

        def depth(root):

            self.counter_depth += 1

            if not root.right and not root.left:
                self.max_depth = max(self.counter_depth, self.max_depth)
                return self.max_depth

            if root.left:
                depth(root.left)
                self.counter_depth -= 1

            if root.right:
                depth(root.right)
                self.counter_depth -= 1

            return self.max_depth

        result = depth(root)

        return result