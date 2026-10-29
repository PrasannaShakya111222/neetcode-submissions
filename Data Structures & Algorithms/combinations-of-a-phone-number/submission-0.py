
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        path = []
        def backtrack(index):
            if index == len(digits):
                result.append("".join(path))
                return
            letters = phone[digits[index]]
            for ch in letters:
                path.append(ch)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result