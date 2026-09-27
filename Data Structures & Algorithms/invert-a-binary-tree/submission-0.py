# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # 上書きを防ぐためにtmpに退避
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # 再帰処理
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root