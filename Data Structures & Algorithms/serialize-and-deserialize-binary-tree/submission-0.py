class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        out = [str(root.val)]
        que = collections.deque()
        que.append(root)

        while que:
            qLen = len(que)
            for _ in range(qLen):
                node = que.popleft()
                
                if node.left:
                    out.append(str(node.left.val))
                    que.append(node.left)
                else:
                    out.append("N")
                
                if node.right:
                    out.append(str(node.right.val))
                    que.append(node.right)
                else:
                    out.append("N")
        return '|'.join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        tokens = data.split('|')
        n = len(tokens)

        root = TreeNode(int(tokens[0]))
        que = collections.deque()
        que.append(root)
        index = 1

        while index < n:
            qLen = len(que)
            for _ in range(qLen):
                node = que.popleft()
                if tokens[index] != "N":
                    node.left = TreeNode(int(tokens[index]))
                    que.append(node.left)
                
                if tokens[index + 1] != "N":
                    node.right = TreeNode(int(tokens[index + 1]))
                    que.append(node.right)
                index += 2

        return root



