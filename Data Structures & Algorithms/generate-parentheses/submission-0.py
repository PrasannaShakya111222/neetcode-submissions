class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current_str, open_count, close_count):
            # Base Case: If current string reaches maximum possible length
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            # can always add open parenthesis if not reached 'n'
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
            # can only add close parenthesis if it matches open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)  
        # Start recursion with empty string & 0 counts
        backtrack("", 0, 0)
        return result  