# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.out = 0
        def traverse(node, val):
            if not node:
                return

            if node.val >= val:
                self.out += 1
                val = node.val
            
            traverse(node.left, val)
            traverse(node.right, val)
        
        traverse(root, root.val)
        return self.out