class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2          
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Target lies within sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right half must be sorted
            else:
                # Target lies within sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1