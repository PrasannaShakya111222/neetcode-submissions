class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                #  array is sorted, discontinue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()
        backtrack(0, target)
        return result