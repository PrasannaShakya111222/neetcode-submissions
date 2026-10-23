class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path, options):
            if not options:
                result.append(path)
                return
            for i in range(len(options)):
                # Choose option, remove it from remaining options, & recurse
                backtrack(path + [options[i]], options[:i] + options[i+1:])  
        backtrack([], nums)
        return result