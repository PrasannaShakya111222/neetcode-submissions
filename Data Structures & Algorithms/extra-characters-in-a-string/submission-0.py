class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        words = set(dictionary)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            # Treat s[i] as extra character
            dp[i] = dp[i + 1] + 1
            # Try matching dictionary words starting at i
            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]