class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        // Rolling array storing dp[i], dp[i+1], dp[i+2], dp[i+3]
        int[] dp = new int[4];
        for (int i = n - 1; i >= 0; i--) {
            int best = Integer.MIN_VALUE;
            int take = 0;
            for (int k = 1; k <= 3 && i + k - 1 < n; k++) {
                take += stoneValue[i + k - 1];
                best = Math.max(best, take - dp[(i + k) % 4]);
            }
            dp[i % 4] = best;
        }
        if (dp[0] > 0) {
            return "Alice";
        } else if (dp[0] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}