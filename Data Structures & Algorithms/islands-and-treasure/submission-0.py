class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        # Add all treasure chests to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Multi-source BFS
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries & empty rooms
                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))