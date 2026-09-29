class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # Found target
            if nums[mid] == target:
                return True
            # case: duplicates make impossible to know which side is sorted
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target lies within sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                # Check if target lies within sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1                
        return False