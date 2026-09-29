class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # The min possible largest sum is max element in nums
        # The max possible largest sum is sum of all elements
        low, high = max(nums), sum(nums)
        ans = high
        # function to check if max_sum capacity is feasible with <= k subarrays
        def canSplit(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    # Start new subarray
                    subarrays += 1
                    current_sum = num
                    # If  exceed k subarrays, max_sum is too small
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
        # Binary search for  optimal max sum
        while low <= high:
            mid = low + (high - low) // 2        
            if canSplit(mid):
                ans = mid       # Record valid minimized sum
                high = mid - 1  # find smaller max sum
            else:
                low = mid + 1   # Increase allowed sum threshold        
        return ans