# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        ans = []
        # if the depth is even number, push from backward
        # if the depth is odd n umber, push with array
        if root is None:
            return ans

        queue = deque([(root, 1)])

        while queue:
            curr_level_nodes = len(queue)
            curr_level_array = []
            for _ in range(curr_level_nodes):
                curr_node, curr_depth = queue.popleft()

                if curr_depth % 2 == 0:
                    curr_level_array.insert(0, curr_node.val)
                else:
                    curr_level_array.append(curr_node.val)

                if curr_node.left:
                    queue.append((curr_node.left, curr_depth + 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_depth + 1))
            ans.append(curr_level_array)
        return ans
