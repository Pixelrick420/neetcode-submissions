class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        out = []
        while q:
            qlen = len(q)
            cur = None
            for _ in range(qlen):
                node = q.popleft()
                if node:
                    cur = node.val
                    q.append(node.left)
                    q.append(node.right)
            if cur is not None:
                out.append(cur)
        return out