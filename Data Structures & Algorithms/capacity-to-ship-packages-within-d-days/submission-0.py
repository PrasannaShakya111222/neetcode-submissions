class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Minimum capacity must be at least heaviest package
        # Maximum capacity is sum of all packages
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # Check if 'mid' capacity enough to ship within given days
            current_weight = 0
            required_days = 1
            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0
                current_weight += weight
            # If it takes more days than allowed, the capacity is too small
            if required_days > days:
                left = mid + 1
            else:
                right = mid  # Try to find smaller feasible capacity       
        return left