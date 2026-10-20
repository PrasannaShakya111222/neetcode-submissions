class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word is not None:
                result.append(nxt.word)
                nxt.word = None  # Avoid duplicate results
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] != "#":
                        dfs(nr, nc, nxt)
            board[r][c] = ch
            # Prune exhausted Trie branches
            if not nxt.children and nxt.word is None:
                del node.children[ch]
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result