impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();

        for i in 0..n {
            if nums[i] == target {
                return i as i32;
            }
        }
        -1
    }
}