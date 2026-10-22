class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack(1)
        return result