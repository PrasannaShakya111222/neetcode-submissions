class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0
        # Find all rotten & fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        # BFS directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:
            # Process all oranges rotten at current minute
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1