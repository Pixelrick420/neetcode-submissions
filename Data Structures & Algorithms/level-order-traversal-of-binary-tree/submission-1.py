class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque();
        q.append(root)
        out = []
        while q:
            qlen = len(q)
            level = []
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                out.append(level)
        return out