from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        need=Counter(t)
        window={}
        have=0
        need_count=len(need)

        left=0
        best_len=float("inf")
        best_start=0

        for right, char in enumerate(s):
            window[char]=window.get(char,0)+1

            if char in need and window[char]==need[char]:
                have +=1

            while have==need_count:
                window_len=right-left+1

                if window_len <best_len:
                    best_len= window_len
                    best_start =left

                left_char=s[left]
                window[left_char] -=1

                if left_char in need and window[left_char] < need[left_char]:
                    have -=1

                left +=1

        if best_len==float("inf"):
            return ""

        return s[best_start:best_start+best_len]
