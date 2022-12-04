# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        deepest_sum = 0
        depth = 0
        queue = deque([(root, 0)])

        while queue:
            node, curr_depth = queue.popleft()
            if node.left is None and node.right is None:  # reached the leaf node
                if depth < curr_depth:
                    depth = curr_depth
                    deepest_sum = node.val
                elif depth == curr_depth:
                    deepest_sum += node.val  # update existing sum
            else:
                if node.left:
                    queue.append((node.left, curr_depth + 1))
                if node.right:
                    queue.append((node.right, curr_depth + 1))

        return deepest_sum