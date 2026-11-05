class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract last bit
            bit = n & 1
            # Shift result left & add extracted bit
            result = (result << 1) | bit
            # Remove last bit from n
            n >>= 1
        return result