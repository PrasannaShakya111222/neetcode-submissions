class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n: int, i: int):
            val = nums[i]
            while (i << 1) + 1 < n:
                child = (i << 1) + 1
                if child + 1 < n and nums[child + 1] > nums[child]:
                    child += 1
                if nums[child] <= val:
                    break
                nums[i] = nums[child]
                i = child
            nums[i] = val

        n = len(nums)
        for i in range((n >> 1) - 1, -1, -1):
            heapify(n, i)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)
        return nums
