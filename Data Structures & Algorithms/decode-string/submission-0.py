class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        current=""
        num=0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                # Save current string and repeat count
                stack.append((current, num))
                current = ""
                num = 0
            elif char == "]":
                # Get string and count from before '['
                previous, repeat = stack.pop()
                current = previous + current * repeat
            else:
                current += char
        return current