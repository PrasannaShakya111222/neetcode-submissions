"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def build(row, col, size):
            # Check if all cells have same value
            first = grid[row][col]
            same = True
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first:
                        same = False
                        break
                if not same:
                    break
            # If all values are same, create leaf
            if same:
                return Node(first, True, None, None, None, None)
            half = size // 2
            # Divide into 4 quadrants
            topLeft = build(row, col, half)
            topRight = build(row, col + half, half)
            bottomLeft = build(row + half, col, half)
            bottomRight = build(row + half, col + half, half)
            return Node(
                0,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )
        return build(0, 0, n)