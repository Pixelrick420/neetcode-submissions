
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ordinal = 0
        self.value = -1

        def traverse(node):
            if not node:
                return
            
            if self.ordinal < k:
                traverse(node.left)
                self.ordinal += 1
                if self.ordinal == k:
                    self.value = node.val
                traverse(node.right)
        traverse(root)
        return self.value

