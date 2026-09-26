class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Ensure A is smaller array to minimize binary search range
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2    # Index for array A
            j = half - i - 2    # Index for array B
            
            # Get border elements, handle out-of-bound cases with infinity
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # If total number of elements odd
                if total % 2:
                    return min(Aright, Bright)
                # If total number of elements even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                
            elif Aleft > Bright:
                # Too many elements from A's left side, move left
                r = i - 1
            else:
                # Too few elements from A's left side, move right
                l = i + 1