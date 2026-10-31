"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # Hash map to store original node -> cloned node mapping
        visited = {}
        # Clone root node & put in map
        clone = Node(node.val)
        visited[node] = clone
        # Queue for BFS traversal
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            # Iterate through all neighbors of current node
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # Clone neighbor & store in map
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Connect cloned neighbor to cloned current node
                visited[curr].neighbors.append(visited[neighbor])
        return clone