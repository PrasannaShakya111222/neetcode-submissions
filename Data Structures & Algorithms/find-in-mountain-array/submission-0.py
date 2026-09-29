class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # Find peak of  mountain
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low
        # Search increasing left side
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1       
        # Search decreasing right side
        low, high = peak, n - 1
        while low <= high:
            mid = (low + high) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                low = mid + 1
            else:
                high = mid - 1            
        return -1