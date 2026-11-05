class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        # adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        # Check for cycles & connectivity
        if not dfs(0, -1):
            return False
        return len(visited) == n