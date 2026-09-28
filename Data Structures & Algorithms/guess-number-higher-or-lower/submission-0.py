# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            # Find middle point to split search range
            mid = (low + high) // 2
            res = guess(mid)
            if res == 0:
                # Found correct number
                return mid
            elif res == -1:
                # Guess too high, narrow search to lower half
                high = mid - 1
            else:
                # Guess too low, narrow search to upper half
                low = mid + 1     
        return -1