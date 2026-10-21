class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            # Exclude nums[i]
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return result