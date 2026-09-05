func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, num :=range nums{
        complement:= target-num
        if index, ok:=seen[complement];ok{
            return []int{index,i}
        }
        seen[num]=i
    }
    return []int{}
}