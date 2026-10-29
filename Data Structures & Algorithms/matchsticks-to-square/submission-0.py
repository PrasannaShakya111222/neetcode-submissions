class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        sides = [0] * 4
        def backtrack(index):
            if index == len(matchsticks):
                return True
            stick = matchsticks[index]
            for i in range(4):
                if sides[i] + stick <= target:
                    sides[i] += stick
                    if backtrack(index + 1):
                        return True
                    sides[i] -= stick
                # Avoid equivalent empty sides
                if sides[i] == 0:
                    break
            return False
        return backtrack(0)