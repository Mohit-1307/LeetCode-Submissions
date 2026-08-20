class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                # Empty subtree is a BST
                # min, max, sum, is_bst
                return (float('inf'), float('-inf'), 0, True)

            left_min, left_max, left_sum, left_bst = dfs(node.left)
            right_min, right_max, right_sum, right_bst = dfs(node.right)

            # Check whether current subtree is a BST
            if left_bst and right_bst and left_max < node.val < right_min:
                curr_sum = left_sum + node.val + right_sum

                ans = max(ans, curr_sum)

                return (
                    min(left_min, node.val),
                    max(right_max, node.val),
                    curr_sum,
                    True
                )

            # Current subtree is not a BST
            return (0, 0, 0, False)

        dfs(root)
        return ans