class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]

        while stack:
            node, currSum = stack.pop()
            currSum += node.val

            if node.left is None and node.right is None:
                if currSum == targetSum:
                    return True

            if node.left:
                stack.append((node.left, currSum))

            if node.right:
                stack.append((node.right, currSum))

        return False