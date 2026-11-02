class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                board[r][c] != 'O'):
                return
            # Mark this cell safe
            board[r][c] = '#'
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        # Traverse first & last columns
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        # Traverse first & last rows
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        # Capture surrounded regions & restore safe regions
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O' 