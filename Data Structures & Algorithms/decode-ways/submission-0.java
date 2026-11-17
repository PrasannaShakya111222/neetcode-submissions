class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0;
        }
        int n = s.length();
        int dp2 = 1; // Represents dp[i-2]
        int dp1 = 1; // Represents dp[i-1]
        for (int i = 1; i < n; i++) {
            int curr = 0;
            // Check single digit decoding
            if (s.charAt(i) != '0') {
                curr += dp1;
            }
            // Check 2 digit decoding
            int twoDigit = Integer.parseInt(s.substring(i - 1, i + 1));
            if (twoDigit >= 10 && twoDigit <= 26) {
                curr += dp2;
            } 
            dp2 = dp1;
            dp1 = curr;
        }
        return dp1;
    }
}