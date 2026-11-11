class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        # Build adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        # Add all leaf nodes
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        remaining = n
        # Remove leaves level by level
        while remaining > 2:
            size = len(q)
            remaining -= size
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        return list(q)