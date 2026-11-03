class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([("0000", 0)])
        visited = {"0000"}
        while queue:
            current, turns = queue.popleft()
            if current == target:
                return turns
            for i in range(4):
                digit = int(current[i])
                # Rotate forward & backward
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    next_state = (
                        current[:i] +
                        str(new_digit) +
                        current[i+1:]
                    )
                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        return -1