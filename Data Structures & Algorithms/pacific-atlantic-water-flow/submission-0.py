class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        # Pacific Ocean: top & left borders
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, 0, pacific)
        # Atlantic Ocean: bottom & right borders
        for c in range(n):
            dfs(m - 1, c, atlantic)
        for r in range(m):
            dfs(r, n - 1, atlantic)
        # Cells reachable from both oceans
        return [[r, c] for r in range(m)
                       for c in range(n)
                       if (r, c) in pacific and (r, c) in atlantic]