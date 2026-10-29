class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        n = len(s)
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        def backtrack(start: int) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return result