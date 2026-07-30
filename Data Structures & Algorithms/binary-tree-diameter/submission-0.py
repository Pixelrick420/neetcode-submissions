class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            
            ldepth = depth(node.left)
            rdepth = depth(node.right)
            self.diameter = max(
                self.diameter, 
                ldepth + rdepth 
            )
            return 1 + max(ldepth, rdepth)
        
        depth(root)
        return self.diameter