class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            # Add without carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # Convert 32-bit unsigned result to signed integer
        if a <= MAX_INT:
            return a
        return ~(a ^ MASK)