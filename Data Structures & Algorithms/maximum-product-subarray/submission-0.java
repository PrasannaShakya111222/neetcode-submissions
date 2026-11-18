class Solution {
    public int maxProduct(int[] nums) {
        int maxProduct = nums[0];
        int max = nums[0];
        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            if (num < 0) {
                int temp = max;
                max = min;
                min = temp;
            }
            max = Math.max(num, max * num);
            min = Math.min(num, min * num);
            maxProduct = Math.max(maxProduct, max);
        }
        return maxProduct;
    }
}