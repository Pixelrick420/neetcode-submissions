from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        components = 0
        visited = [False] * n

        def traverse(node):
            visited[node] = True
            for neib in adjList[node]:
                if not visited[neib]:
                    traverse(neib)

        for node in range(n):
            if not visited[node]:
                traverse(node)
                components += 1
        
        return components