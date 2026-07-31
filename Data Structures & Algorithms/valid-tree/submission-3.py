from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = [False] * n
        def traverse(node, parent):
            visited[node] = True

            for neib in adjList[node]:
                if neib == parent:
                    continue
                
                elif visited[neib]:
                    return False
                
                elif not traverse(neib, node):
                    return False
            
            return True
        
        return traverse(0, -1) and all(visited)
