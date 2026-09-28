class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases for 0 and 1
        if x < 2:
            return x
        # Square root of x where x >= 2 is always less than x // 2
        left, right = 1, x // 2 
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1       
        # 'right' will be floor value when perfect square not found
        return right