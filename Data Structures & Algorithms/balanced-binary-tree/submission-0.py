# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True

        def height(node):
            if not node:
                return 0
            
            lheight = height(node.left)
            rheight = height(node.right)
            self.isbalanced &= (abs(lheight - rheight) <= 1)
            return 1 + max(lheight, rheight)
        
        height(root)
        return self.isbalanced