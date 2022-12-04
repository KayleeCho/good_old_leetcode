class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:  # skewed tree
            return 1 + max(left, right)

        return min(left, right) + 1