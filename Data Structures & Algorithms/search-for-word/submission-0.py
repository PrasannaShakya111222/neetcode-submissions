class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r, c, index):
            # If matched all characters
            if index == len(word):
                return True
            # Check bounds, character match, & visited status
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[index]):
                return False
            # Temporarily mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            # Explore all 4 neighboring directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )
            # Backtrack: restore cell's original value
            board[r][c] = temp
            return found
        # Start DFS from every cell on board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True      
        return False