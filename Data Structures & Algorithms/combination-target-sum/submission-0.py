class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    continue
                path.append(nums[i])
                # Reuse same no.
                backtrack(i, remaining - nums[i])
                path.pop()
        backtrack(0, target)
        return result