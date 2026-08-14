# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right:

class Solution:
    def minCameraCover(self, root):
        cameras = 0

        def dfs(node):
            nonlocal cameras

            if not node:
                return 2  # Covered

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                cameras += 1
                return 1  # Has camera

            if left == 1 or right == 1:
                return 2  # Covered

            return 0  # Not covered

        if dfs(root) == 0:
            cameras += 1

        return cameras