class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--; // Adjust for 1-based indexing
            int remainder = columnNumber % 26;
            result.append((char) ('A' + remainder));
            columnNumber /= 26;
        }
        // extracted characters from right to left, reverse result
        return result.reverse().toString();
    }
}