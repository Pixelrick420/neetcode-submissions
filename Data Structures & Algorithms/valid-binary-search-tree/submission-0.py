class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, minval, maxval):
            if not node:
                return True
            
            if minval < node.val < maxval:
                return traverse(node.left, minval, node.val) and traverse(node.right, node.val, maxval)
            
            return False
        
        return traverse(root, -float('inf'), float('inf'))